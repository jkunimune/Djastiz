#translator.py

import collections
import csv
import json
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
from os import path
import pandas as pd
import pickle
import re
import unicodedata



logging.basicConfig(level=logging.ERROR)


DIACRITIC_GUIDE = {
	('àá', 'a'), 
	('é', 'e'),
	('ìíĩ', 'i'),
	('òōõ', 'o'),
	('ùúũ', 'u'),
}

SOURCE_LANGUAGES = {
	'cmn':.2243,
	'spa':.1495,
	'epo':.1429,
	'eng':.0930,
	'hin':.0898,
	'ben':.0838,
	'pan':.0422,
	'jav':.0286,
	'yor':.0260,
	'mar':.0248,
	'msa':.0206,
	'ibo':.0186,
	'fil':.0153,
	'swa':.0111,
	'zul':.0081,
	'nya':.0067,
	'xho':.0056,
	'sho':.0050,
	'sot':.0041,
}

ALLOWED_CHANGES = [
	('mɱ', 'm'),
	('nɳŋɴ', 'n'),
	('ɲ', 'nj'),
	('pbɓ', 'p'),
	('tdʈɖɗ', 't'),
	('cɟʄ', 'kj'),
	('kɡɠ', 'k'),
	('fɸ', 'f'),
	('θsz', 's'),
	('ʃʒɕʑʂʐ', 'c'),
	('ç', 'hj'),
	('xχħhɦ', 'h'),
	('wʷɰ', 'w'),
	('jʲʎ', 'j'),
	('lɬrɾɽɭ', 'l'),
	('aɑæ', 'a'),
	('eèɛ', 'e'),
	('iɪɨ', 'i'),
	('oɔɒ', 'o'),
	('uʊʉɯ', 'u'),
	('- ˩˨˧˦˥ʰʼˈˌː⁀', '')
]
RESTRICTED_CHANGES = [
	('ǃǀ', 't'),
	('ǁ', 'k'),
	('ʄ', 'kj'),
	('ð', 's'),
	('ɣʁʕʀ', 'h'),
	('ɮ', 'l'),
	('ə', 'a'),
	('ɤ', 'aw'),
	('œ', 'ew'),
]

VERB_DERIVATIONS = ['ANTONYM','INCOHATIVE','CESSATIVE','REVERSAL','POSSIBILITY','VERB']
NOUN_DERIVATIONS = ['GENITIVE','SBJ','OBJ','IND','AMOUNT','LOCATION','TIME','INSTRUMENT','CAUSE','METHOD','COMPLEMENT','RELATIVE']
MISC_DERIVATIONS = ['OPPOSITE']


def get_curly_brace_pair(string):
	""" return the indices of a matching pair of {} in string """
	assert '{' in string and '}' in string, "There aren't enough curly braces in {}".format(string)
	i_open = string.index('{')
	assert '}' in string[i_open:], "Curly braces out of order: {}".format(string)
	i_close = i_open+1
	depth = 1
	while i_close < len(string):
		if string[i_close] == '}':
			depth -= 1
		elif string[i_close] == '{':
			depth += 1
		if depth == 0:
			return i_open, i_close
		i_close += 1
	raise ValueError("Unbalanced curly braces: {}".format(string))


def reduce_phoneme(phoneme, before, after):
	""" return the nearest lsl phoneme and the distance """
	if phoneme.endswith('̩'): # this is how I do syllabics
		cons, dist = reduce_phoneme(phoneme[0], before, after)
		try:
			return {'m':'u','n':'e','l':'o','r':'a','ɹ':'a'}[phoneme[0]] + cons, dist+1 # TODO: check context
		except KeyError:
			logging.error("epitran is trying to pass off /{}/ as a phoneme...?".format(phoneme))
			return cons, dist
	elif phoneme.endswith('̯'): # convert semivowels
		if phoneme[0] in 'iɪeɛ':
			return reduce_phoneme('j', before, after)
		elif phoneme[0] in 'uʊoɔɯɤ':
			return reduce_phoneme('w', before, after)
		elif phoneme[0] in 'yʏø':
			return reduce_phoneme('ɥ', before, after)
		else:
			raise IllegalArgumentException(phoneme)
	for combined, vowel in DIACRITIC_GUIDE: # remove unnecessary diacritics
		if phoneme in combined:
			return vowel, 0
	for fulls, reduced in ALLOWED_CHANGES: # these loops should cover most sounds
		if phoneme in fulls:
			return reduced, 0
	for fulls, reduced in RESTRICTED_CHANGES:
		if phoneme in fulls:
			return reduced, 1
	if phoneme in 'βvⱱʋ':
		return 'w', 0 # TODO: use context
	if phoneme == 'ʝ':
		return 'j', 0 # TODO: use context
	if phoneme == 'y':
		return 'i', 1 # TODO: use context
	if phoneme == 'ɥ':
		return 'j', 1 # TODO: use context
	if phoneme == 'ɹ':
		return '', 1 # TODO: use context
	if phoneme == '̃':
		return 'n', 0 # TODO: use context
	if unicodedata.combining(phoneme):
		return '', 0 # ignore all combining diacritics not expliticly listed here
	raise ValueError(phoneme)


def apply_phonotactics(ipa, ending='csktp'):
	""" take some phonetic alphabet and approximate it with my phonotactics, and say how many changes there were """
	logging.debug(ipa)
	lsl, changes = '', 0
	next_phoneme = ''
	while ipa:
		if len(ipa) > 1 and ipa[-1] in '̩̯': # combine certain combining diacritics
			ipa, phoneme = ipa[:-2], ipa[-2:]
		elif len(ipa) > 2 and ipa[-2] == '͡': # treat tied characters as one phoneme
			ipa, phoneme = ipa[:-3], ipa[-1:]
		else:
			ipa, phoneme = ipa[:-1], ipa[-1:]

		new_phoneme, dist = reduce_phoneme(phoneme, ipa[-1:], next_phoneme)
		lsl = new_phoneme + lsl
		next_phoneme = phoneme

	return lsl, changes


def choose_key(entry):
	""" choose the meaning key to use in the dictionary """
	key = entry['source'][1:] if entry['source'].startswith('*') else entry['eng'][0]
	if len(key.split()) > 1 and key.split()[0] in ['be', 'find', 'have', 'give', 'do', 'get', 'can']:
		key = ' '.join(key.split()[1:]) # remove English grammar particles
	elif entry['partos'] == 'verb' and not entry['source'].startswith('*'):
		key = 'to '+key
	return key


def choose_word(english, real_words, counts):
	""" determine what word should represent english, based on the given foreign dictionaries and
		current representation of each language. Return the source lang, source orthography, source IPA, and my word """
	logging.info("choosing a word for {}".format(english))
	options, scores = [], []
	for lang, target_frac in sorted(SOURCE_LANGUAGES.items()):
		try:
			orthography, broad, narrow = real_words[english][lang]
		except KeyError:
			logging.error("missing translation of '{}' in {}".format(english, lang))
			orthography, broad, narrow = english, english, english

		if broad == '*':
			continue # star means we don't have that word

		try:
			reduced, changes = apply_phonotactics(broad)
		except ValueError as e:
			logging.error("could not read IPA in {} \"{}\" /{}/; '{}' may not be an IPA symbol".format(lang, english, broad, e))
			reduced, changes = broad, 0

		score = sum(counts.values())*target_frac - counts[lang] # determine how far above or below its target this language is
		score -= 2.0*changes # favour words that require fewer changes

		options.append((lang, orthography, narrow, reduced))
		logging.debug(*options[-1])
		scores.append(score)

	for i, ((lang, orthography, narrow, reduced), score) in enumerate(zip(options, scores)):
		score -= 3.0*len(reduced) # prefer longer words
		for _, _, _, reduced2 in options:
			for c1, c2 in zip(reduced, reduced2): # prefer words that are similar in other languages
				if c1 == c2:	score += 0.5
				else:			break
		scores[i] = score
	
	logging.info("Out of \n{};\nI choose {}".format(',\n'.join(str(tup) for tup in options), options[np.argmax(scores)]))
	return options[np.argmax(scores)]


def derive(source_word, deriv_type):
	""" Apply that powerful morphological derivation system I keep bragging about """
	return source_word+deriv_type


def load_dictionary(directory):
	""" load words from the given directory into a big dictionary thing """
	words = {} # each key is an English gloss key; value is {definition, my word, derivatives}
	queue = collections.deque()

	for filename in [
		'special', 'postposition', 'sentence particle', 'specifier',
		'pronoun', 'numeral', 'verb', 'noun', 'compound word', 'loanword'
	]:
		with open(path.join(directory, filename+'.csv'), 'r', encoding='utf-8') as f:
			word_set = pd.read_csv(f, dtype=str, na_filter=False)
			word_set['partos'] = filename
			queue.extend(word_set.itertuples(index=False))

	while queue:
		entry = queue.popleft()
		try:
			entry['derivatives'] = {} # don't forget to start counting these
		except TypeError:
			entry = entry._asdict() # convert row to a dict
			entry['derivatives'] = {}

		for key, value in entry.items():
			if '*' in value:
				starred = re.search(r'\*(\w+)\b', value).group(1) # look for explicit source word selections
				entry['source'] = '*'+starred
				entry[key] = value.replace('*','')
				break

		unprocessed_derivatives = collections.defaultdict(lambda: {key:'' for key in entry}) # start looking for noun derivatives that need to be processed later

		for key, value in entry.items():
			while '{' in value: # handle explicit derivatives
				i, j = get_curly_brace_pair(value)
				for deriv_statement in value[i+1:j].split('|'):
					if re.match(r'^[A-Z]+:', deriv_statement):
						k = deriv_statement.index(':')
						unprocessed_derivatives[deriv_statement[:k]][key] = deriv_statement[k+1:]
					else:
						assert value[i-4:i-1] in ['SBJ','OBJ','IND'], value
						unprocessed_derivatives[value[i-4:i-1]][key] = deriv_statement
				value = (value[:i-1] + value[j+1:]).strip()
				entry[key] = value

		for key in entry:
			if key not in ['source', 'ltl', 'derivatives', 'partos']:
				entry[key] = entry[key].split('; ') # separate definitions when applicable
				for i, meaning in reversed(list(enumerate(entry[key]))):
					if meaning == '' or meaning in entry[key][:i]:
						entry[key].pop(i) # ignore any empty things and duplicates

		for i, eng_meaning in enumerate(entry['eng']):
			if eng_meaning.startswith('beI '): # handle implicit derivatives
				entry['eng'][i] = eng_meaning.replace('beI ', 'be ')
				unprocessed_derivatives['IND']['eng'] += '; '+eng_meaning[4:]
			elif eng_meaning.startswith('be '):
				unprocessed_derivatives['OBJ']['eng'] += '; '+eng_meaning[3:]

		if ' OF ' in entry['source']:
			i = entry['source'].index(' OF ')
			deriv_type, deriv_word = entry['source'][:i], entry['source'][i+4:]
			assert deriv_word in words, '{} of "{}" declared before "{}"'.format(deriv_type, deriv_word, deriv_word)
			words[deriv_word]['derivatives'][deriv_type] = entry

		for possible_gloss in entry['eng']:
			if possible_gloss not in words:
				words[possible_gloss] = entry
				break
		if words[possible_gloss] != entry:
			gloss = '{}{:03d}'.format(entry['eng'][0], len(words))
			logging.warn("There is no possible gloss for {}. '{}' will be used as a key.".format(entry, gloss))
			words[gloss] = entry

		for deriv_type, deriv_dict in unprocessed_derivatives.items():
			deriv_dict['source'] = '{} OF {}'.format(deriv_type, possible_gloss)
			if deriv_type in VERB_DERIVATIONS:
				deriv_dict['partos'] = 'verb'
			elif deriv_type in NOUN_DERIVATIONS:
				deriv_dict['partos'] = 'noun'
			elif deriv_type in MISC_DERIVATIONS:
				deriv_dict['partos'] = entry['partos']
			else:
				raise TypeError("What is {}".format(deriv_type))
			queue.append(deriv_dict) # finally, put the unprocessed derivatives in the queue

	return words


def fill_blanks(my_words, real_words):
	""" come up with words from the source dictioraries for all nouns and verbs that aren't
		onomotopoeias, and update the compound words accordingly """
	tallies = collections.Counter() # start by counting how many words we have of each language already
	for entry in my_words.values():
		if entry['partos'] not in ['noun','verb','loanword','compound word']:
			if entry['source'] and len(entry['source'].split()[0]) == 3:
				tallies[entry['source'].split()[0]] += 1
	logging.info(tallies)
				
	for entry in my_words.values():
		if entry['partos'] in ['noun','verb']:
			if entry['source'].startswith('*') or entry['source'] == '' or entry['source'].split()[0] in SOURCE_LANGUAGES:
				eng = choose_key(entry)
				lang, source_orth, source_ipa, my_word = choose_word(eng, real_words, tallies)
				entry['ltl'] = my_word
				entry['source'] = "{} <{}> [{}]".format(lang, source_orth, source_ipa)
				tallies[lang] += 1

	for entry in my_words.values():
		if ' OF ' in entry['source']:
			d_type, d_gloss = entry['source'].split(' OF ')
			entry['ltl'] = derive(my_words[d_gloss]['ltl'], d_type)
		elif entry['partos'] == 'compound word':
			entry['ltl'] = ''
			for component in entry['source'].split():
				try:
					entry['ltl'] += my_words[component.replace('-',' ')]['ltl']
				except KeyError as e:
					logging.error("No {} for {}'s {}".format(e, entry['eng'][0], entry['source'].split()))


def save_dictionary(dictionary, directory):
	""" save the updated values of all these nouns and verbs and compounds """
	pass


def format_dictionary(dictionary, directory):
	""" make a bunch of nicely-formatterd dictionaries in Markdown and LaTeX """


def measure_corpus(directory):
	""" count the occurences of all words in this corpus """
	return collections.Counter()



if __name__ == '__main__':
	all_words = load_dictionary('words')
	with open('../data/all_languages.p', 'rb') as f:
		source_dictionaries = pickle.load(f)
	fill_blanks(all_words, source_dictionaries)
	logging.info(json.dumps(all_words, indent=2))
	save_dictionary(all_words, 'words')
	format_dictionary(all_words, '../Dictionaries')
	hist = measure_corpus('../Example Texts')
	for word, count in hist.most_common(36):
		logging.info("{:03}\t{}".format(count, word))

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



logging.basicConfig(level=logging.INFO)


DIACRITIC_GUIDE = {
	('àá', 'a'), 
	('èé', 'e'),
	('ìí', 'i'),
	('òō', 'o'),
	('ùúṳ', 'u'),
	('ĩ', 'ĩ'),
	('õ', 'õ'),
	('ũ', 'ũ'),
}

SOURCE_LANGUAGES = {
	'cmn':.2089,
	'epo':.1429,
	'spa':.1329,
	'eng':.0866,
	'hin':.0836,
	'ben':.0781,
	'ara':.0586,
	'pan':.0393,
	'jav':.0267,
	'yor':.0243,
	'mar':.0231,
	'msa':.0192,
	'ibo':.0174,
	'fil':.0142,
	'swa':.0103,
	'zul':.0076,
	'nya':.0062,
	'xho':.0053,
	'sho':.0046,
	'sot':.0038,
}

ALLOWED_CHANGES = [
	('aɑæ', 'a'),
	('eɛ', 'e'),
	('iɪɨ', 'i'),
	('oɔɒ', 'o'),
	('uʊʉɯ', 'u'),
	('mɱ', 'm'),
	('nɳŋɴ', 'n'),
	('ɲ', 'nj'),
	('pbɓ', 'p'),
	('tdʈɖɗ', 't'),
	('cɟʄ', 'kj'),
	('kɡɠq', 'k'),
	('fɸ', 'f'),
	('θsz', 's'),
	('ʃʒɕʑʂʐ', 'c'),
	('ç', 'hj'),
	('xχħhɦ', 'h'),
	('wʷɰ', 'w'),
	('jʲʎ', 'j'),
	('lɬrɾɽɭ', 'l'),
	('- ˩˨˧˦˥ʰʼˈˌː͡⁀..,，​', '')
]
RESTRICTED_CHANGES = [
	('ə', 'a'),
	('ɤʌ', 'aw'),
	('œø', 'ew'),
	('ǃǀ', 't'),
	('ǁ', 'k'),
	('ʄ', 'kj'),
	('ð', 's'),
	('ɣʁʕʀ', 'h'),
	('ɮ', 'l'),
	('ʔ', ''),
]

ALL_VOWELS = 'aɑæeɛiɪɨoɔɒuʊʉɯəɤʌœø'
ALL_GLIDES = 'wʷɰjʲʎ'
PHONEME_TABLE = ['eaoiu', 'jw', 'h', 'l', 'ktp', 'f', 'cs', 'nm'] # the lawnsosliel phonemes, arranged by strength
INVERSES = {'a':'a', 'e':'o', 'i':'u', 'j':'w', 'l':'t', 'n':'k', 'm':'p', 'h':'s', 'c':'f'}
for k, v in list(INVERSES.items()):	INVERSES[v] = k # inversion is involutory

SUPPORTED_LANGUAGES = ["eng","spa"] # the languages for which I have the dictiorary translated

VERB_DERIVATIONS = ['ANTONYM','INCOHATIVE','CESSATIVE','PROGRESSIVE','REVERSAL','POSSIBILITY','VERB']
NOUN_DERIVATIONS = ['GENITIVE','SBJ','OBJ','IND','AMOUNT','LOCATION','TIME','INSTRUMENT','CAUSE','METHOD',
		'COMPLEMENT','RELATIVE','INTERROGATIVE','INDETERMINATE','DETERMINATE','PROXIMAL']
MISC_DERIVATIONS = ['OPPOSITE']


def difference(a, b):
	""" count the characters different between a and b """
	return abs(len(a) - len(b)) + sum([ai != bi for ai, bi in zip(a, b)])


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


def strength_of(phoneme):
	""" return the row of this phoneme in the phoneme table """
	for i in range(len(PHONEME_TABLE)):
		if phoneme in PHONEME_TABLE[i]:
			return i
	assert False, phoneme


def is_consonant(phoneme):
	""" is this a big strong consonant? """
	return phoneme not in ALL_VOWELS and phoneme not in ALL_GLIDES


def strongest(cluster, preference=[]):
	""" return the strongest phoneme of the bunch, always choosing one from the preference if available """
	if preference is not None and any([cons in preference for cons in cluster]):
		cluster = filter(lambda cons:cons in preference, cluster)
	return max(cluster, key=strength_of)


def has_antonym(entry):
	""" does this word ever need to be inverted? """
	return any([deriv_type in deriv['derivatives'] for deriv in list(entry['derivatives'].values())+[entry] for deriv_type in ['ANTONYM','OPPOSITE','REVERSAL']])


def get_antonym(word):
	""" invert all letters up to the second consonant """
	new_word = INVERSES[word[0]]
	for c in word[1:]:
		if not is_consonant(c):	new_word += INVERSES[c]
		else:					break # we're out of the switching section
	new_word += word[len(new_word):]
	return new_word


def reduce_phoneme(phoneme, before, after):
	""" return the nearest lsl phoneme and the distance in phone space """
	if phoneme.endswith('̩'): # this is how I do syllabics
		consonant, dist = reduce_phoneme(phoneme[0], before, after)
		try:
			anaptyxis = {'m':'u','n':'e','l':'o','r':'a','ɹ':'a'}[phoneme[0]] + consonant # the vowel to insert next to the syllabic consonant
		except KeyError:
			logging.error("epitran is trying to pass off /{}/ as a phoneme...?".format(phoneme))
			anaptyxis = 'u'
		if before == '' or (not is_consonant(before) and is_consonant(after)):
			return consonant+anaptyxis, dist+1 # put the vowel after it if that works better
		else:
			return anaptyxis+consonant, dist+1 # but usually put it before
	elif phoneme.endswith('̯'): # convert semivowels
		if phoneme[0] in ['i','ɪ','e','ɛ']:
			return reduce_phoneme('j', before, after)
		elif phoneme[0] in ['u','ʊ','o','ɔ','ɯ','ɤ']:
			return reduce_phoneme('w', before, after)
		elif phoneme[0] in ['y','ʏ','ø']:
			return reduce_phoneme('ɥ', before, after)
		else:
			raise ValueError(phoneme)
	for fulls, reduced in ALLOWED_CHANGES: # these loops should cover most sounds
		if phoneme in fulls:
			return reduced, 0
	for fulls, reduced in RESTRICTED_CHANGES:
		if phoneme in fulls:
			return reduced, 1
	if phoneme in ['β','v','ⱱ','ʋ']: # these ones will take care of the weird ones that depend on context
		if not before or not after or before in ['w','u','o'] or after in ['w','u']:
			return 'f', 1 # use 'f' when you need a consonant or to create contrast,
		else:
			return 'w', 0 # 'w' otherwise
	if phoneme == 'ʝ':
		return ('hj', 0) if not before else ('j', 0) # /ʝ/ gets a free 'h' if it needs it
	if phoneme == 'y':
		if before in ['ʷ','w','u','ʊ','o','ɔ'] or after in ['ʷ','u','ʊ','o','ɔ']:
			return 'i', 0 # /y/ looks like /i/ when surrounded by other rounded things
		elif before in ['ʲ','j','i','ɪ','e','ɛ'] or after in ['ʲ','i','ɪ','e','ɛ']:
			return 'u', 0 # and like /u/ when surrounded by other front things
		else:
			return 'iw', 1 # and not like much on its own
	if phoneme == 'ɥ':
		if before in ['u','ʊ','o','ɔ'] or after in ['u','ʊ','o','ɔ']:
			return 'j', 0 # /ɥ/ looks like /j/ when surrounded by other rounded things
		elif before in ['i','ɪ','e','ɛ'] or after in ['i','ɪ','e','ɛ']:
			return 'w', 0 # and like /w/ when surrounded by other front things
		else:
			return 'ju', 1 # and not like much on its own
	if phoneme == 'ɹ':
		if not before or not after:
			return 'l', 0 # use 'l' when you need a consonant
		elif not is_consonant(reduce_phoneme(before,'','')[0]) and not is_consonant(reduce_phoneme(after,'','')[0]):
			return 'l', 0 # or when intervocalic
		else:
			return '', 0 # otherwise it's better as nothing
	if phoneme == '̃':
		return 'm' if after in ['p','f'] else 'n', 0 # nasal vowels can be n or m
	if unicodedata.combining(phoneme):
		return '', 0 # ignore all combining diacritics not expliticly listed here
	raise ValueError(phoneme)


def apply_phonotactics(ipa, ending='csktp'): # TODO: what if dynamic verbs end in 'a'+something
	""" take some phonetic alphabet and approximate it with my phonotactics, and say how many changes there were """
	to_convert = ipa
	lsl, changes = '', 0
	next_phoneme = ''
	while to_convert:
		for charset, value in DIACRITIC_GUIDE:
			if to_convert[-1] in charset:
				to_convert = to_convert[:-1] + value # start by breaking up any poorly-represented diacritics
				continue

		if len(to_convert) > 1 and to_convert[-1] in '̩̯': # combine certain combining diacritics
			to_convert, phoneme = to_convert[:-2], to_convert[-2:]
		elif len(to_convert) > 2 and to_convert[-2] == '͡': # treat tied characters as one phoneme
			to_convert, phoneme = to_convert[:-3], to_convert[-1:]
		else:
			to_convert, phoneme = to_convert[:-1], to_convert[-1:]

		new_phoneme, dist = reduce_phoneme(phoneme, to_convert[-1:], next_phoneme)
		changes += dist
		lsl = new_phoneme + lsl
		next_phoneme = phoneme

	while not is_consonant(lsl[-1]): # make sure it ends with a consonant
		num_vowels = len(re.findall(r'[eaoiu]', lsl))
		if num_vowels == 1 or not is_consonant(lsl[-2]): # either by adding a consonant to the end if there are multiple trailing vowel/glides or there aren't enough vowels
			lsl += 'h' if 'h' in ending else 's'
			changes += 0.5
		else: # or by removing if there is just one
			lsl = lsl[:-1]
			changes += 0.5

	for i in range(len(lsl)-1, 0, -1):
		if lsl[i-1] == lsl[i]: # remove double lettres
			lsl = lsl[:i-1] + lsl[i:]
			changes += 0.5
	for i in range(len(lsl)-1, 0, -1):
		if is_consonant(lsl[i-1]) and is_consonant(lsl[i]): # remove consonant clusters
			one_true_consonant = strongest(lsl[i-1:i+1], preference=ending if i == len(lsl)-1 else [])
			lsl = lsl[:i-1] + one_true_consonant + lsl[i+1:]
			changes += 1

	if not is_consonant(lsl[0]): # make sure it starts with a consonant
		lsl = 'h' + lsl
		changes += 1
	if not lsl[-1] in ending: # make sure it ends on the right class of letter
		lsl = lsl[:-1] + INVERSES[lsl[-1]]
		changes += 1

	lsl = re.sub(r'([lnmhcsfktp])w([lnmhcsfktp])', r'\1u\2', lsl) # these rogue semivowels are weird and need to go die.
	lsl = re.sub(r'([lnmhcsfktp])j([lnmhcsfktp])', r'\1i\2', lsl)
	lsl = re.sub(r'ej([lnmhcsfktp\b])', r'e\1', lsl) # restricted diphthongs
	lsl = re.sub(r'ow([lnmhcsfktp\b])', r'o\1', lsl)
	lsl = re.sub(r'w?uw?', 'u', lsl) # these are effectively double letters
	lsl = re.sub(r'j?ij?', 'i', lsl)

	logging.debug("{} -> {}".format(ipa, lsl))
	return lsl, changes


def choose_key(entry):
	""" choose the meaning key to use to look this up in other languages """
	key = entry['source'][1:] if entry['source'].startswith('*') else entry['eng'][0]
	if len(key.split()) > 1 and key.split()[0] in ['be', 'find', 'have', 'give', 'do', 'get', 'can']:
		key = ' '.join(key.split()[1:]) # remove English grammar particles
	elif entry['partos'] == 'verb' and not entry['source'].startswith('*'):
		key = 'to '+key
	return key


def legal_new_word(word, all_words, open_words, has_antonym, lang='', ipa=''): # TODO: no i/j distinction nor u/w
	""" does this word at all conflict with what already exists? """
	test_word = word.replace('j','i').replace('w','u')
	if test_word in all_words:
		logging.debug("{}'s {} ({}) is already a word".format(lang, test_word, ipa))
		return False # make sure it doesn't collide; if it does, don't add it to the list
	if has_antonym:
		if difference(word, get_antonym(word)) < 2:
			logging.debug("{} is too similar to its own antonym".format(word))
			return False
		if not legal_new_word(get_antonym(word), all_words, open_words, False, lang=lang, ipa=ipa):
			logging.debug("And that endangers its antonym")
			return False
	for preexisting in open_words: # make sure it doesn't look like an open word plus a potential closed word
		if re.fullmatch(preexisting+r'[lnmhcsfktp]([eaoiu]+[lnmhcsfktp])+', test_word):
			logging.debug("{}'s {} ({}) collides with {}".format(lang, repr(word), ipa, repr(preexisting)))
			return False # this is a little weird, I admit, but important for morphological self-segregation
		if re.fullmatch(r'([lnmhcsfktp][eaoiu]+)+[lnmhcsfktp]'+preexisting, test_word):
			logging.debug("{}'s {} ({}) collides with {}".format(lang, repr(word), ipa, repr(preexisting)))
			return False
		if test_word == preexisting+'l' or test_word == 'l'+preexisting:
			logging.debug("{}'s {} ({}) collides with {}".format(lang, repr(word), ipa, repr(preexisting)))
			return False
	return True


def choose_word(english, real_words, counts, partos, has_antonym=False, all_words={}, open_words=None):
	""" determine what word should represent english, based on the given foreign dictionaries and
		current representation of each language. Return the source lang, source orthography, source IPA, and my word """
	if open_words is None:	open_words = all_words

	logging.info("choosing a word for '{}'".format(english))
	options, scores = [], []
	for lang, target_frac in SOURCE_LANGUAGES.items():
		try:
			orthography, broad, narrow = real_words[english][lang]
		except KeyError:
			logging.error("missing translation of '{}' in {}".format(english, lang))
			orthography, broad, narrow = english, english.replace('g','ɡ'), english # I don't want to stop the proɡram when this happens, so I use the Enɡlish word as a fake IPA transcription

		if broad == '*':
			continue # star means we don't have that word

		try:
			reduced, changes = apply_phonotactics(broad, ending='lnmhf' if partos=='noun' else 'csktp')
		except ValueError as e:
			logging.error("could not read IPA in {} \"{}\" /{}/; '{}' may not be an IPA symbol".format(lang, english, broad, e))
			continue

		score = sum(counts.values())*target_frac - counts[lang] # determine how far above or below its target this language is
		if not legal_new_word(reduced, all_words, open_words, has_antonym, lang=lang, ipa=narrow):
			score = float('-inf') # don't allow it to be taken if it's not legal (but still put it in the list so we can compare it to other candidates)
		score -= 3.0*changes # favour words that require fewer changes

		options.append((lang, orthography, narrow, reduced))
		scores.append(score)

	for i, ((lang, orthography, narrow, reduced), score) in enumerate(zip(options, scores)):
		score -= 1.0*len(reduced) # prefer shorter words
		for lang2, _, _, reduced2 in options:
			for c1, c2 in zip(reduced, reduced2): # prefer words that are similar in other major languages
				if c1 == c2:								score += 2*SOURCE_LANGUAGES[lang2]
				elif is_consonant(c1) or is_consonant(c2):	break
		scores[i] = score

	if np.isfinite(max(scores)):
		logging.info("Out of \n{};\nI choose {}".format(',\n'.join(str(tup) for tup in options), options[np.argmax(scores)]))
		return options[np.argmax(scores)]
	else:
		raise Exception("There are no possible words for '{}' that don't conflict with words I already have. Oh god. How did this happen? Do I need even more languages?".format(english))


def derive(source_word, deriv_type, all_words, has_antonym):
	""" Apply that powerful morphological derivation system I keep bragging about """
	if deriv_type in ['ANTONYM', 'REVERSAL', 'OPPOSITE']:
		return get_antonym(source_word)
	elif deriv_type in ['CESSATIVE']:
		if has_antonym:
			return get_antonym(source_word) + all_words['begin']['ltl']
		else:
			return source_word + all_words['end']['ltl']
	elif deriv_type in ['NEGATIVE', 'INCOHATIVE', 'PROGRESSIVE', 'POSSIBILITY', 'GENITIVE', 'SBJ', 'OBJ',
		'IND', 'AMOUNT', 'LOCATION', 'TIME', 'INSTRUMENT', 'CAUSE', 'METHOD']:
		inflection_word = {
			'NEG':'no', 'INC':'begin', 'PRO':'continue', 'POS':'be possible', 'GEN':'of', 'SBJ':'who', 'OBJ':'which', 'IND':'whom',
			'AMO':'the amount that', 'LOC':'where', 'TIM':'when', 'INS':'with which', 'CAU':'why', 'MET':'by which'}[deriv_type[:3]]
		return source_word + all_words[inflection_word]['ltl']
	elif deriv_type in ['INTERROGATIVE', 'INDETERMINATE', 'DETERMINATE', 'PROXIMAL']:
		inflection_word = {'INT':'what', 'IND':'something', 'DET':'it', 'PRO':'this'}[deriv_type[:3]]
		return all_words[inflection_word]['ltl'] + ' ' + source_word
	elif deriv_type == 'RELATIVE':
		return 'l' + source_word
	elif deriv_type == 'COMPLEMENT':
		return 'l' + source_word # TODO: what am I going to do about these complements? They can't take a verb; then stuff would collide. But they can't not take a verb. Then they look like relatives.
	elif deriv_type == 'VERB':
		return all_words['which']['ltl'] + source_word + all_words['do']['ltl']
	else:
		raise ValueError("The {1} of {0}?".format(source_word, deriv_type))


def load_dictionary(directory):
	""" load words from the given directory into a big dictionary thing """
	words = {} # each key is an English gloss key; value is {definition, my word, derivatives}
	queue = collections.deque()

	for filename in [
		'special', 'postposition', 'sentence particle', 'specifier', 'pronoun',
		'proverb', 'numeral', 'verb', 'noun', 'compound word', 'loanword'
	]:
		with open(path.join(directory, filename+'.csv'), 'r', encoding='utf-8') as f:
			word_set = pd.read_csv(f, dtype=str, na_filter=False)
			word_set['partos'] = filename
			queue.extend(word_set.itertuples(index=True))

	while queue: # go through all the words we have to process
		entry = queue.popleft()
		try:
			entry['derivatives'] = {} # start counting its derivatives
		except TypeError:
			entry = entry._asdict() # convert row to a dict
			entry['derivatives'] = {}

		for key in SUPPORTED_LANGUAGES:
			if '*' in entry[key]:
				starred = re.search(r'\*(\w+)\b', entry[key]).group(1) # look for explicit source word selections
				entry['source'] = '*'+starred
				entry[key] = entry[key].replace('*','')
				break

		unprocessed_derivatives = collections.defaultdict(lambda: {key:'' for key in entry}) # start looking for noun derivatives that need to be processed later

		for key in SUPPORTED_LANGUAGES:
			value = entry[key]
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

		for key in SUPPORTED_LANGUAGES:
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
			logging.warning("There is no possible gloss for {}. '{}' will be used as a key.".format(entry, gloss))
			words[gloss] = entry

		if entry['partos'] == 'compound word':
			try:
				entry['partos'] = 'compound '+words[entry['source'].split()[-1].replace('-',' ')]['partos'] # the pos of a compound is based on the last word in it
			except (KeyError, IndexError):
				pass # this'll print an error message later

		for deriv_type, deriv_dict in unprocessed_derivatives.items(): # look at each of the unprocessed derivatives (the things in {})
			deriv_dict['source'] = '{} OF {}'.format(deriv_type, possible_gloss)
			if deriv_type in VERB_DERIVATIONS:
				deriv_dict['partos'] = 'verb'
			elif deriv_type in NOUN_DERIVATIONS:
				deriv_dict['partos'] = 'noun'
			elif deriv_type in MISC_DERIVATIONS:
				deriv_dict['partos'] = entry['partos']
			else:
				raise TypeError("What is {}".format(deriv_type))
			queue.insert(0, deriv_dict) # finally, put the unprocessed derivatives in the queue

	return words


def verify_words(my_words):
	""" check various things to catch mistakes I made with my dictionary """
	errors = 0
	for key, entry in my_words.items():
		if not entry['eng']:
			logging.error("The entry {} has no meaning".format(entry))
			errors += 1
		if not any(w in entry['derivatives'] for w in ['ANTONYM','OPPOSITE','REVERSAL']) and has_antonym(entry):
			logging.error("Derivatives of '{0}' have antonyms even though '{0}' itself does not".format(entry['eng'][0], entry))
			errors += 1
		if entry['partos'].endswith('verb') and 'OBJ' not in entry['eng'][-1]:
			logging.error("{} sure doesn't _look_ like a verb.".format(entry['eng']))
			errors += 1

	if not errors:
		logging.info("Dictionary verified.") # if you make it this far, you've passed my test


def fill_blanks(my_words, real_words):
	""" come up with words from the source dictioraries for all nouns and verbs that aren't
		onomotopoeias, and update the compound words accordingly """
	all_ltl_words = set()
	all_open_ltl_words = set() # the set of open words that can cause isolating morphology issues 
	tallies = collections.Counter() # start by counting how many words we have of each language already
	for entry in my_words.values():
		if entry['partos'] not in ['noun','verb','loanword'] or re.match(r'^ono ', entry['source']): # only count grammar words and onomotopoeias
			if re.match(r'^[a-z][a-z][a-z] <.*> \[.*\]', entry['source']):
				tallies[entry['source'].split()[0]] += 1
			if entry['ltl'] and not entry['partos'].startswith('compound'):
				all_ltl_words.add(entry['ltl'].replace('j','i').replace('w','u'))
				if 'OF' not in entry['source'] and 'ono [' not in entry['source']:
					all_open_ltl_words.add(entry['ltl'].replace('j','i').replace('w','u'))
	logging.info(tallies)
				
	for entry in my_words.values(): # make up words for anything that needs it
		if entry['partos'] in ['noun','verb']:
			if entry['source'].startswith('*') or entry['source'] == '' or entry['source'].split()[0] in SOURCE_LANGUAGES:
				eng = choose_key(entry)
				lang, source_orth, source_ipa, my_word = choose_word(eng, real_words, tallies,
					partos=entry['partos'], has_antonym=has_antonym(entry), all_words=all_ltl_words, open_words=all_open_ltl_words)
				entry['ltl'] = my_word
				entry['source'] = "{} <{}> [{}]".format(lang, source_orth, source_ipa)
				tallies[lang] += 1
				all_ltl_words.add(my_word.replace('j','i').replace('w','u')) # skip the i/j distinction behind the curtain

	for entry in my_words.values(): # derive the derivatives
		if ' OF ' in entry['source']:
			d_type, d_gloss = entry['source'].split(' OF ')
			entry['ltl'] = derive(my_words[d_gloss]['ltl'], d_type, my_words, 'ANTONYM' in entry['derivatives'])
	for entry in my_words.values(): # then compound the compound words
		if entry['partos'].startswith('compound'):
			entry['ltl'] = ''
			if entry['source']:
				for component in entry['source'].split():
					try:
						entry['ltl'] += my_words[component.replace('-',' ')]['ltl']
					except KeyError as e:
						logging.error("No {} for {}'s {}".format(e, entry['eng'][0], entry['source'].split()))
			else:
				logging.error("{} has no components".format(entry['eng'][0]))


def save_dictionary(dictionary, directory):
	""" save the updated values of all these nouns and verbs and compounds """
	for partos in ['verb', 'noun', 'compound word']:
		with open(path.join(directory, partos+'.csv'), 'r', encoding='utf-8') as f:
			rows = pd.read_csv(f, dtype=str, na_filter=False)

		for row_index, row in rows.iterrows():
			for entry in dictionary.values():
				if entry['partos'] == partos and entry['Index'] == row_index:
					row['source'] = entry['source']
					row['ltl'] = entry['ltl']
					break

		with open(path.join(directory, partos+'.csv'), 'w', encoding='utf-8') as f:
			rows.to_csv(f, index=False)


def format_dictionary(dictionary, directory):
	""" make a bunch of nicely-formatterd dictionaries in Markdown and LaTeX """
	pass


def measure_corpus(directory):
	""" count the occurences of all words in this corpus """
	return collections.Counter()



if __name__ == '__main__':
	all_words = load_dictionary('words')
	verify_words(all_words)
	with open('../data/all_languages.pkl', 'rb') as f:
		source_dictionaries = pickle.load(f)
	fill_blanks(all_words, source_dictionaries)
	logging.info(json.dumps(all_words, indent=2))
	logging.info("{} roots, {} of which are of European origin".format(
		sum([re.match(r'<', word['source']) is not None for word in all_words.values()]),
		sum([re.match(r'(eng|spa|epo) <', word['source']) is not None for word in all_words.values()])))
	save_dictionary(all_words, 'words')
	format_dictionary(all_words, '../Dictionaries')
	hist = measure_corpus('../Example Texts')
	for word, count in hist.most_common(36):
		logging.info("{:03}\t{}".format(count, word))

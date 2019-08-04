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
	('òōó', 'o'),
	('ùúṳ', 'u'),
	('ĩ', 'ĩ'),
	('õ', 'õ'),
	('ũ', 'ũ'),
	('ń', 'n'),
}

SOURCE_LANGUAGES = {
	('zh-CN','cmn',.2243),
	('es','spa',.1495),
	('eo','epo',.1429),
	('en','eng',.0930),
	('hi','hin',.0898),
	('bn','ben',.0838),
	# ('ar','ara',.0000),
	('pa','pan',.0422),
	('jv','jav',.0286),
	('yo','yor',.0260),
	('mr','mar',.0248),
	('ms','msa',.0206),
	('ig','ibo',.0186),
	('tl','fil',.0153),
	('sw','swa',.0111),
	('zu','zul',.0081),
	('ny','nya',.0067),
	('xh','xho',.0056),
	('sn','sho',.0050),
	('st','sot',.0041),
}
DESIRED_FRAC = {threelc:num for twolc, threelc, num in SOURCE_LANGUAGES}
THREECODE_TO_TWOCODE = {threelc:twolc for twolc, threelc, num in SOURCE_LANGUAGES}

ALLOWED_CHANGES = [
	('aɑæ', 'a'),
	('eɛ', 'e'),
	('iɪɨ', 'i'),
	('oɔɒ', 'o'),
	('uʊʉɯ', 'u'),
	('mᵐɱᶬ', 'm'),
	('nⁿɳŋᵑɴ', 'n'),
	('pbɓ', 'p'),
	('tdʈɖɗ', 't'),
	('kɡɠq', 'k'),
	('fɸ', 'f'),
	('θsz', 's'),
	('ʃʒɕʑʂʐ', 'c'),
	('xχħhɦ', 'h'),
	('wʷɰ', 'w'),
	('jʲʎ', 'y'),
	('lrɾɽɭ', 'l'),
	('ɬɮ', 'cl'),
	('ʰˤʼ',''),
	('- ˩˨˧˦˥ˈˌː͡⁀..,，​', ''),
]
RESTRICTED_CHANGES = [
	('əɚ', 'a'),
	('ɤʌ', 'aw'),
	('œø', 'ew'),
	('ǃǀ', 't'),
	('ǁ', 'k'),
	('ǂ', 'ky'),
	('ð', 's'),
	('ɣʁʀ', 'h'),
	('ʔʕ', ''),
]
PALATAL_CHANGES = [
	('ɲ', 'ny'),
	('cɟʄ', 'ky'),
	('ç', 'hy'),
]

ALPHABET = 'eaoiuylwnmhcsfktp'
PHONEME_TABLE = ['eaoiu', 'yw', 'h', 'ktp', 'f', 'cs', 'nm', 'l'] # the lawnsosliel phonemes, arranged by strength
INVERSES = {'a':'a', 'e':'o', 'i':'u', 'y':'w', 'l':'t', 'n':'k', 'm':'p', 'h':'c', 's':'f'}
for k, v in list(INVERSES.items()):	INVERSES[v] = k # inversion is involutory

SUPPORTED_LANGUAGES = ["eng","spa"] # the languages for which I have the dictiorary translated

VERB_DERIVATIONS = ['ANTONYM','NEGATIVE','INCOHATIVE','CESSATIVE','PROGRESSIVE','REVERSAL','POSSIBILITY','VERB']
NOUN_DERIVATIONS = ['GENITIVE','SBJ','OBJ','IND','AMOUNT','LOCATION','TIME','INSTRUMENT','CAUSE','METHOD','CONDITION','COMPLEMENT',
		'RELATIVE','INTERROGATIVE','INDETERMINATE','DETERMINATE','PROXIMAL','COUNTRY','LANGUAGE','REGION','PEOPLE']
MISC_DERIVATIONS = ['OPPOSITE']

MARKDOWN_ENTRY = """\
- <a name="{otp}">**{otp}**</a> _{pos}._ ({source_str})  
{definitions}

"""
LATEX_ENTRY = """\
\\textbf{{{otp}}} \\textit{{{pos}.}} ({source_str_tex})
{definitions_tex} \\label{{{otp}}} \\\\
"""
LATEX_REVERSE = """\
\\textbf{{{gloss}}} {translations} \\\\
"""


def difference(a, b):
	""" count the characters different between a and b """
	return abs(len(a) - len(b)) + sum([ai != bi for ai, bi in zip(a, b)])


def latexify(md):
	""" convert some Markdown to LaTeX """
	tex = [""] # list of layers, from outer to inner
	enclosing = [""] # list of enclosing characters
	i = 0
	while i < len(md):
		token = md[i]
		if token == '\\': # a backslash
			i += 1 # groups with the following character
			token += md[i]
		elif token == '~' and i+1 < len(md) and md[i+1] == '~': # as does a tilde
			i += 1 # if the next character is also a tilde
			token += md[i]
		elif token == ']' and i+1 < len(md) and md[i+1] == '(': # '](' is also kind of a special token
			i += 1
			token += md[i]

		if enclosing[-1] == '~~' and token == '~~': # if it's closing an earlier strikethrough
			tex[-2] += '\\sout{{{}}}'.format(tex[-1]) # add the strikethrough
			tex.pop()
			enclosing.pop()
		elif enclosing[-1] == '_' and token == '_': # if it's closing an earlier emphasis
			tex[-2] += '\\textit{{{}}}'.format(tex[-1]) # add the emphasis
			tex.pop()
			enclosing.pop()
		elif enclosing[-1] == '[' and token == ']': # if it's closing an earlier bracket
			tex[-2] += '\\hyperref{{{}}}'.format(tex[-1]) # add a hyperref
			tex.pop()
			enclosing.pop()
		elif enclosing[-1] == '[' and token == '](': # if it's closing an earlier bracket and opening a parenthesis
			tex[-2] += '\\hyperref[{{:}}]{{{}}}'.format(tex[-1]) # add a hyperref with a space for the ref
			tex[-1] = ""
			enclosing[-1] = '('
		elif enclosing[-1] == '(' and token == ')': # if it's closing an earlier parenthesis
			tex[-2] = tex[-2].replace('{:}', tex[-1].replace(r'\#','')) # fill out the hyperref
			tex.pop()
			enclosing.pop()
		elif token[0] == '\\': # if a backslash
			tex[-1] += token[1:] # ask no questions and add the next character literally
		elif token in ['#','$','%','&','{','}']: # if it's a special ascii character
			tex[-1] += '\\'+token # add a backslash
		elif token == "^": # use the escape sequence
			tex[-1] += '\\textasciicircum{}'
		elif token in ['[','~~','_']: # if it's an opening enclosure
			enclosing.append(token) # note it
			tex.append("")
		else: # otherwise
			tex[-1] += token # just add the token
		i += 1

	assert len(enclosing) == 1, "{!r} was never closed in {!r}".format(enclosing, md)
	return tex[0]


def get_curly_brace_pair(string):
	""" return the indices of a matching pair of {} in string """
	assert '{' in string and '}' in string, "There aren't enough curly braces in {}".format(string)
	i_open = string.index('{')
	assert '}' in string[i_open:], "Curly braces out of order: {}".format(string)
	depth = 1
	for i_close in range(i_open+1, len(string)):
		if string[i_close] == '}':
			depth -= 1
		elif string[i_close] == '{':
			depth += 1
		if depth == 0:
			return i_open, i_close
	raise ValueError("Unbalanced curly braces: {}".format(string))


def split_by_bars(string):
	""" return string.split('|'), but ignoring bars in brackets """
	parts = []
	depth = 0
	i_start = 0
	for i_end in range(len(string)):
		if string[i_end] == '{':
			depth += 1
		elif string[i_end] == '}':
			depth -= 1
		elif string[i_end] == '|' and depth == 0:
			parts.append(string[i_start:i_end])
			i_start = i_end+1
	parts.append(string[i_start:])
	return parts


def dehyphenated(key):
	""" return the key of a compound word in a usable state """
	return key.replace('-',' ').replace('=','-')


def strength_of(phoneme):
	""" return the row of this phoneme in the phoneme table """
	for i in range(len(PHONEME_TABLE)):
		if phoneme in PHONEME_TABLE[i]:
			return i
	assert False, phoneme


def is_vowel(phoneme):
	""" is this a pure wholesome vowel? """
	return len(phoneme) == 1 and phoneme in 'aɑæeɛiɪɨoɔɒuʊʉɯəɤʌœø'

def is_consonant(phoneme, ipa=True):
	""" is this a big strong consonant? """
	return len(phoneme) == 1 and phoneme not in 'aɑæeɛiɪɨoɔɒuʊʉɯəɤʌœø' and phoneme not in ('wʷɰjʲɥ' if ipa else 'wy')


def strongest(cluster, preference=[]):
	""" return the strongest phoneme of the bunch, always choosing one from the preference if available """
	if preference is not None and any([cons in preference for cons in cluster]):
		cluster = filter(lambda cons:cons in preference, cluster)
	return max(cluster, key=strength_of)


def has_antonym(entry):
	""" does this word ever need to be inverted? """
	return any([deriv_type in deriv['derivatives'] for deriv in list(entry['derivatives'].values())+[entry] for deriv_type in ['ANTONYM','OPPOSITE','REVERSAL']])


def get_antonym(word):
	""" invert all letters up to the second consonant if applicable """
	try:
		return ''.join(INVERSES[c] for c in word)
	except KeyError:
		return None


def otp_ord(word):
	""" return a key that can be used to alphabetically sort words in oltilip """
	val = 0
	i = 0
	for c in word:
		if c == ' ' or c == "'":
			continue
		try:
			val += ALPHABET.index(c)*len(ALPHABET)**(-i)
		except ValueError:
			raise ValueError("{} contains {}, which is not allowed in Oltilip words.".format(word, c))
		i += 1
	return val


def reduce_phoneme(phoneme, before='', after=''):
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
		elif phoneme[0] in ['u','ʊ','o','ɔ','ɯ','ɤ','ʌ']:
			return reduce_phoneme('w', before, after)
		elif phoneme[0] in ['y','ʏ','ø','œ']:
			return reduce_phoneme('ɥ', before, after)
		else:
			raise ValueError(phoneme)
	for fulls, reduced in ALLOWED_CHANGES: # these loops should cover most sounds
		if phoneme in fulls:
			return reduced, 0
	for fulls, reduced in RESTRICTED_CHANGES:
		if phoneme in fulls:
			return reduced, 1
	if phoneme in ['β','v','ⱱ','ʋ']: # these blocks will take care of the weird ones that depend on context
		if before in ['w','u','ʊ'] or after in ['w','u','ʊ',''] or (before in ['o','ɔ'] and is_consonant(after)): # for example, labial sonorants
			return 'f', 1 # use 'f' to create contrast,
		else:
			return 'w', .5 # 'w' otherwise
	if phoneme == 'ʝ':
		return ('c', 1) if after == 'w' else ('y', 0) # /ʝ/ can become 'c' if needed for contrast
	if phoneme == 'y':
		if before in ['ʷ','w','u','ʊ','o','ɔ'] or after in ['w','u','ʊ','o','ɔ']:
			return 'i', 0 # /y/ looks like /i/ when surrounded by other rounded things
		elif before in ['ʲ','j','i','ɪ','e','ɛ'] or after in ['j','i','ɪ','e','ɛ']:
			return 'u', 0 # and like /u/ when surrounded by other front things
		else:
			return 'iw', 1 # and not like much on its own
	if phoneme == 'ɥ':
		if before in ['u','ʊ','o','ɔ'] or after in ['u','ʊ','o','ɔ']:
			return 'y', 0 # /ɥ/ looks like /j/ when surrounded by other rounded things
		elif before in ['i','ɪ','e','ɛ'] or after in ['i','ɪ','e','ɛ']:
			return 'w', 0 # and like /w/ when surrounded by other front things
		else:
			return 'yu', 1 # and not like much on its own
	if phoneme == 'ɹ':
		if (is_vowel(before) or before == '') and is_vowel(after):
			return 'l', 1 # use 'l' when intervocalic or initial and prevocalic
		else:
			return '', 0 # otherwise it's better as nothing
	if phoneme == 'ɻ':
		if (is_vowel(before) or before == '') and is_vowel(after):
			return 'l', 1 # use 'l' when intervocalic or initial and prevocalic
		else:
			return '', 1 # otherwise it's better as nothing (but not as good in the alveolar case)
	if phoneme in ['ɲ','c','ɟ','ç','ʄ']:
		for fulls, reduced in PALATAL_CHANGES:
			if phoneme in fulls:
				default = reduced # palatals tend to be transcribed as an alveolar plus a [j]
		if is_consonant(after):
			return default[0], 0 # unless they come before a consonant, in which case that's not needed
		else:
			return default, 0
	if phoneme == '̃':
		return 'm' if after in ['p','f'] else 'n', 0 # nasal vowels can be n or m
	if unicodedata.combining(phoneme):
		return '', 0 # ignore all combining diacritics not expliticly listed here
	raise ValueError(phoneme)


def apply_phonotactics(ipa, ending=''):
	""" take some phonetic alphabet and approximate it with my phonotactics, and say how many changes there were """
	to_convert = ipa.replace('̤','')
	lsl, changes = '', 0
	left_phoneme, this_phoneme, next_phoneme = '', '', ''
	while to_convert or left_phoneme: # go backwards through the word
		if to_convert:
			for charset, value in DIACRITIC_GUIDE:
				if to_convert[-1] in charset:
					to_convert = to_convert[:-1] + value # start by breaking up any poorly-represented diacritics
					continue

			if len(to_convert) > 1 and to_convert[-1] in ['̩','̯']: # combine certain combining diacritics
				to_convert, left_phoneme = to_convert[:-2], to_convert[-2:]
			elif to_convert[-1] in 'ɸβszʃʒɕʑʂʐxɣɬ' and len(to_convert) > 2 and to_convert[-2] == '͡': # treat tied fricatives as one phoneme
				to_convert, left_phoneme = to_convert[:-3], to_convert[-1:]
			else:
				to_convert, left_phoneme = to_convert[:-1], to_convert[-1:]
		else:
			left_phoneme = ''

		if this_phoneme:
			new_phoneme, dist = reduce_phoneme(this_phoneme, left_phoneme, next_phoneme)
			changes += dist
			lsl = new_phoneme + lsl

		next_phoneme = this_phoneme
		this_phoneme = left_phoneme # move forward (backward)

	for i in range(len(lsl)-1, 0, -1):
		if lsl[i-1] == lsl[i]: # remove double lettres
			lsl = lsl[:i-1] + lsl[i:]
			changes += 0.5

	lsl = re.sub(r'([lnmhcsfktp])w([lnmhcsfktp])', r'\1u\2', lsl) # these rogue semivowels are weird and need to go die.
	lsl = re.sub(r'([lnmhcsfktp])y([lnmhcsfktp])', r'\1i\2', lsl)
	lsl = re.sub(r'ey([lnmhcsfktp]|$)', r'e\1', lsl) # restricted diphthongs
	lsl = re.sub(r'ow([lnmhcsfktp]|$)', r'o\1', lsl)
	lsl = re.sub(r'w?uw?', 'u', lsl) # these are effectively double letters
	lsl = re.sub(r'y?iy?', 'i', lsl)

	if ending == 'c': # make sure it ends with a consonant
		while not is_consonant(lsl[-1], ipa=False):
			num_vowels = len(re.findall(r'[eaoiu]', lsl))
			if num_vowels > 1 and is_consonant(lsl[-2], ipa=False): # either by removing the last letter if that will work
				lsl = lsl[:-1]
				changes += 1
			else: # or by adding a consonant to the end
				lsl += 'h'
				changes += 1
	elif ending == 'v': # make sure it ends with a vowel
		if lsl[-1] not in 'eaoiu':
			if lsl[-1] == 'y':
				lsl = lsl[:-1] + 'i' # either by changing a semivowel to a vowel if that would work
				changes += 0.5
			elif lsl[-1] == 'w':
				lsl = lsl[:-1] + 'u'
				changes += 0.5
			elif lsl[-1] == 'h' and lsl[-2] in 'eaoiu': # or by removing a final 'h'
				lsl = lsl[:-1]
				changes += 1
			else: # or by just adding another vowel to the end
				lsl += re.findall(r'[eaoiu]', lsl)[-1]
				changes += 1
	if len(lsl) >=2 and lsl[0] not in 'eaoiuyw' and lsl[1] not in 'eaoiuyw': # also, if it starts with two consonants,
		lsl = re.findall(r'[eaoiu]', lsl)[0] + lsl # throw a vowel on the front
		changes += 1

	i = 0
	clusters = []
	while i < len(lsl): # to get the consonant clusters,
		j = i # group letters into sets of vowel/semivowels and consonants
		while j < len(lsl) and (lsl[j] in 'eaoiuyw') == (lsl[i] in 'eaoiuyw'):
			j += 1
		clusters.append(lsl[i:j])
		i = j
	for i in range(len(clusters)):
		cluster = clusters[i]
		if cluster[0] not in 'eaoiuyw': # take all the consonant clusters
			if i == 0 or i == len(clusters)-1:
				max_len = 1
			else:
				max_len = 2
			if len(cluster) > max_len: # that are too long
				changes += len(cluster) - max_len
				idcs = list(range(len(cluster)))
				idcs = [idx for idx in idcs if cluster[idx] not in cluster[idx+1:]] # remove all but the last instance of each particular sound
				idcs.sort(key=lambda idx:strength_of(cluster[idx])) # pick out the most important consonants
				idcs = sorted(idcs[-max_len:])
				clusters[i] = ''.join(cluster[j] for j in idcs) # and reassemble the now reduced cluster
	lsl = ''.join(clusters)

	return lsl, changes


def choose_key(entry):
	""" choose the meaning key to use to look this up in other languages """
	key = entry['source'][1:] if entry['source'].startswith('*') else entry['eng'][0]
	if len(key.split()) > 1 and key.split()[0] in ['be', 'find', 'have', 'give', 'do', 'get', 'can']:
		key = ' '.join(key.split()[1:]) # remove English grammar particles
	elif entry['partos'] == 'verb' and not entry['source'].startswith('*'):
		key = 'to '+key
	return key


def legal_new_word(word, all_words, has_antonym, lang='', ipa=''):
	""" does this word at all conflict with what already exists? """
	test_word = word.replace('y','i').replace('w','u')
	if test_word in all_words:
		logging.debug("{}'s {} ({}) is already a word".format(lang, test_word, ipa))
		return False # make sure it doesn't collide; if it does, don't add it to the list
	for suffix in ['ki','nu','nyo','kwe','powi','calu','ak','lon','les','lum']:
		if test_word != suffix and test_word.endswith(suffix):
			logging.debug("'{}' sounds kind of like it has a {} derivative".format(test_word, suffix))
			return False
	if has_antonym:
		if difference(word, get_antonym(word)) < 2:
			logging.debug("{} is too similar to its own antonym".format(word))
			return False
		if not legal_new_word(get_antonym(word), all_words, False, lang=lang, ipa=ipa):
			logging.debug("And that endangers its antonym")
			return False
	return True


def choose_word(english, real_words, counts, partos, has_antonym=False, all_words={}):
	""" determine what word should represent english, based on the given foreign dictionaries and
		current representation of each language. Return the source lang, source orthography, source IPA, and my word """
	logging.debug("choosing a word for '{}'".format(english))
	options, scores = [], []
	for _, lang, target_frac in SOURCE_LANGUAGES:
		try:
			orthography, broad, narrow = real_words[english][lang]
		except KeyError:
			logging.error("missing translation of '{}' in {}".format(english, lang))
			orthography, broad, narrow = english, english.replace('g','ɡ'), english # I don't want to stop the proɡram when this happens, so I use the Enɡlish word as a fake IPA transcription

		if broad in ['*', '']:
			continue # star means we don't have that word

		try:
			reduced, changes = apply_phonotactics(broad, ending='c' if partos=='noun' else 'v')
		except ValueError as e:
			logging.error("could not read IPA in {} \"{}\" /{}/; '{}' may not be an IPA symbol".format(lang, english, broad, e))
			continue

		score = sum(counts.values())*target_frac - counts[lang] # determine how far above or below its target this language is
		if not legal_new_word(reduced, all_words, has_antonym, lang=lang, ipa=narrow):
			score = float('-inf') # don't allow it to be taken if it's not legal (but still put it in the list so we can compare it to other candidates)
		score -= 10.0*changes**2 # favour words that require fewer changes

		options.append((lang, orthography, narrow, reduced, changes))
		scores.append(score)

	for i, ((lang, orthography, narrow, reduced, changes), score) in enumerate(zip(options, scores)):
		score -= 0.6*len(reduced)**2 # prefer shorter words
		for lang2, _, _, reduced2, _ in options: # prefer words that are similar in other major languages
			if lang2 != lang:
				for is_important in [(lambda c: True), (lambda c: is_consonant(c, ipa=False))]: # measuring similarity as number of matching letters, and number of
					for c1, c2 in zip([c for c in reduced if is_important(c)], [c for c in reduced2 if is_important(c)]): # matching consonants
						if c1 == c2:	score += 3.0*DESIRED_FRAC[lang2]
						else:			break
		scores[i] = score

	if np.isfinite(max(scores)):
		logging.debug("Out of \n{};\nI choose {}".format(',\n'.join(str(tup) for tup in options), options[np.argmax(scores)]))
		return options[np.argmax(scores)][:4]
	else:
		raise Exception("There are no possible words for '{}' that don't conflict with words I already have. Oh god. How did this happen? Do I need even more languages?".format(english))


def derive(source_word, deriv_type, all_words, has_antonym):
	""" Apply that powerful morphological derivation system about which I keep bragging """
	if deriv_type in ['ANTONYM', 'REVERSAL', 'OPPOSITE']:
		return get_antonym(source_word)
	elif deriv_type in ['CESSATIVE']:
		if has_antonym:
			return get_antonym(source_word) + all_words['begin']['otp']
		else:
			return source_word + all_words['end']['otp']
	elif deriv_type in [
			'NEGATIVE', 'INCOHATIVE', 'PROGRESSIVE', 'POSSIBILITY', 'GENITIVE', 'SBJ', 'OBJ', 'IND', 'AMOUNT', 'LOCATION',
			'TIME', 'INSTRUMENT', 'CAUSE', 'METHOD', 'CONDITION', 'LANGUAGE', 'COUNTRY', 'REGION', 'PEOPLE']:
		inflection_word = {
			'NEG':'no', 'INC':'begin', 'PRO':'continue', 'POS':'be possible', 'GEN':'of', 'SBJ':'who (relative)',
			'OBJ':'which (relative)', 'IND':'whom (relative)', 'AMO':'the amount that', 'LOC':'where (relative)',
			'TIM':'when (relative)', 'INS':'with which (relative)', 'CAU':'why (relative)', 'MET':'how (relative)',
			'CON':'for which', 'LAN':'language', 'COU':'country', 'REG':'location', 'PEO':'person',
		}[deriv_type[:3]]
		return source_word + all_words[inflection_word]['otp']
	elif deriv_type in ['INTERROGATIVE', 'INDETERMINATE', 'DETERMINATE', 'PROXIMAL']:
		inflection_word = {'INT':'what', 'IND':'something', 'DET':'it', 'PRO':'this'}[deriv_type[:3]]
		if not all_words[inflection_word]['otp']:
			logging.error("The inflection word for {} seems to be missing".format(deriv_type))
		return all_words[inflection_word]['otp'] + ' ' + source_word
	elif deriv_type == 'RELATIVE':
		return 'l' + source_word
	elif deriv_type == 'VERB':
		return all_words['which']['otp'] + source_word + all_words['do']['otp'] # TODO: why doesn't this actually append kweki?
	else:
		raise ValueError("The {1} of {0}?".format(source_word, deriv_type))


def compile_dictionaries(directory):
	""" compile the csvs of real words I have in my data folder """
	all_transcriptions = {}
	for lang_2, lang_3, _ in SOURCE_LANGUAGES:
		with open('{}/dict_{}.csv'.format(directory, lang_2), 'r', encoding='utf-8', newline='') as f:
			for word, orthography, broad, narrow in csv.reader(f):
				if word not in all_transcriptions:	all_transcriptions[word] = {}
				all_transcriptions[word][lang_3] = (orthography, broad, narrow)
	return all_transcriptions


def load_dictionary(directory):
	""" load words from the given directory into a big dictionary thing """
	words = collections.OrderedDict() # each key is an English gloss key; value is {definition, my word, derivatives}
	queue = collections.deque()

	for filename in [
		'postposition', 'sentence particle', 'specifier', 'pronoun',
		'proverb', 'numeral', 'verb', 'noun', 'loanword', 'compound word',
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
				i, j = get_curly_brace_pair(value) # first dig into the matched braces
				for deriv_statement in split_by_bars(value[i+1:j]): # then separate out the individual derivative statements
					if re.match(r'^[A-Z]+:', deriv_statement):
						k = deriv_statement.index(':')
						unprocessed_derivatives[deriv_statement[:k]][key] = deriv_statement[k+1:]
					else:
						assert value[i-4:i-1] in ['SBJ','OBJ','IND'], '{}\t"{}"\t{}?'.format(value[:i-4], value[i-4:i-1], value[i-1:])
						unprocessed_derivatives[value[i-4:i-1]][key] = deriv_statement
				value = (value[:i-1] + value[j+1:]).strip()
				entry[key] = value

		for key in SUPPORTED_LANGUAGES:
			if key not in ['source', 'otp', 'derivatives', 'partos']:
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
				entry['gloss'] = possible_gloss
				words[possible_gloss] = entry
				break
		if words[possible_gloss] != entry:
			gloss = '{}{:03d}'.format(entry['eng'][0], len(words))
			# logging.warning("There is no possible gloss for {}. '{}' will be used as a key.".format(entry, gloss))
			entry['gloss'] = gloss
			words[gloss] = entry

		if entry['partos'] == 'compound word':
			if ' OF ' in entry['source']:
				if entry['source'].split()[0] in VERB_DERIVATIONS:
					entry['partos'] = 'compound verb'
				elif entry['source'].split()[0] in NOUN_DERIVATIONS:
					entry['partos'] = 'compound noun'
				else:
					raise ValueError("{} should not be in the compound word list".format(entry['source'].split()[0]))
			else:
				try:
					entry['partos'] = 'compound '+words[dehyphenated(entry['source'].split()[-1])]['partos'] # the pos of a compound is based on the last word in it
				except (KeyError, IndexError):
					raise ValueError("Did not understand part of speech of {}".format(words[entry['source']].split()[-1]))

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
		if entry['otp']:
			for entry1 in my_words.values():
				if entry1['eng'] < entry['eng'] and entry1 is not entry and entry1['otp'] == entry['otp']:
					logging.warning("{} ({}) is homophonous with {} ({})".format(entry['otp'], entry['eng'], entry1['otp'], entry1['eng']))
		if not any(w in entry['derivatives'] for w in ['ANTONYM','OPPOSITE','REVERSAL']) and has_antonym(entry):
			logging.error("Derivatives of '{0}' have antonyms even though '{0}' itself does not".format(entry['eng'][0], entry))
			errors += 1
		if entry['partos'].endswith('verb') and not ('OBJ' in entry['eng'][-1]) and not ('see' in entry['eng'][-1] and 'OBJ' in entry['eng'][-2]):
			logging.warning("{} sure doesn't _look_ like a verb.".format(entry['eng']))
			errors += 1

	if not errors:
		logging.info("Dictionary verified.") # if you make it this far, you've passed my test


def fill_blanks(my_words, real_words):
	""" come up with words from the source dictioraries for all nouns and verbs that aren't
		onomotopoeias, and update the compound words accordingly """
	for entry in my_words.values(): # start by clearing the nouns, verbs, derivatives, and compounds
		if (entry['partos'] in ['noun','verb'] and not entry['source'].startswith('ono ')) \
				or (' OF ' in entry['source'] and not (entry['partos'] == 'proverb' or entry['partos'] == 'pronoun')) \
				or entry['partos'].startswith('compound'):
			entry['otp'] = ''

	all_otp_words = set()
	tallies = collections.Counter()
	for entry in my_words.values(): # then count how many words we have of each language already
		if entry['partos'] not in ['noun','verb','loanword'] or re.match(r'^ono ', entry['source']): # only count grammar words and onomotopoeias
			if re.match(r'^[a-z][a-z][a-z] <.*> \[.*\]', entry['source']):
				tallies[entry['source'].split()[0]] += 1
			if entry['otp'] and not entry['partos'].startswith('compound'):
				all_otp_words.add(entry['otp'].replace('y','i').replace('w','u'))
	logging.info(tallies)
				
	for entry in my_words.values():
		if ' OF ' in entry['source']: # derive their derivatives
			d_type, d_gloss = entry['source'].split(' OF ')
			assert my_words[d_gloss]['otp'], entry['source']
			entry['otp'] = derive(my_words[d_gloss]['otp'], d_type, my_words, 'ANTONYM' in my_words[d_gloss]['derivatives'])
			all_otp_words.add(entry['otp'].replace('y','i').replace('w','u'))

		elif entry['partos'] in ['noun','verb'] and entry['otp'] == '': # make up words for any noun or verb that needs it
			eng = choose_key(entry)
			lang, source_orth, source_ipa, my_word = choose_word(eng, real_words, tallies,
				partos=entry['partos'], has_antonym=has_antonym(entry), all_words=all_otp_words)
			entry['otp'] = my_word
			entry['source'] = "{} <{}> [{}]".format(lang, source_orth, source_ipa)
			tallies[lang] += 1
			all_otp_words.add(my_word.replace('y','i').replace('w','u')) # skip the i/j distinction behind the curtain

		elif entry['partos'].startswith('compound'): # and then compound the compound words
			if entry['source']:
				for component in entry['source'].split():
					key = dehyphenated(component)
					if key in my_words and my_words[key]['otp'] != '':
						entry['otp'] += my_words[key]['otp']
					else:
						raise ValueError("No '{}' for {}'s {}".format(component, entry['eng'][0], entry['source'].split()))
			else:
				logging.error("{} has no components".format(entry['eng'][0]))


def analyse_dictionary(all_words):
	""" count up the number of words with each root """
	tallies = collections.Counter()
	for word in all_words.values():
		if '[' in word['source'] and word['partos'] != 'loanword':
			tallies[word['source'][:3]] += 1
	actual_fracs = [(lang, tallies[lang]/sum(tallies.values())) for lang in tallies.keys()]
	for lang, frac in sorted(actual_fracs, key=lambda t:-t[1]):
		logging.info("{}:{:.3f} ({:2d})".format(lang, frac, tallies[lang]))
	logging.info("{} roots, {} of which are of European origin".format(
		sum(tallies.values()), tallies['eng']+tallies['spa']+tallies['epo']))


def save_dictionary(dictionary, directory):
	""" save the updated values of all these nouns and verbs and compounds """
	for partos in ['verb', 'noun', 'compound word']:
		with open(path.join(directory, partos+'.csv'), 'r', encoding='utf-8') as f:
			rows = pd.read_csv(f, dtype=str, na_filter=False)

		for row_index, row in rows.iterrows():
			for entry in dictionary.values(): # look for the entry
				if entry['partos'][:4] == partos[:4] and entry['Index'] == row_index: # that matches this file and row
					row['source'] = entry['source'] # and overwrite the latter two columns
					row['otp'] = entry['otp']
					break

		with open(path.join(directory, partos+'.csv'), 'w', encoding='utf-8', newline='\n') as f:
			rows.to_csv(f, index=False)


def format_dictionary(dictionary, directory):
	""" make a bunch of nicely-formatterd dictionaries in Markdown and LaTeX """
	partos_abbrv = {'noun':'n', 'loanword':'n', 'verb':'v', 'proverb':'v', 'pronoun':'pn',
		'numeral':'num', 'postposition':'post', 'sentence particle':'ptcl', 'specifier':'spec'}
	for lang3 in SUPPORTED_LANGUAGES:
		lang2 = THREECODE_TO_TWOCODE[lang3]
		markdown = ""
		latex = ""

		previous_initial = ''
		for entry in sorted(dictionary.values(), key=lambda e: otp_ord(e['otp'])):
			initial = entry['otp'].replace("'",'')[0]
			if initial != previous_initial:
				markdown += "### {}\n\n".format(initial)
				latex += "\\subsection{{{}}}\n\n".format(initial)
				previous_initial = initial

			while 'compound ' in entry['partos']:
				entry['partos'] = entry['partos'][9:]
			entry['pos'] = partos_abbrv[entry['partos']]

			if '[' in entry['source']:
				lang = entry['source'][:3]
				rest = entry['source'][3:].replace('<','⟨').replace('>','⟩').replace('[','\\[').replace(']','\\]')
				if lang == 'ono':
					entry['source_str'] = "{}.{}".format(lang, rest)
				else:
					entry['source_str'] = "{}.{}".format(lang.capitalize(), rest)
			elif ' OF ' in entry['source']:
				base_word = dictionary[entry['source'].split(' OF ')[1]]['otp']
				base_invs = get_antonym(base_word)
				full_word = entry['otp'].replace(' ','')
				if full_word == base_invs:
					entry['source_str'] = "[~~{0}~~](#{0})".format(base_word)
				elif full_word.startswith(base_word) or full_word.startswith(base_invs):
					i = len(base_word)
					entry['source_str'] = "[{0}](#{0})+[{1}](#{1})".format(full_word[:i], full_word[i:])
				elif full_word.endswith(base_word) or full_word.endswith(base_invs):
					i = -len(base_word)
					entry['source_str'] = "[{0}](#{0})+[{1}](#{1})".format(full_word[:i], full_word[i:])
				elif base_word in full_word:
					i = full_word.index(base_word)
					j = i + len(base_word)
					entry['source_str'] = "[{0}](#{0})+[{1}](#{1})+[{2}](#{2})".format(full_word[:i], full_word[i:j], full_word[j:])
				else:
					raise Exception("How is {} related to {}?".format(full_word, base_word))
			elif entry['source']:
				otp_parts = []
				for part in entry['source'].split(' '):
					otp_parts.append(dictionary[dehyphenated(part)]['otp'])
				entry['source_str'] = "+".join("[{0}](#{0})".format(part) for part in otp_parts)
			else:
				entry['source_str'] = "∅"

			entry['definitions'] = '; '.join(entry[lang3])
			for arg, code, suffix in [('SBJ',"ʟєꜱ","les"), ('OBJ',"ʟᴏᴧ","lon"), ('IND',"ʟᴜᴍ","lum")]: # for these arguments
				if arg in entry['derivatives']: # try linking to the derivative
					entry['definitions'] = entry['definitions'].replace(arg, "[{}](#{})".format(code, entry['otp']+suffix))
				else:
					entry['definitions'] = entry['definitions'].replace(arg, code)

			markdown += MARKDOWN_ENTRY.format(**entry)

			entry['source_str_tex'] = latexify(entry['source_str'])
			entry['definitions_tex'] = latexify(entry['definitions'])
			latex += LATEX_ENTRY.format(**entry)		

		with open(path.join(directory, '{}-dict.md'.format(lang2)), 'w', encoding='utf-8') as f:
			f.write(markdown)
		with open(path.join(directory, '{}-dict.tex'.format(lang2)), 'w', encoding='utf-8') as f:
			f.write(latex)


def measure_corpus(directory):
	""" count the occurences of all words in this corpus """
	return collections.Counter()



if __name__ == '__main__':
	source_dictionaries = compile_dictionaries('../data')
	all_words = load_dictionary('words')
	fill_blanks(all_words, source_dictionaries)
	verify_words(all_words)
	logging.info(json.dumps(all_words, indent=2))
	analyse_dictionary(all_words)
	save_dictionary(all_words, 'words')
	format_dictionary(all_words, '../Dictionaries')
	hist = measure_corpus('../Example Texts')
	for word, count in hist.most_common(36):
		logging.info("{:03}\t{}".format(count, word))

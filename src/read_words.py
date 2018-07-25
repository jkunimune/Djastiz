# read_words.py

import csv
from dragonmapper import hanzi
import epitran
from os import path
import pickle
import re
import sys

sys.path.append(path.sep.join([*sys.path[0].split(path.sep)[0:-2], 'English-to-IPA']))
import eng_to_ipa # available at https://github.com/mphilli/English-to-IPA.git


['zh-CN', 'es', 'eo', 'en', 'hi', 'bn', 'ar', 'pa', 'yo', 'mr', 'ig', 'sw', 'zu', 'ny', 'xh', 'sn', 'st']
EPITRANSLATORS = {lang:epitran.Epitran(script) for lang, script in
	[('hi','hin-Deva'), ('bn','ben-Beng'), ('ar','ara-Arab'), ('pa','pan-Guru'), ('yo','yor-Latn'), ('mr','mar-Deva'),
	('sw','swa-Latn'), ('zu','zul-Latn'), ('ny','nya-Latn'), ('xh','xho-Latn'), ('sn','sna-Latn')]}


def read_mandarin(word):
	""" read a word phonetically in Hanzi (Mandarin pronunciations) """
	try:
		broad = hanzi.to_ipa(word).replace('ɪ','ɪ̯').replace('ʊ','ʊ̯').replace(' ','') # well, that was easy
	except ValueError:
		broad = '*'
	return broad, broad


def read_spanish(word):
	""" read a word phonetically in Spanish """
	word = word.lower()
	if word.startswith('me ') or word.startswith('de '):
		word = word[3:]

	broad = ''
	stress_i = None
	for i, c in enumerate(word):
		if c == 'á':
			stress_i = len(broad)
			broad += 'a'
		elif c == 'c':
			if i+1 < len(word) and word[i+1] == 'h':
				broad += 'tʃ'
			elif i+1 < len(word) and word[i+1] in 'eiéí':
				broad += 's'
			else:
				broad += 'k'
		elif c == 'é':
			stress_i = len(broad)
			broad += 'e'
		elif c == 'g':
			if i+1 < len(word) and word[i+1] in 'eiéí':
				broad += 'x'
			else:
				broad += 'ɡ'
		elif c == 'h':
			pass
		elif c == 'i':
			if (i+1 < len(word) and word[i+1] in 'aeouáéíóú') or (i-1 >= 0 and word[i-1] in 'aeoáéíóú'):
				broad += 'j'
			else:
				broad += 'i'
		elif c == 'í':
			stress_i = len(broad)
			broad += 'i'
		elif c == 'j':
			broad += 'x'
		elif c == 'l':
			if i+1 < len(word) and word[i+1] == 'l':
				broad += 'ʝ'
			elif i-1 >= 0 and word[i-1] == 'l':
				pass
			else:
				broad += 'l'
		elif c == 'ñ':
			broad += 'ɲ'
		elif c == 'ó':
			stress_i = len(broad)
			broad += 'o'
		elif c == 'q':
			broad += 'k'
		elif c == 'r':
			if (i-1 < 0 or word[i-1] in 'rmn ') or i == len(word)-1:
				broad += 'r'
			elif i+1 < len(word) and word[i+1] == 'r':
				pass
			else:
				broad += 'ɾ'
		elif c == 'u':
			if i-1 >= 0 and word[i-1] == 'q':
				pass
			elif i-1 >= 0 and word[i-1] == 'g' and i+1 < len(word) and word[i+1] in 'eiéí':
				pass
			elif (i+1 < len(word) and word[i+1] in 'aeoáéíó') or (i-1 >= 0 and word[i-1] in 'aeoiáéíó'):
				broad += 'w'
			else:
				broad += 'u'
		elif c == 'ú':
			stress_i = len(broad)
			broad += 'u'
		elif c == 'ü':
			broad += 'w'
		elif c == 'v':
			broad += 'b'
		elif c == 'x':
			broad += 'ks'
		elif c == 'y':
			if i+1 < len(word) and word[i+1] in 'aoeuáóéíú':
				broad += 'ʝ'
			elif i-1 >= 0 and word[i-1] in 'aoeáóéíú':
				broad += 'j'
			else:
				broad += 'i'
		elif c == 'z':
			broad += 's'
		else:
			broad += c
	if stress_i is None:
		vowels = [i for i,c in enumerate(broad) if c in 'aoeui']
		if len(vowels) > 1:
			stress_i = vowels[-2] if (broad[-1] in 'aoeuins') else vowels[-1]
	if stress_i is not None:
		while broad[stress_i-1] in 'jw':
			stress_i -= 1
		stress_j = stress_i-1
		while stress_j >= 0 and broad[stress_j] not in 'aeiou ':
			stress_j -= 1
		if stress_j < 0:
			broad = 'ˈ' + broad
		else:
			broad = broad[:(stress_j+stress_i+1)//2] + 'ˈ' + broad[(stress_j+stress_i+1)//2:]

	narrow = ''
	for i, c in enumerate(broad):
		last_char = broad[i-1] if i-1 >= 0 else None
		if last_char == 'ˈ':
			last_char = broad[i-2] if i-2 >= 0 else None
		if c == 'b':
			if (last_char and last_char not in 'mnŋ ') or i+1 >= len(broad):
				narrow += 'β'
			else:
				narrow += 'b'
		elif c == 'd':
			if (last_char and last_char not in 'mnŋ l') or i+1 >= len(broad):
				narrow += 'ð'
			else:
				narrow += 'd'
		elif c == 'ɡ':
			if (last_char and last_char not in 'mnŋ ') or i+1 >= len(broad):
				narrow += 'ɣ'
			else:
				narrow += 'ɡ'
		elif c == 'ʝ':
			if (last_char and last_char not in 'mnŋ ') or i+1 >= len(broad):
				narrow += 'ʝ'
			else:
				narrow += 'ɟʝ'
		elif c == 'n':
			if i+1 < len(broad) and broad[i+1] in 'kɡx':
				narrow += 'ŋ'
			else:
				narrow += 'n'
		else:
			narrow += c

	if broad.endswith('ar') or broad.endswith('er') or broad.endswith('ir'):
		broad = broad[:-1] + 's' # put all verbs in singular second person present, to better fit the morphological rules
	return broad, narrow


def read_esperanto(word):
	""" read a word phonetically in Esperanto """
	word = word.lower()
	if word.endswith('i') or word.endswith('u'):
		word = word[:-1] + 'as' # put all verbs in present

	broad = word.replace(
		'c', 'ts').replace('ĉ', 'tʃ').replace('ĝ', 'dʒ').replace('ĥ', 'x').replace(
		'ĵ', 'ʒ').replace('ŝ', 'ʃ').replace('ŭ', 'w').replace('g', 'ɡ')
	vowels = [i for i,c in enumerate(broad) if c in 'aeiou']
	if len(vowels) > 1:
		stress_i = vowels[-2]
		stress_j = stress_i-1 # locating the stress marker is by far the hardest part
		while stress_j >= 0 and broad[stress_j] not in 'aoeui': # as you may have guessed, I have my qualms with Esperanto. The orthography, though,
			stress_j -= 1 # is by far the best thing about it, and it boggles the mind that Idoists would ever try to change that.
		if stress_j < 0:
			broad = 'ˈ' + broad
		else:
			broad = broad[:(stress_j+stress_i+1)//2] + 'ˈ' + broad[(stress_j+stress_i+1)//2:]
	return broad, broad


def read_english(word):
	""" read a word phonetically in English """
	broad = eng_to_ipa.convert(word.replace('-',' ')).replace('ʧ','tʃ').replace('ʤ','dʒ').replace('r','ɹ')\
		.replace('e','eɪ̯').replace('oʊ','oʊ̯').replace('aɪ','ɑɪ̯').replace('ɔɪ','ɔɪ̯').replace('aʊ','aʊ̯')

	if '*' in broad: # if it couldn't find it,
		return '*', '*' # cry

	narrow = ''
	for i, c in enumerate(broad): # there aren't actually too many allohponies in English of which I could think
		if c in 'td' and i-1 >= 0 and broad[i-1] in 'aeiouəɪʊɔɑɛæɹj̯' and i+1 < len(broad) and broad[i+1] in 'aeiouəɪʊɔɑɛæɹj̯':
			narrow += 'ɾ'
		elif c in 'ptk' and (i == 0 or broad[i-1] == 'ˈ'):
			narrow += c+'ʰ'
		elif c == 'ɹ' and i+1 < len(broad) and broad[i+1] in 'aeiouəɪʊɔɑɛæ':
			narrow += c+'ʷ'
		elif c in 'ɑiuɔ' and (i+1 >= len(broad) or broad[i+1] not in 'ɪʊ'):
			narrow += c+'ː'
		elif c == 'ɑ' and i+3 < len(broad) and broad[i+1:i+3] == 'ɪ̯' and broad[i+3] in 'ptkfθsʃh':
			narrow += 'ə'
		else:
			narrow += c
	return broad, narrow


def read_igbo(word):
	return '*', '*'

def read_sotho(word):
	return '*', '*'


def read(word, lang):
	""" Convert a word in a language to IPA """
	if lang == 'zh-CN':
		return read_mandarin(word)
	elif lang == 'es':
		return read_spanish(word)
	elif lang == 'eo':
		return read_esperanto(word)
	elif lang == 'en':
		return read_english(word)
	elif lang == 'ig':
		return read_igbo(word)
	elif lang == 'st':
		return read_sotho(word)
	else:
		return (EPITRANSLATORS[lang].transliterate(word),)*2


if __name__ == '__main__':
	try:
		all_transcriptions = pickle.load(open('../data/all_languages.p','rb'))
	except IOError:
		all_transcriptions = {}
	for lang in ['zh-CN', 'es', 'eo', 'en', 'hi', 'bn', 'ar', 'pa', 'yo', 'mr', 'ig', 'sw', 'zu', 'ny', 'xh', 'sn', 'st']:
		with open('../data/dict_{}.csv'.format(lang), 'r', encoding='utf-8', newline='') as f:
			for word, orthography in csv.reader(f):
				if lang != 'en' and word == orthography:
					broad, narrow = '*', '*' # if it's exactly the same in English and the other language, then Google Translate is selling us lies
				else:
					broad, narrow = read(orthography, lang)
				all_transcriptions[word] = {**all_transcriptions.get(word,{}), lang:(orthography, broad, narrow)}
				print("{} in {} is spelled {} and pronounced /{}/ [{}]".format(word, lang, *all_transcriptions[word][lang]))
	pickle.dump(all_transcriptions, open('../data/all_languages.p','wb'))

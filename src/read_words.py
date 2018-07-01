# read_words.py

import csv
import re


def read_mandarin(word):
	""" read a word phonetically in Esperanto """
	return '', ''


def read_spanish(word):
	""" read a word phonetically in Esperanto """
	word = word.lower()
	if word.startswith('me ') or word.startswith('de '):
		word = word[3:]

	broad = ''
	stress_i = None
	for i, c in enumerate(word):
		if c == 'á':
			broad += 'a'
			stress_i = i
		elif c == 'c':
			if i+1 < len(word) and word[i+1] == 'h':
				broad += 'tʃ'
			if i+1 < len(word) and word[i+1] in 'ei':
				broad += 's'
			else:
				broad += 'k'
		elif c == 'é':
			broad += 'e'
			stress_i = i
		elif c == 'g':
			if i+1 < len(word) and word[i+1] in 'ei':
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
			broad += 'i'
			stress_i = i
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
			broad += 'o'
			stress_i = i
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
			if i-1 >= 0 and word[i-1] in 'gq':
				pass
			elif (i+1 < len(word) and word[i+1] in 'aeoáéíóú') or (i-1 >= 0 and word[i-1] in 'eoiáéíóú'):
				broad += 'w'
			else:
				broad += 'u'
		elif c == 'ú':
			broad += 'u'
			stress_i = i
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
		stress_j = stress_i-1 # locating the stress marker is by far the hardest part
		while stress_j >= 0 and broad[stress_j] not in 'aeiou': # as you may have guessed, I have my qualms with Esperanto. The orthography, though,
			stress_j -= 1 # is by far the best thing about it, and it boggles the mind that Idists would ever try to change that.
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
	""" read a word phonetically in Esperanto """
	return '', ''


def read_hindustani(word):
	""" read a word phonetically in Esperanto """
	return '', ''


def read_bengali(word):
	""" read a word phonetically in Esperanto """
	return '', ''


def read_arabic(word):
	return '', ''


def read_punjabi(word):
	return '', ''


def read_yoruba(word):
	return '', ''


def read_marathi(word):
	return '', ''


def read_igbo(word):
	return '', ''


def read_swahili(word):
	return '', ''


def read_zulu(word):
	return '', ''


def read_chichewa(word):
	return '', ''


def read_xhosa(word):
	return '', ''


def read_shona(word):
	return '', ''


def read_sotho(word):
	return '', ''


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
	elif lang == 'hi':
		return read_hindustani(word)
	elif lang == 'bn':
		return read_bengali(word)
	elif lang == 'ar':
		return read_arabic(word)
	elif lang == 'pa':
		return read_punjabi(word)
	elif lang == 'yo':
		return read_yoruba(word)
	elif lang == 'mr':
		return read_marathi(word)
	elif lang == 'ig':
		return read_igbo(word)
	elif lang == 'sw':
		return read_swahili(word)
	elif lang == 'zu':
		return read_zulu(word)
	elif lang == 'ny':
		return read_chichewa(word)
	elif lang == 'xh':
		return read_xhosa(word)
	elif lang == 'sn':
		return read_shona(word)
	elif lang == 'st':
		return read_sotho(word)
	else:
		raise ValueError("Unrecognised language code: '{}'".format(lang))


if __name__ == '__main__':
	all_transcriptions = {}
	for lang in ['zh-CN', 'es', 'eo', 'en', 'hi', 'bn', 'ar', 'pa', 'yo', 'mr', 'ig', 'sw', 'zu', 'ny', 'xh', 'sn', 'st']:
		with open('../data/dict_{}.csv'.format(lang), 'r', encoding='utf-8', newline='') as f:
			for eng, other in csv.reader(f):
				broad, narrow = read(other, lang)
				all_transcriptions[eng] = all_transcriptions.get(eng, []) + [(broad, narrow)]
	print(all_transcriptions)

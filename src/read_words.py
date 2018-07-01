# read_words.py

import csv
import re


def read_mandarin(word):
	""" read a word phonetically in Esperanto """
	return '', ''


def read_spanish(word):
	""" read a word phonetically in Esperanto """
	return '', ''


def read_esperanto(word):
	""" read a word phonetically in Esperanto """
	if word.endswith('i') or word.endswith('u'):
		word = word[:-1] + 'as' # put all verbs in present

	broad = word.replace(
		'c', 'ts').replace('ĉ', 'tʃ').replace('ĝ', 'dʒ').replace('ĥ', 'x').replace(
		'ĵ', 'ʒ').replace('ŝ', 'ʃ').replace('ŭ', 'w')
	stress_i = [i for i,c in enumerate(broad) if c in 'aeiou'][-2]
	stress_j = stress_i-1 # locating the stress marker is by far the hardest part
	while word[stress_j] not in 'aeiou': # as you may have guessed, I have my qualms with Esperanto. The orthography, though,
		stress_j -= 1 # is by far the best thing about it, and it boggles the mind that Idists would ever try to change that.
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

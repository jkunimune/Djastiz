# load_words.py
# collect translations of all the words in the word lists into all the requisite languages

import csv
import os
import pandas as pd
import re
import six

from google.cloud import translate


LANGUAGES = ['zh-CN', 'es', 'eo', 'en', 'hi', 'bn', 'ar', 'pa', 'jv', 'yo', 'mr', 'ms', 'ig', 'tl', 'sw', 'zu', 'ny', 'xh', 'sn', 'st']

DISCARD_UNUSED = False


def translate_text(source, target, text, translate_client):
	"""Translates text into the target language.

	Target must be an ISO 639-1 language code.
	See https://g.co/cloud/translate/v2/translate-reference#supported_languages
	"""
	if target == source:
		return text

	if isinstance(text, six.binary_type):
		text = text.decode('utf-8')

	result = translate_client.translate(text, source_language=source, target_language=target)

	return result['translatedText']


def load_dictionaries(filepath):
	dictionaries = {}
	for lang_code in LANGUAGES:
		print("Loading the {} dictionary...".format(lang_code))
		dictionaries[lang_code] = {}
		if os.path.isfile(filepath.format(lang_code)):
			with open(filepath.format(lang_code), 'r', encoding='utf-8', newline='') as f:
				for row in csv.reader(f):
					dictionaries[lang_code][row[0]] = row[1:]
	return dictionaries


def save_dictionaries(dictionaries, filepath):
	for lang_code, dictionary in dictionaries.items():
		with open(filepath.format(lang_code), 'w', encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			for english, row in sorted(dictionary.items()):
				writer.writerow([english, *row])


def get_key(entry, pos):
	if '*' in entry.eng:
		return 'en', re.search(r'\*(\w+)\b', entry.eng).group(1)
	elif '*' in entry.spa:
		return 'es', re.search(r'\*(\w+)\b', entry.spa).group(1)
	else:
		key = re.search(r'^([^;\{]+)( \{|;|$)', entry.eng).group(1)
		if len(key.split()) > 1 and key.split()[0] in ['be', 'beI', 'find', 'have', 'give', 'do', 'get', 'can']:
			key = ' '.join(key.split()[1:]) # drop the "be"
		elif pos == 'verb':
			key = 'to '+key
		return 'en', key



if __name__ == '__main__':
	translate_client = translate.Client()

	num_roots = 0
	saved_dictionaries = load_dictionaries('../data/dict_{}.csv')
	if DISCARD_UNUSED:
		new_dictionaries = {code:{} for code in LANGUAGES}
	else:
		new_dictionaries = saved_dictionaries
	
	print("Let us begin...")
	for filename in ['verb.csv', 'noun.csv']:
		with open('./words/{}'.format(filename), 'r', encoding='utf-8', newline='') as f:
			word_set = pd.read_csv(f, dtype=str, na_filter=False)
		for row in word_set.itertuples():
			english, source = row.eng, row.source

			if not source or (len(source.split()[0]) == 3 and source.split()[0] != 'ono'):
				source_lang_code, key = get_key(row, pos=filename.split('.')[0])
				print('Translating "{}" to {} languages...'.format(key, len(LANGUAGES)))
				any_update = False
				for lang_code in LANGUAGES:
					if key in saved_dictionaries[lang_code]:
						new_dictionaries[lang_code][key] = saved_dictionaries[lang_code][key]
					else:
						new_dictionaries[lang_code][key] = [translate_text(source_lang_code, lang_code, key, translate_client)]
						print("\t{}: {}".format(lang_code[:2], new_dictionaries[lang_code][key][0]))
						any_update = True

				if any_update:
					save_dictionaries(new_dictionaries, '../data/dict_{}.csv')
				num_roots += 1
		if DISCARD_UNUSED:
			save_dictionaries(new_dictionaries, '../data/dict_{}.csv')

	print("{} noun and verb roots".format(num_roots))

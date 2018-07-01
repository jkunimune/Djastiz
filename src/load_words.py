# load_words.py
# collect translations of all the words in the word lists into all the requisite languages

import csv
import os
import six

from google.cloud import translate


LANGUAGES = ['zh-CN', 'es', 'eo', 'en', 'hi', 'bn', 'ar', 'pa', 'yo', 'mr', 'ig', 'sw', 'zu', 'ny', 'xh', 'sn', 'st']


def translate_text(target, text, translate_client, source='en'):
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
				for english, other_language in csv.reader(f):
					dictionaries[lang_code][english] = other_language
	return dictionaries


def save_dictionaries(dictionaries, filepath):
	for lang_code, dictionary in dictionaries.items():
		with open(filepath.format(lang_code), 'w', encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			for english, other_language in sorted(dictionary.items()):
				writer.writerow([english, other_language])


if __name__ == '__main__':
	translate_client = translate.Client()

	num_roots = 0
	dictionaries = load_dictionaries('../data/dict_{}.csv')
	
	print("Let us begin...")
	for filename in ['verb.csv', 'noun.csv']:
		with open('./words/{}'.format(filename), 'r', encoding='utf-8', newline='') as f:
			for english, chatisun, source in csv.reader(f):
				if not source or (len(source.split()[0]) == 3 and source.split()[0] != 'ono'):
					key = english.split(';')[0]
					if len(key.split()) > 1 and key.split()[0] in ['be', 'find', 'have', 'give', 'do', 'get']:
						key = ' '.join(key.split()[1:]) #drop the "be"
					print('Translating "{}" to {} languages...'.format(key, len(LANGUAGES)))
					any_update = False
					for lang_code in LANGUAGES:
						if key not in dictionaries[lang_code]:
							dictionaries[lang_code][key] = translate_text(lang_code, key, translate_client)
							print("\t{}: {}".format(lang_code[:2], dictionaries[lang_code][key]))
							any_update = True

					if any_update:
						save_dictionaries(dictionaries, '../data/dict_{}.csv')
					num_roots += 1

	print("{} noun and verb roots".format(num_roots))

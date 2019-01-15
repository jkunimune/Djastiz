# compile_words.py

import pickle
import csv


LANG_CODES = {
	'zh-CN':'cmn', 'es':'spa', 'eo':'epo', 'en':'eng', 'hi':'hin', 'bn':'ben', 'ar':'ara', 'pa':'pan',
	'jv':'jav', 'yo':'yor', 'mr':'mar', 'ms':'msa', 'ig':'ibo', 'tl':'fil', 'sw':'swa', 'zu':'zul',
	'ny':'nya', 'xh':'xho', 'sn':'sho', 'st':'sot'}


if __name__ == '__main__':
	try:
		with open('../data/all_languages.pkl','rb') as f:
			all_transcriptions = pickle.load(f)
	except IOError:
		all_transcriptions = {}
	for lang in LANG_CODES:
		with open('../data/dict_{}.csv'.format(lang), 'r', encoding='utf-8', newline='') as f:
			for word, orthography, broad, narrow in csv.reader(f):
				if word not in all_transcriptions:	all_transcriptions[word] = {}
				all_transcriptions[word][LANG_CODES[lang]] = (orthography, broad, narrow)
	with open('../data/all_languages.pkl','wb') as f:
		pickle.dump(all_transcriptions, f)

# load_words.py
# collect translations of all the words in the word lists into all the requisite languages

import csv
import os


LANGUAGES = ['cmn', 'spa', 'epo', 'eng', 'hin', 'ben', 'ara', 'pan', 'yor', 'mar', 'igb', 'swa', 'zul', 'chi']


for filename in os.listdir('words'):
	print(filename)
	with open('./words/{}'.format(filename), 'r', encoding='utf-8') as f:
		for english, chatisun, source in csv.reader(f):
			print(english)

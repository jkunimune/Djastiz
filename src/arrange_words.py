#translator.py

import collections
import csv
import matplotlib.pyplot as plt
import os
from os import path
import pickle



def load_dictionary(directory):
	""" load words from the given directory into a big dictionary thing """
	header = None
	words = {} # each key is an English gloss key; value is {definition, my word, derivatives}
	for filename in os.listdir(directory):
		with open(path.join(directory, filename), 'r', encoding='utf-8') as f:
			for row in csv.reader(f):
				if header is None:
					header = row
				else:
					assert len(row) == len(header), row
					row = {head:row[i] for i, head in enumerate(header)}
					print("{}: {}".format(row['eng'].split(';')[0], row['source']))
	return {}


def fill_blanks(my_words, real_words):
	""" come up with words from the source dictioraries for all nouns and verbs that aren't
		onomotopoeias, and update the compound words accordingly """
	pass


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
	save_dictionary(all_words, 'words')
	format_dictionary(all_words, '../Dictionaries')
	hist = measure_corpus('../Example Texts')
	for word, count in hist.most_common(36):
		print("{:03}\t{}".format(count, word))

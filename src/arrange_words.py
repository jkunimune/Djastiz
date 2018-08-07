#translator.py

import collections
import csv
import matplotlib.pyplot as plt
import os
from os import path
import pickle
import re



def get_curly_brace_pair(string):
	""" return the indices of a matching pair of {} in string """
	assert '{' in string and '}' in string, "There are no curly braces in {}".format(string)
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


def load_dictionary(directory):
	""" load words from the given directory into a big dictionary thing """
	header = None
	words = {} # each key is an English gloss key; value is {definition, my word, derivatives}
	for filename in os.listdir(directory):
		with open(path.join(directory, filename), 'r', encoding='utf-8') as f:
			for row in csv.reader(f):
				if header is None:
					header = row # the header is actually useful for once
					continue
				else:
					assert len(row) == len(header), row
					entry = {head:row[i] for i, head in enumerate(header)} # convert row to a dict
					entry['derivatives'] = {} # don't forget to start counting these

				for key, value in entry.items():
					if '*' in value:
						assert not entry['source'], "Why is there a * and a source cited for {}".format(entry)
						starred = value[value.index('*')+1:]
						starred = starred[:re.search(r'\b', starred).start()] # look for explicit source word selections
						entry['source'] = starred
						entry[key] = value.replace('*','')

				for key, value in entry.items():
					while '{' in value: # handle explicit derivatives
						i, j = get_curly_brace_pair(value)
						print("What do I do with ({})?".format(value[i+1:j])) # TODO
						value = (value[:i-1] + value[j+1:]).strip()
						entry[key] = value

				for key in entry:
					if key not in ['source', 'ltl', 'derivatives']:
						entry[key] = entry[key].split('; ') # separate definitions when applicable

				for i, eng_meaning in enumerate(entry['eng']):
					if eng_meaning.startswith('beI '):
						entry['eng'][i] = eng_meaning.replace('beI ', 'be ') # TODO: create derivatives from this
					elif eng_meaning.startswith('be '):
						pass # TODO

				if ' OF ' in entry['source']:
					i = entry['source'].index(' OF ')
					deriv_type, deriv_word = entry['source'][:i], entry['source'][i+4:]
					assert deriv_word in words, '{} of "{}" declared before "{}"'.format(deriv_type, deriv_word, deriv_word)
					words[deriv_word]['derivatives'][deriv_type] = entry

				for possible_gloss in entry['eng']:
					if possible_gloss not in words:
						words[possible_gloss] = entry
						break

	import json
	print(json.dumps(words, indent=2))
	return words


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

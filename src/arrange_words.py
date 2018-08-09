#translator.py

import collections
import csv
import matplotlib.pyplot as plt
import os
from os import path
import pandas as pd
import pickle
import re



def get_curly_brace_pair(string):
	""" return the indices of a matching pair of {} in string """
	assert '{' in string and '}' in string, "There aren't enough curly braces in {}".format(string)
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
	words = {} # each key is an English gloss key; value is {definition, my word, derivatives}
	for filename in os.listdir(directory):
		with open(path.join(directory, filename), 'r', encoding='utf-8') as f:
			word_set = pd.read_csv(f, dtype=str, na_filter=False)

		queue = collections.deque(word_set.itertuples(index=False))
		while queue:
			entry = queue.popleft()
			print(entry)
			try:
				entry['derivatives'] = {} # don't forget to start counting these
			except TypeError:
				entry = entry._asdict() # convert row to a dict
				entry['derivatives'] = {}

			for key, value in entry.items():
				if '*' in value:
					assert not entry['source'], "Why is there a * and a source cited for {}".format(entry)
					starred = value[value.index('*')+1:]
					starred = starred[:re.search(r'\b', starred).start()] # look for explicit source word selections
					entry['source'] = '*'+starred
					entry[key] = value.replace('*','')
					break

			unprocessed_derivatives = collections.defaultdict(lambda: {key:'' for key in entry}) # start looking for noun derivatives that need to be processed later

			for key, value in entry.items():
				while '{' in value: # handle explicit derivatives
					i, j = get_curly_brace_pair(value)
					for deriv_statement in value[i+1:j].split('|'):
						if re.match(r'^[A-Z]+:', deriv_statement):
							k = deriv_statement.index(':')
							unprocessed_derivatives[deriv_statement[:k]][key] = deriv_statement[k+1:]
						else:
							assert value[i-4:i-1] in ['SBJ','OBJ','IND']
							unprocessed_derivatives[value[i-4:i-1]][key] = deriv_statement
					value = (value[:i-1] + value[j+1:]).strip()
					entry[key] = value

			for key in entry:
				if key not in ['source', 'ltl', 'derivatives']:
					entry[key] = entry[key].split('; ') # separate definitions when applicable
					while not entry[key][0]:
						entry[key].pop(0) # ignore any empty things

			for i, eng_meaning in enumerate(entry['eng']):
				if eng_meaning.startswith('beI '): # handle implicit derivatives
					entry['eng'][i] = eng_meaning.replace('beI ', 'be ') # TODO: create derivatives from this
					unprocessed_derivatives['IND']['eng'] += '; '+eng_meaning[3:]
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
			if words[possible_gloss] != entry:
				gloss = '{}{:03d}'.format(entry['eng'][0], len(words))
				print("Warning: There is no possible gloss for {}. '{}' will be used as a key.".format(entry, gloss))
				words[gloss] = entry

			for deriv_type, deriv_dict in unprocessed_derivatives.items():
				deriv_dict['source'] = '{} OF {}'.format(deriv_type, possible_gloss)
				queue.append(deriv_dict) # finally, put the unprocessed derivatives in the queue

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

# word generator
import copy
import os
import random


CONSONANTS = [{'m','l',''},{'p','j','r'}]
VOWELS = {'a','e','u','o'}
TONES = [u'\u030F', u'\u0300', u'\u0304', u"\u0301", u'\u030B']

def random_choice(s):
	"""because random_choice doesn't work for sets"""
	return random.choice(tuple(s))


def similar(a, b):
	"""return True if a and b might sound too similar"""
	if len(a) == len(b)+1:
		for i in range(len(a)):
			for tone in TONES:
				if b[:i] + tone + b[i:] == a:
					return True
		return False
	elif len(b) == len(a)+1:
		return similar(b, a)
	else:
		return a == b


def length(word):
	"""the number of Djastiz letters in the word"""
	return len(word.replace('`','').replace("'","").replace('-','').replace('"',''))


def random_consonant(ending=False):
	"""choose a consonant to go here"""
	if ending:
		return random_choice(CONSONANTS[0])
	else:
		return random_choice(CONSONANTS[0]|CONSONANTS[1])


def random_tone(tonic=False):
	if tonic:
		return random.choice([TONES[0], TONES[-1]])
	elif random.random() < .2:
		return ''
	else:
		return random.choice(TONES[1:-1])


def new_tense_marker():
	"""create a new monosyllabic tonic word"""
	return random_consonant() + random_choice(VOWELS) + TONES[0]


def new_particle():
	"""create a new monosyllabic non-tonic word"""
	word = ''
	if random.random() < .5:
		word += random_consonant()
	word += random_choice(VOWELS) + random_tone()
	if random.random() < .5:
		word += random_consonant(ending=True)
	return word


def new_verb():
	"""create a new polysyllabic pseudo-tonic word"""
	word = ''
	num_syl = int(random.random()**2*2.5+1)
	for i in range(num_syl-1):
		word += random_consonant() + random_choice(VOWELS) + random_tone(tonic=random.random()<.3)
	word += random_consonant() + random_choice(VOWELS) + random_tone(tonic=True) + random_consonant(ending=True)
	return word


def new_noun():
	"""create a new polysyllabic non-tonic word"""
	word = ''
	num_syl = int(random.random()**2*2.5+1)
	for i in range(num_syl-1):
		word += random_consonant() + random_choice(VOWELS) + random_tone()
	word += random_consonant() + random_choice(VOWELS) + random_tone(tonic=False) + random_consonant(ending=True)
	return word


def load_all_words(directory, max_size=0):
	"""return a list of all the words in this directory"""
	words = []
	for filename in os.listdir(directory):
		if 'cache' not in filename:
			with open(directory+'\\'+filename, 'r', encoding='utf-8') as f:
				lines = f.readlines()
				if max_size == 0 or len(lines) < max_size:
					for line in lines:
						if len(line) > 1:
							try:
								djastiz_word = line[line.rindex(',')+1:].strip()
							except ValueError:
								djastiz_word = line.strip()
							if djastiz_word:
								words.append(djastiz_word)
							if words[-1] == '':
								print("! {}".format(filename))
	return words


def check_words(directory):
	"""verify that no two words are too similar"""
	words = load_all_words(directory, max_size=1000)
	problem = False
	for i, wordi in enumerate(words):
		for j, wordj in enumerate(words[:i]):
			if similar(wordi, wordj):
				print("Are you aware that {} and {} are both words?".format(wordi, wordj))
				problem = True
	if problem:
		return 1
	else:
		print("All clear")
		return 0


def generate_dictionary(num_words=[1,1,1,1], seed=None, filename=None):
	"""generate a bunch of random unique words that do not conflict with seed"""
	if seed is None:
		seed = []
	
	all_words = []
	for i, num in enumerate(num_words): # for each syllable-count set
		words = []
		j = 0
		while j < num: # until you have created the correct number of words
			if i == 0:
				word = new_tense_marker()
			elif i == 1:
				word = new_particle()
			elif i == 2:
				word = new_verb()
			else:
				word = new_noun()

			too_similar = False # check that it is not too similar to any other words
			for w in seed+all_words+words:
				if similar(word, w):
					too_similar = True
					break
			if too_similar: continue

			min_idx, max_idx = 0, len(words)
			while True:
				idx = (min_idx+max_idx)//2
				if idx >= 0 and idx < len(words) and length(words[idx]) <= length(word):
					min_idx = idx+1
				elif idx > 0 and idx <= len(words) and length(words[idx-1]) > length(word):
					max_idx = idx-1
				else:
					words.insert(idx, word) # insert it into the list, sorted by number of characters
					break
			j += 1 # count it

		all_words += words
		with open(filename+'.csv', 'w', encoding='utf-8') as f:
			for word in all_words:
				f.write(word+'\n')
	return all_words


if __name__ == '__main__':
	print(check_words('dictionary'))
	words = generate_dictionary(num_words=[10, 50, 800, 600], seed=load_all_words('dictionary'), filename='dictionary/word_cache')
	for word in words:
		print(word)

# word generator
import copy
import os
import random


CONSONANTS = [{'k','t','p'},{'g','d','b'}, {'h','th','f'},{'y','dh','v'}, {'ng','n','m'}, {'ss','sh','s'},{'j','zh','z'}]
VOWELS = [{'a','e','o'}, {'r','i','u','l'}]

VALID_CHAINS = [[5], [6], [], [], [], [0], []]


def random_choice(s):
	"""because random_choice doesn't work for sets"""
	return random.choice(tuple(s))


def similar(a, b):
	"""return True if a and b might sound too similar"""
	return a == b


def length(word):
	"""the number of Djastiz letters in the word"""
	return len(word.replace('th',' ').replace('dh',' ').replace('sh',' ').replace('zh',' ').replace('ng',' ').replace('ss',' '))


def new_consonant_group():
	""" generate a string of CONSONANTS that make a single sound together"""
	row = random.randrange(0,len(CONSONANTS))
	group = random_choice(CONSONANTS[row])
	if VALID_CHAINS[row] and random.random() < .3:
		row = random_choice(VALID_CHAINS[row])
		group += random_choice(CONSONANTS[row])
	return group


def new_strong_vowel(previous='', l_allowed=False):
	"""choose a consonant-like vowel that fits here"""
	possibilities = VOWELS[1]
	if previous[-1:] in VOWELS[1]:
		possibilities = possibilities - {previous[-1:]} #apparently "a-=b" in Python is _not_ equivalent to "a=a-b".
	elif previous.endswith('ss') or previous.endswith('j'):
		possibilities = possibilities - {'i', 'u'} #because you know. It's not like that's exactly what that means or anything
	elif previous.endswith('sh') or previous.endswith('zh'):
		possibilities = possibilities - {'r', 'u'}
	elif previous.endswith('s') or previous.endswith('z'):
		possibilities = possibilities - {'r', 'i'}
	elif previous.endswith('d') or previous.endswith('t'):
		possibilities = possibilities - {'r', 'i', 'l'}
	if not l_allowed or previous.endswith('h') or previous.endswith('y'):
		possibilities = possibilities - {'l'}
	return random_choice(possibilities)


def new_vowel_group(previous=''):
	"""generate 1-2 VOWELS that make a single sound together"""
	last_letter = previous[-1:]
	if random.random() < .2:
		return random_choice(VOWELS[0]) + random_choice(VOWELS[1])
	else:
		return random_choice(VOWELS[0]|VOWELS[1]-{'l'}-{last_letter}) #l cannot be a standalone vowel, nor may the vowel repeat the last letter


def new_word(num_syl):
	"""generate a random word with num_syl syllables"""
	if random.random() < .7:
		word = new_consonant_group()
	else:
		word = ''
	if random.random() < .3:
		word += new_strong_vowel(word, l_allowed=False)
	word += new_vowel_group(word)

	for i in range(num_syl-1):
		if random.random() < .5:
			word += new_consonant_group()
		elif random.random() < .8:
			word += new_strong_vowel(word, l_allowed=True)
		else:
			word += new_consonant_group()
			word += new_strong_vowel(word, l_allowed=True)
		word += new_vowel_group(word)

	if random.random() < .7:
		word += new_consonant_group()
	return word


def load_all_words(directory, max_size=0):
	"""return a list of all the words in this directory"""
	words = []
	for filename in os.listdir(directory):
		if 'cache' not in filename:
			with open(directory+'\\'+filename, 'r') as f:
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


def generate_dictionary(num_words_syl=[5,5], seed=None, filename=None):
	"""generate a bunch of random unique words"""
	if seed is None:
		seed = []

	words = []
	for i, num_words in enumerate(num_words_syl): # for each syllable-count set
		num_syl = i+1
		j = 0
		while j < num_words: # until you have created the correct number of words
			word = new_word(num_syl) # think of a word

			too_similar = False # check that it is not too similar to any other words
			for w in seed+words:
				if similar(word, w):
					too_similar = True
					break
			if too_similar: continue

			min_idx, max_idx = 0, len(words)
			while True:
				idx = (min_idx+max_idx)//2
				if idx >= 0 and idx < len(words) and (length(words[idx])-1)//2 <= (length(word)-1)//2:
					min_idx = idx+1
				elif idx > 0 and idx <= len(words) and (length(words[idx-1])-1)//2 > (length(word)-1)//2:
					max_idx = idx-1
				else:
					words.insert(idx, word) # insert it into the list, sorted by number of characters
					break
			j += 1 # count it

			if j % 1000 == 0:
				with open(filename+'.csv','w') as f:
					for word in words:
						f.write(word+'\n')
	return words


if __name__ == '__main__':
	print(check_words('dictionary'))
	words = generate_dictionary([2000], seed=load_all_words('dictionary'), filename='dictionary/word_cache')
	for word in words:
		print(word)

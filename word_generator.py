# word generator
import copy
import os
import random


vowels = [['a','e','o'], ['i','u']]
consonants = ['k','g','t','d','p','b','s','z','c','j']

char_type = {'':-1,'a':0,'e':0,'o':0,'i':0,'u':0,'k':1,'t':1,'p':1,'g':1,'d':1,'b':1,'s':2,'c':2,'z':2,'j':2,}


def similar(a, b):
	"""return True if a and b might sound too similar"""
	for i in range(3):
		if len(a) > len(b):
			a, b = b, a
		if len(a) < len(b):
			return a == b[1:] or a == b[:-1]
		else:
			one_diff = False
			for i in range(len(a)):
				if char_type[a[i]] != char_type[b[i]]:
					return False
				if a[i] != b[i]:
					if one_diff:
						return False
					one_diff = True
			return True


def random_vowel(nxt):
	"""pick a vowel"""
	options = copy.copy(vowels[0])+copy.copy(vowels[1])
	if nxt != '' and nxt in options:
		options.remove(nxt)
	return random.choice(options)


def random_consonant():
	"""pick 1-2 pronounceable random consonants"""
	return random.choice(consonants)


def strong_vowel(nxt):
	"""pick one of the strong vowels that is not equal to next"""
	l = copy.copy(vowels[1])
	if nxt in l:
		l.remove(nxt)
	return random.choice(l)


def new_vowel_group(next_letter=''):
	"""generate 1-2 vowels that make a single sound together"""
	if char_type[next_letter] != 0 and random.random() < .15:
		return random.choice(vowels[0]) + random.choice(vowels[1])
	else:
		return random_vowel(next_letter)


def new_consonant_group(next_letter=''):
	"""generate a consonant and/or a strong vowel"""
	if next_letter == '' or random.random() < .9:
		return random_consonant()
	elif random.random() < .6:
		return strong_vowel(next_letter[0])
	else:
		return random_consonant()+strong_vowel(next_letter[0])


def new_word(num_syl):
	"""generate a random word with num_syl syllables"""
	if random.random() < .7:
		word = new_consonant_group()
	else:
		word = ''
	word = new_vowel_group() + word
	for i in range(num_syl-1):
		c = new_consonant_group(word[0])
		v = new_vowel_group(c[0])
		word = v+c+word
	if random.random() < .7:
		word = new_consonant_group(word[0])+word
	
	for i in range(len(word)-1, 0, -1): # remove duplicate letters
		if word[i] == word[i-1]:
			word = word[0:i]+word[i+1:len(word)]
	return word


def load_all_words(directory, max_size=0):
	"""return a list of all the words in this directory"""
	words = []
	for filename in os.listdir(directory):
		with open(directory+'\\'+filename, 'r') as f:
			lines = f.readlines()
			if max_size == 0 or len(lines) < max_size:
				for line in lines:
					if len(line) > 1:
						try:
							words.append(line[line.index(',')+1:].replace('sh','c').replace('\n',''))
						except ValueError:
							words.append(line.replace('sh','c').replace('\n',''))
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
	if seed == None: #pre-existing words
		seed = []

	cache = [] #words from previous syllable counts

	for i, num_words in enumerate(num_words_syl): # for each syllable-count set
		words = []
		num_syl = i+1
		j = 0
		while j < num_words: # until you have created the correct number of words
			word = new_word(num_syl) # think of a word

			too_similar = False # check that it is not too similar to any other words
			for w in seed+cache+words:
				if similar(word, w):
					too_similar = True
					break
			if too_similar: continue

			min_idx, max_idx = 0, len(words)
			while True:
				idx = (min_idx+max_idx)//2
				if idx >= 0 and idx < len(words) and len(words[idx])//num_syl <= len(word)//num_syl:
					min_idx = idx+1
				elif idx > 0 and idx <= len(words) and len(words[idx-1])//num_syl > len(word)//num_syl:
					max_idx = idx-1
				else:
					words.insert(idx, word) # insert it into the list, sorted by number of characters
					break
			j += 1 # count it

			if j % 1000 == 0:
				with open(filename+'.csv','w') as f:
					for word in cache:
						f.write(word+'\n')
					for word in words:
						f.write(word+'\n')
		cache = cache+words
	return cache


if __name__ == '__main__':
	print(check_words('dictionary'))
	# words = generate_dictionary([0,20], seed=load_all_words('dictionary'))
	# for word in words:
	# 	print(word)

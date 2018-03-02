#translator.py
import csv
import matplotlib.pyplot as plt
import numpy as np
import os


def compound(english, components, eng_to_dja={}, pts_o_spch={}):
	"""create a compound word out of several component words"""
	intermediate = components.split(' ') #read the provided list of space-separated English words
	djastiz = ''
	for eng_word in intermediate: #then translate and stack them
		try:
			if djastiz and djastiz[-1] + eng_to_dja[eng_word][0] in ('ng','th','dh','ss','sh','zh'):
				djastiz += "'" + eng_to_dja[eng_word] #use aprostrophes to separate phonemes like ss and h, when necessary
			else:
				djastiz += eng_to_dja[eng_word] #and translate and combine them
		except KeyError as e:
			raise ValueError("The word for '{}' relies on the nonexistent word for {}".format(english, e))

	root_part = pts_o_spch[eng_to_dja[intermediate[0]]] #the part of speech is based on the part of the first word
	if root_part == 'compound pronoun': 	root_part = 'noun' #compound pronouns that get used in compounds should be called nouns
	elif root_part == 'fastener': 			root_part = 'modifier' #fasteners become modifiers when combined with other words
	whole_part = root_part if 'compound' in root_part else 'compound '+root_part #attach 'compound' unless it's already there
	return english, djastiz, whole_part


def translate_quoted(phrase, eng_to_dja={}):
	"""replace quoted english words with Djastiz words"""
	if '"' in phrase:
		assert phrase.count('"')%2 == 0, "Character vector is not terminated properly: {}".format(note)
		pieces = phrase.split('"')
		phrase = ''
		for i in range(0, len(pieces)-1, 2):
			try:
				translated = translate_line(pieces[i+1], eng_to_dja)
				phrase += pieces[i] + '[`' + translated + '`](#' + translated + ')'
			except ValueError as e:
				phrase += pieces[i] + '"' + pieces[i+1] + '"'
				print("Warning: missing word in definition notes" + str(e)[str(e).index(':'):])
	return phrase


def load_dictionary(directory):
	"""return a dict mapping English words to Djastiz words, Djastiz words to English words,
	Djastiz words to part of speech, and English words to notes"""
	eng_to_dja, dja_to_eng, pts_o_spch, notes = {}, {}, {}, {}
	all_filenames = os.listdir(directory)
	all_filenames.remove('word_cache.csv')
	all_filenames.remove('compound_word.csv')
	all_filenames.append('compound_word.csv') #do the compound words last
	for filename in all_filenames:
		with open(directory+'\\'+filename,'r') as csvfile:
			for line in csv.reader(csvfile):
				if len(line) < 2:
					raise ValueError("There are not enough commas in {}".format(line))
				if filename == 'compound_word.csv': #compound words need a bit more work
					english, djastiz, prt_o_spch = compound(*line, eng_to_dja=eng_to_dja, pts_o_spch=pts_o_spch)
				else:
					english, djastiz = line
					prt_o_spch = filename[:-4]

				if '(' in english:
					assert ')' in english, "Unbalanced or unexpected parenthesis or bracket: {}".format(english)
					note = english[english.index('(')+1:english.index(')')]
					english = english[:english.index('(')-1]
				else:
					note = None
				if len(english) == 0 or len(djastiz) == 0:
					raise ValueError("I think you forgot something, Justin: '{}', `{}`".format(english, djastiz))
				if english in eng_to_dja:
					raise ValueError("There are two words for '{}': `{}` and `{}`".format(english, eng_to_dja[english], djastiz))
				if djastiz in dja_to_eng:
					raise ValueError("`{}` has two meanings: '{}' and '{}'".format(djastiz, dja_to_eng[djastiz], english))
				eng_to_dja[english] = djastiz
				dja_to_eng[djastiz] = english
				pts_o_spch[djastiz] = prt_o_spch
				if note != None:
					notes[english] = note

	return eng_to_dja, dja_to_eng, pts_o_spch, notes


def translate_line(eng_sent, english_to_djastiz, hist=None):
	"""return the word-for-word translation of this line"""
	frequencies = {} if hist==None else hist
	eng_words = eng_sent.split()
	dja_line = ""
	for eng_word in eng_words:
		if eng_word in english_to_djastiz:
			dja_word = english_to_djastiz[eng_word]
			dja_line += dja_word
			if not eng_word.endswith("-"):
				dja_line += " "
			frequencies[dja_word] = frequencies.get(dja_word,0)+1
		else:
			if eng_word[0] != eng_word[0].upper(): #ignore capitalized words for which there is no word
				raise ValueError("Missing word in '{}': There is no word for '{}'".format(eng_sent.strip(), eng_word))
			else:
				dja_line += eng_word+" "
	return dja_line[:-1]


def translate(filename, english_to_djastiz, hist=None, arr=None):
	"""replace every %4=2 line with the word-for-word translation of the previous line
	and return a word frequency histogram and an array of syllable counts from encountered sentences"""
	frequencies = {} if hist==None else hist
	syl_counts = [] if arr==None else arr
	new_file = ""
	with open(filename,'r') as f:
		for i, line in enumerate(f):
			if i%4 == 2:
				new_file += translate_line(eng_sent, english_to_djastiz, hist=frequencies)+'\n'
			else:
				new_file += line
			if i%4 == 1:
				eng_sent = line
			if i%4 == 0:
				if '->' in line:
					n_e, n_d = line[line.rindex('[')+1:line.rindex(']')].split('->')
					syl_counts.append([int(n_e), int(n_d)])

	with open(filename,'w') as f:
		f.write(new_file)
	return frequencies, syl_counts


def reverse_dictionary(djastiz_to_english, english_to_djastiz, djastiz_to_pos, english_to_notes, filename):
	"""create a Djastiz-to-English dictionary and save it to filename"""
	alphabetized = sorted(djastiz_to_english.keys())
	with open(filename,'w') as f:
		f.write("# Word Guide\n\n")
		f.write("This complete Modern-Djastiz-to-English dictionary gives the part of speech and English meaning of each Modern Djastiz word in latin alphabetical order. A crucial reference for anyone living in this post-Djastiz society.\n\n")
		f.write(translate_line(
				"dictionary what-kind to Modern-Djastiz obj English ind who completeness this sbj both part-of-speech and one-that-gets- denote which-one English which-one each word what-kind Modern-Djastiz obj say alphabet which-one Latium one arrange by . one-that-gets- reference of-which need person of-which society who Modern-Djastiz obj hence any sbj obj",
				english_to_djastiz)+"\n")
		f.write("______\n")
		for djastiz in alphabetized:
			f.write("\n### {}\n_{}_  \n\t*{}*".format(djastiz, djastiz_to_pos[djastiz], djastiz_to_english[djastiz]))
			if djastiz_to_english[djastiz] in english_to_notes:
				f.write("; {}".format(translate_quoted(english_to_notes[djastiz_to_english[djastiz]], english_to_djastiz)))
			f.write("\n")


if __name__ == '__main__':
	eng_to_dja, dja_to_eng, dja_to_pos, eng_to_notes = load_dictionary('dictionary')
	reverse_dictionary(dja_to_eng, eng_to_dja, dja_to_pos, eng_to_notes, 'word_guide.md')
	hist = {}
	arr = []
	hist, arr = translate('proverbs.txt', eng_to_dja, hist, arr)
	hist, arr = translate('common_expressions.txt', eng_to_dja, hist, arr)
	hist, arr = translate('examples.txt', eng_to_dja, hist, arr)
	for key in sorted(hist.keys(), key=lambda k: hist[k]):
		print("{:03}\t{}".format(hist[key], key))

	arr = np.array(arr)
	plt.plot([0, max(arr[:,0])], [0, max(arr[:,0])])
	plt.plot(arr[:,0], arr[:,1], '.')
	plt.axis('square')
	plt.savefig('syllable_comparison.png')
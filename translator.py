#translator.py
import matplotlib.pyplot as plt
import numpy as np
import os

def load_dictionary(directory):
	"""return a dict mapping English words to Djastiz words, Djastiz words to English words,
	Djastiz words to part of speech, and English words to notes"""
	eng_to_dja, dja_to_eng, pts_o_spc, notes = {}, {}, {}, {}
	for filename in os.listdir(directory):
		if 'word_cache' in filename:	continue
		with open(directory+'\\'+filename,'r') as f:
			for line in f:
				if len(line) <= 1:		break
				if line[-1] == '\n':	line = line[:-1]
				try:
					english, djastiz = tuple(line.split(','))
				except ValueError:
					raise ValueError("There are too many commas in '{}'".format(line))
				if '(' in english:
					note = english[english.index('(')+1:english.index(')')]
					english = english[:english.index('(')-1]
				else:
					note = None
				if len(english) == 0 or len(djastiz) == 0:
					raise ValueError("I think you forgot something, Justin: '{}', `{}`".format(english, djastiz))
				if english in eng_to_dja:
					raise ValueError("There are two words for '{}'".format(english))
				if djastiz in dja_to_eng:
					raise ValueError("`{}` has two meanings".format(djastiz))
				eng_to_dja[english] = djastiz
				dja_to_eng[djastiz] = english
				pts_o_spc[djastiz] = filename[:-4]
				if note != None:
					notes[english] = note
	return eng_to_dja, dja_to_eng, pts_o_spc, notes


def translate(filename, english_to_djastiz, hist=None, arr = None):
	"""replace every %4=2 line with the word-for-word translation of the previous line
	and return a word frequency histogram and an array of syllable counts from encountered sentences"""
	frequencies = {} if hist==None else hist
	syl_counts = [] if arr==None else arr
	new_file = ""
	with open(filename,'r') as f:
		for i, line in enumerate(f):
			if i%4 == 2:
				eng_words = eng_sent.split()
				dja_line = ""
				for eng_word in eng_words:
					if eng_word in english_to_djastiz:
						dja_word = english_to_djastiz[eng_word]
						dja_line=dja_line+ dja_word+" "
						frequencies[dja_word] = frequencies.get(dja_word,0)+1
					else:
						dja_line=dja_line+ eng_word+" " #ignore capitalized words
						if eng_word[0] != eng_word[0].upper():
							print("Warning: There is no word for '{}'".format(eng_word))
				new_file=new_file+ dja_line[:-1]+'\n'
			else:
				new_file=new_file+ line
			if i%4 == 1:
				eng_sent = line
			if i%4 == 0:
				if '->' in line:
					n_e, n_d = line[line.index('(')+1:line.index(')')].split('->')
					syl_counts.append([int(n_e), int(n_d)])

	with open(filename,'w') as f:
		f.write(new_file)
	return frequencies, syl_counts


def reverse_dictionary(djastiz_to_english, djastiz_to_pos, english_to_notes, filename):
	"""create a Djastiz-to-English dictionary and save it to filename"""
	alphabetized = sorted(djastiz_to_english.keys())
	with open(filename,'w') as f:
		f.write("<dl>\n")
		for djastiz in alphabetized:
			f.write("<dt>{}</dt>\n<dd><i>{}</i>\t<b>{}</b>".format(djastiz, djastiz_to_pos[djastiz], djastiz_to_english[djastiz]))
			if djastiz_to_english[djastiz] in english_to_notes:
				f.write("; {}".format(english_to_notes[djastiz_to_english[djastiz]]))
			f.write("</dd>\n\n")
		f.write("</dl>")


if __name__ == '__main__':
	eng_to_dja, dja_to_eng, dja_to_pos, eng_to_notes = load_dictionary('dictionary')
	reverse_dictionary(dja_to_eng, dja_to_pos, eng_to_notes, 'word_guide.md')
	hist = {}
	arr = []
	hist, arr = translate('idioms.txt', eng_to_dja, hist, arr)
	hist, arr = translate('common_expressions.txt', eng_to_dja, hist, arr)
	hist, arr = translate('examples.txt', eng_to_dja, hist, arr)
	for key in sorted(hist.keys(), key=lambda k: hist[k]):
		print("{:03}\t{}".format(hist[key], key))

	arr = np.array(arr)
	plt.plot(arr[:,0], arr[:,1], '.')
	plt.xlim([0,70])
	plt.ylim([0,70])
	plt.axis('square')
	plt.savefig('syllable_comparison.png')
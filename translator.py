#translator.py
import os

def load_dictionary(directory):
	"""return a dict mapping English words to Djastiz words, Djastiz words to English words,
	Djastiz words to part of speech, and English words to notes"""
	eng_to_dja, dja_to_eng, pts_o_spc, notes = {}, {}, {}, {}
	for filename in os.listdir(directory):
		if 'word_cache' in filename:	continue
		with open('{}\\{}'.format(directory,filename),'r') as f:
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


def translate(filename, english_to_djastiz, hist=None):
	"""replace every %4=2 line with the word-for-word translation of the previous line
	and return a word frequency histogram"""
	frequencies = {} if hist==None else hist
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
						dja_line=dja_line+ eng_word+" "
						print("Warning: There is no word for '{}'".format(eng_word))
				new_file=new_file+ dja_line[:-1]+'\n'
			else:
				new_file=new_file+ line
			if i%4 == 1:
				eng_sent = line

	with open(filename,'w') as f:
		f.write(new_file)
	return frequencies


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
	hist = translate('idioms.txt', eng_to_dja, hist)
	hist = translate('common_expressions.txt', eng_to_dja, hist)
	hist = translate('examples.txt', eng_to_dja, hist)
	for key in sorted(hist.keys(), key=lambda k: hist[k]):
		print("{:03}\t{}".format(hist[key], key))
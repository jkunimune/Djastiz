#translator.py
import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import random


TONES = {u'\u030F':0, u'\u0300':4, u'\u0304':7, u"\u0301":10, u'\u030B':12}
VOWELS = {'a', 'e', 'i', 'o', 'u'}


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

	root_part = pts_o_spch[eng_to_dja[intermediate[-1]]] #the part of speech is based on the part of the first word
	if root_part == 'pronoun': 				root_part = 'noun' #compound pronouns that get used in compounds should be called nouns
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
				translated, melody = translate_line(pieces[i+1], eng_to_dja, {})
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
		with open(directory+'\\'+filename, 'r', encoding='utf-8') as csvfile:
			for line in csv.reader(csvfile):
				if len(line) < 2:
					raise ValueError("There are not enough commas in {}".format(line))
				elif len(line) > 2:
					raise ValueError("There are not enough quotations in {}".format(line))
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


def word_to_notes(djastiz, djastiz_to_pos):
	"""return a list of pitch numbers and lengths for this word"""
	part_of_speech = djastiz_to_pos.get(djastiz, None)
	if part_of_speech == 'tense-marker':
		for char in djastiz:
			if char in TONES:
				if TONES[char] == 0:
					return [(None, 1), (0, .5)]
				else:
					return [(TONES[char], .5)]
	elif part_of_speech in {'postposition','conjunction','fasteners','qualifiers'}:
		for char in djastiz:
			if char in TONES:
				return [(TONES[char], .5)]
		return [(-1, .5)]
	else:
		notes = []
		for i, char in enumerate(djastiz):
			if char in TONES:
				notes.append(TONES[char])
			elif char in VOWELS and (i == len(djastiz)-1 or djastiz[i+1] not in TONES):
				notes.append(-1)
		return [(note, 1/min(4,len(notes))) for note in notes]


def translate_line(eng_sent, english_to_djastiz, djastiz_to_pos, hist=None):
	"""return the word-for-word translation of this line"""
	frequencies = {} if hist==None else hist
	eng_words = eng_sent.split()
	dja_line = ""
	melody = []
	for eng_word in eng_words:
		if eng_word in english_to_djastiz:
			dja_word = english_to_djastiz[eng_word]
			dja_line += dja_word
			if not eng_word.endswith("-"):
				melody += word_to_notes(dja_line[dja_line.rfind(' ')+1:], djastiz_to_pos)
				dja_line += " "
			frequencies[dja_word] = frequencies.get(dja_word,0)+1
		else:
			if eng_word[0] != eng_word[0].upper(): #ignore capitalized words for which there is no word
				raise ValueError("Missing word in '{}': There is no word for '{}'".format(eng_sent.strip(), eng_word))
			else:
				dja_line += eng_word+" "
	return dja_line[:-1], melody


def translate(filename, english_to_djastiz, djastiz_to_pos, djastiz_to_hist=None):
	"""replace every %4=2 line with the word-for-word translation of the previous line
	and return a word frequency histogram and an array of syllable counts from encountered sentences"""
	frequencies = {} if hist==None else hist
	notes = []
	new_file = ""
	with open(filename, 'r', encoding='utf-8') as f:
		for i, line in enumerate(f):
			if i%4 == 2:
				sentence, melody = translate_line(eng_sent, english_to_djastiz, djastiz_to_pos, hist=frequencies)
				new_file += sentence+'\n'
				notes += melody + [(None,4)]
			else:
				new_file += line
			if i%4 == 1:
				eng_sent = line

	with open(filename, 'w', encoding='utf-8') as f:
		f.write(new_file)
	save_to_midi(notes, filename)
	return frequencies


def save_to_midi(notes, filename):
	print(filename.replace('txt','mid'))
	with open(filename.replace('txt', 'mid'), 'wb') as f:
		f.write(b'MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x78')
		track_chunk = b''
		tonic = 60
		delay = 0
		last_note = 0
		for note, length in notes:
			if note is None:
				if length < 1:
					track_chunk += bytes([round(length*120), 0b10000000, 0, 0])
				else:
					num = round(length*120)
					track_chunk += bytes([128+num//128, num%128, 0b10000000, 0, 0])
				tonic = random.randint(58,62)
			else:
				note = note if note >= 0 else last_note
				track_chunk += bytes([0,                 0b10010000, tonic+note, 96]) #note on
				track_chunk += bytes([round(length*120), 0b10000000, tonic+note, 96]) #note off
				last_note = note
		track_chunk += b'\x00\xFF\x2F\x00'
		f.write(b'MTrk' + (len(track_chunk)).to_bytes(4,'big') + track_chunk)


def reverse_dictionary(djastiz_to_english, english_to_djastiz, djastiz_to_pos, english_to_notes, filename):
	"""create a Djastiz-to-English dictionary and save it to filename"""
	alphabetized = sorted(djastiz_to_english.keys())
	with open(filename, 'w', encoding='utf-8') as f:
		f.write("# Word Guide\n\n")
		f.write("This complete Musical-Djastiz-to-English dictionary gives the part of speech and English meaning of each Musical Djastiz word in latin alphabetical order. A crucial reference for anyone living in this post-Djastiz society.\n\n")
		f.write("`"+translate_line(
				"dictionary what-kind to Musical-Djastiz obj English ind who complete this sbj both part-of-speech and one-that-gets- denote which-one English which-one each word what-kind Musical-Djastiz obj say alphabet which-one Latium one arrange by . one-that-gets- reference of-which need person of-which society who Musical-Djastiz obj after any sbj obj",
				english_to_djastiz, djastiz_to_pos)[0]+"`\n")
		f.write("______\n")
		for djastiz in alphabetized:
			f.write("\n### `{}`\n_{}_  \n\t**{}**".format(djastiz, djastiz_to_pos[djastiz], djastiz_to_english[djastiz].replace('\\','&#54;')))
			if djastiz_to_english[djastiz] in english_to_notes:
				f.write("; {}".format(translate_quoted(english_to_notes[djastiz_to_english[djastiz]], english_to_djastiz)))
			f.write("\n")


if __name__ == '__main__':
	eng_to_dja, dja_to_eng, dja_to_pos, eng_to_notes = load_dictionary('dictionary')
	reverse_dictionary(dja_to_eng, eng_to_dja, dja_to_pos, eng_to_notes, 'word_guide.md')
	hist = {}
	hist = translate('proverbs.txt', eng_to_dja, dja_to_pos, hist)
	hist = translate('common_expressions.txt', eng_to_dja, dja_to_pos, hist)
	hist = translate('examples.txt', eng_to_dja, dja_to_pos, hist)
	translate('alphabet_song.txt', eng_to_dja, dja_to_pos)
	for key in sorted(hist.keys(), key=lambda k: hist[k]):
		print("{:03}\t{}".format(hist[key], key))

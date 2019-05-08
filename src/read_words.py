# read_words.py

from dragonmapper import hanzi
import epitran
import re
from os import path
import pandas as pd
import sys

sys.path.append(path.sep.join([*sys.path[0].split(path.sep)[0:-2], 'English-to-IPA']))
import eng_to_ipa # available at https://github.com/mphilli/English-to-IPA.git


LANG_CODES = {
	'zh-CN', 'es', 'eo', 'en', 'hi', 'bn', 'ar', 'pa', 'jv', 'yo',
	'mr', 'ms', 'ig', 'tl', 'sw', 'zu', 'ny', 'xh', 'sn', 'st'}
EPITRANSLATORS = {lang:epitran.Epitran(script) for lang, script in
	[('hi','hin-Deva'), ('bn','ben-Beng'), ('pa','pan-Guru'), ('yo','yor-Latn'),
	 ('mr','mar-Deva'), ('ms','msa-Latn'), ('tl','tgl-Latn'), ('sw','swa-Latn'),
	 ('zu','zul-Latn'), ('ny','nya-Latn'), ('xh','xho-Latn'), ('sn','sna-Latn')]}


def read_mandarin(word):
	""" read a word phonetically in Hanzi (Mandarin pronunciations) """
	try:
		broad = hanzi.to_ipa(word).replace('ɪ','ɪ̯').replace('ʊ','ʊ̯').replace('ʈʂ','ʈ͡ʂ').replace('tɕ','t͡ɕ').replace('ts','t͡s').replace('ʐ','ɻ').replace(' ','') # well, that was easy
	except ValueError:
		broad = '*'
	return broad, broad


def read_spanish(word):
	""" read a word phonetically in Spanish """
	broad = ''
	stress_i = None
	for i, c in enumerate(word):
		if c == 'á':
			stress_i = len(broad)
			broad += 'a'
		elif c == 'c':
			if i+1 < len(word) and word[i+1] == 'h':
				broad += 't͡ʃ'
			elif i+1 < len(word) and word[i+1] in 'eiéí':
				broad += 's'
			else:
				broad += 'k'
		elif c == 'é':
			stress_i = len(broad)
			broad += 'e'
		elif c == 'g':
			if i+1 < len(word) and word[i+1] in 'eiéí':
				broad += 'x'
			else:
				broad += 'ɡ'
		elif c == 'h':
			pass
		elif c == 'i':
			if (i+1 < len(word) and word[i+1] in 'aeouáéíóú') or (i-1 >= 0 and word[i-1] in 'aeoáéíóú'):
				broad += 'j'
			else:
				broad += 'i'
		elif c == 'í':
			stress_i = len(broad)
			broad += 'i'
		elif c == 'j':
			broad += 'x'
		elif c == 'l':
			if i+1 < len(word) and word[i+1] == 'l':
				broad += 'ʝ'
			elif i-1 >= 0 and word[i-1] == 'l':
				pass
			else:
				broad += 'l'
		elif c == 'ñ':
			broad += 'ɲ'
		elif c == 'ó':
			stress_i = len(broad)
			broad += 'o'
		elif c == 'q':
			broad += 'k'
		elif c == 'r':
			if (i-1 < 0 or word[i-1] in 'rmn ') or i == len(word)-1:
				broad += 'r'
			elif i+1 < len(word) and word[i+1] == 'r':
				pass
			else:
				broad += 'ɾ'
		elif c == 'u':
			if i-1 >= 0 and word[i-1] == 'q':
				pass
			elif i-1 >= 0 and word[i-1] == 'g' and i+1 < len(word) and word[i+1] in 'eiéí':
				pass
			elif (i+1 < len(word) and word[i+1] in 'aeoáéíó') or (i-1 >= 0 and word[i-1] in 'aeoiáéíó'):
				broad += 'w'
			else:
				broad += 'u'
		elif c == 'ú':
			stress_i = len(broad)
			broad += 'u'
		elif c == 'ü':
			broad += 'w'
		elif c == 'v':
			broad += 'b'
		elif c == 'x':
			broad += 'ks'
		elif c == 'y':
			if i+1 < len(word) and word[i+1] in 'aoeuáóéíú':
				broad += 'ʝ'
			elif i-1 >= 0 and word[i-1] in 'aoeáóéíú':
				broad += 'j'
			else:
				broad += 'i'
		elif c == 'z':
			broad += 's'
		else:
			broad += c
	if stress_i is None:
		vowels = [i for i,c in enumerate(broad) if c in 'aoeui']
		if len(vowels) > 1:
			stress_i = vowels[-2] if (broad[-1] in 'aoeuins') else vowels[-1]
	if stress_i is not None:
		while broad[stress_i-1] in 'jw':
			stress_i -= 1
		stress_j = stress_i-1
		while stress_j >= 0 and broad[stress_j] not in 'aeiou ':
			stress_j -= 1
		if stress_j < 0:
			broad = 'ˈ' + broad
		else:
			broad = broad[:(stress_j+stress_i+1)//2] + 'ˈ' + broad[(stress_j+stress_i+1)//2:]

	narrow = ''
	for i, c in enumerate(broad):
		last_char = broad[i-1] if i-1 >= 0 else None
		if last_char == 'ˈ':
			last_char = broad[i-2] if i-2 >= 0 else None
		if c == 'b':
			if (last_char and last_char not in 'mnŋ ') or i+1 >= len(broad):
				narrow += 'β'
			else:
				narrow += 'b'
		elif c == 'd':
			if (last_char and last_char not in 'mnŋ l') or i+1 >= len(broad):
				narrow += 'ð'
			else:
				narrow += 'd'
		elif c == 'ɡ':
			if (last_char and last_char not in 'mnŋ ') or i+1 >= len(broad):
				narrow += 'ɣ'
			else:
				narrow += 'ɡ'
		elif c == 'ʝ':
			if (last_char and last_char not in 'mnŋ ') or i+1 >= len(broad):
				narrow += 'ʝ'
			else:
				narrow += 'ɟ͡ʝ'
		elif c == 'n':
			if i+1 < len(broad) and broad[i+1] in 'kɡx':
				narrow += 'ŋ'
			else:
				narrow += 'n'
		else:
			narrow += c

	broad = broad.replace('ue','o').replace('ie','e') # this will easily and intelligibly make words more like other romance words
	if broad.startswith('ʝ'):
		broad = 'd͡ʒ' + broad[1:] # and make it clear that words like <llamar> should start with <c>, not <hj>
	return broad, narrow


def read_esperanto(word):
	""" read a word phonetically in Esperanto """
	broad = word.replace(
		'c', 't͡s').replace('ĉ', 't͡ʃ').replace('ĝ', 'd͡ʒ').replace('ĥ', 'x').replace(
		'ĵ', 'ʒ').replace('ŝ', 'ʃ').replace('ŭ', 'w').replace('g', 'ɡ')
	vowels = [i for i,c in enumerate(broad) if c in 'aeiou']
	if len(vowels) > 1:
		stress_i = vowels[-2]
		stress_j = stress_i-1 # locating the stress marker is by far the hardest part
		while stress_j >= 0 and broad[stress_j] not in 'aoeui': # as you may have guessed, I have my qualms with Esperanto. The orthography, though,
			stress_j -= 1 # is by far the best thing about it, and it boggles the mind that Idoists would ever try to change that.
		if stress_j < 0:
			broad = 'ˈ' + broad
		else:
			stress = (stress_j+stress_i+1)//2
			if broad[stress] == '͡':
				stress -= 1
			broad = broad[:stress] + 'ˈ' + broad[stress:]
	return broad, broad


def read_english(word):
	""" read a word phonetically in English """
	word = eng_to_ipa.convert(word.replace('-',' ')).replace('ʧ','t͡ʃ').replace('ʤ','d͡ʒ').replace('r','ɹ')\
		.replace('e','eɪ̯').replace('oʊ','oʊ̯').replace('aɪ','ɑɪ̯').replace('ɔɪ','ɔɪ̯').replace('aʊ','aʊ̯').replace('g','ɡ')

	if '*' in word: # if it couldn't find it,
		return '*', '*' # cry

	broad = ''
	for i, c in enumerate(word): # this could be considered an allophone, but I definitely want my program to see rhotic labialisation as an important feature
		if c == 'ɹ' and i+1 < len(word) and word[i+1] in 'aeiouəɪʊɔɑɛæ':
			broad += c+'ʷ'
		else:
			broad += c

	narrow = ''
	for i, c in enumerate(broad): # there aren't actually too many allohponies in English of which I could think
		if c in 'td' and i-1 >= 0 and broad[i-1] in 'aeiouəɪʊɔɑɛæɹj̯' and i+1 < len(broad) and broad[i+1] in 'aeiouəɪʊɔɑɛæɹj̯':
			narrow += 'ɾ'
		elif c in 'ptk' and (i == 0 or broad[i-1] == 'ˈ'):
			narrow += c+'ʰ'
		elif c in 'iu' and (i+1 >= len(broad) or broad[i+1] not in 'ɪʊɹ'):
			narrow += c+'ː'
		elif c == 'ɑ' and i+3 < len(broad) and broad[i+1:i+3] == 'ɪ̯' and broad[i+3] in 'ptkfθsʃh':
			narrow += 'ə'
		elif c == 'l' and (i+1 >= len(broad) or broad[i+1] not in 'aeiouəɪʊɔɑɛæ'):
			narrow += 'ɫ'
		elif c == 'ɹ' and i-1 >= 0 and broad[i-1] == 'ə':
			narrow = narrow[:-1] + 'ɚ'
		else:
			narrow += c
	return broad, narrow


def read_arabic(word):
	""" apply allophones to Arabic words """
	broad = word.replace('d͡ʒ','ʒ')
	narrow = ''
	for i, c in enumerate(broad):
		if c == 'a':
			if (i-1 >= 0 and broad[i-1] in 'rqˤ') or (i+1 < len(broad) and broad[i+1] in 'rq') or (i+2 < len(broad) and broad[i+2] == 'ˤ'):
				narrow += 'ɑ'
			elif i-1 < 0 or broad[i-1] not in 'xɣ':
				narrow += 'æ'
			else:
				narrow += 'a'
		elif c == 'i':
			if (i-1 >= 0 and broad[i-1] in 'ˤqrħʕ') or (i+1 < len(broad) and broad[i+1] in 'qrħʕ') or (i+2 < len(broad) and broad[i+2] in 'ˤ'):
				narrow += 'e'
			else:
				narrow += 'i'
		elif c == 'u':
			if (i-1 >= 0 and broad[i-1] in 'ˤqrħʕ') or (i+1 < len(broad) and broad[i+1] in 'qrħʕ') or (i+2 < len(broad) and broad[i+2] in 'ˤ'):
				narrow += 'o'
			else:
				narrow += 'u'
		elif c == 'ʒ':
			narrow += 'd͡ʒ'
		else:
			narrow += c
	return word, narrow


IGBO_DIGRAPHS = {
	'ch':'t͡ʃ', 'gb':'ɡ͡b', 'gh':'ɣ', 'gw':'ɡʷ', 'kp':'k͡p', 'kw':'kʷ', 'nw':'ŋʷ', 'ny':'ɲ', 'n\'':'ŋ', 'sh':'ʃ'}
IGBO_MONOGRAPHS = {
	'g':'ɡ', 'h':'ɦ', 'ṅ':'ŋ', 'ị':'ɪ', 'j':'dʒ', 'ọ':'ɒ', 'r':'ɾ', 'ụ':'ʊ', 'y':'j'}
def read_igbo(word):
	""" read a word phonetically in Igbo """
	word = word.replace('&#39;', '\'').lower()
	broad = ""
	i = 0
	while i < len(word):
		if i+1 < len(word) and word[i:i+2] in IGBO_DIGRAPHS:
			broad += IGBO_DIGRAPHS[word[i:i+2]]
			i += 2
		elif word[i] in IGBO_MONOGRAPHS:
			broad += IGBO_MONOGRAPHS[word[i]]
			i += 1
		else:
			broad += word[i]
			i += 1
	word, broad = broad, ""
	for i, c in enumerate(word): # special rules that I didn't want to treat as graphemes
		if c in 'mnɳŋ' and (i+1 >= len(word) or word[i+1] not in 'aeɪiɒoʊujʷ'):
			broad += c+'̩'
		else:
			broad += c

	narrow = ""
	for i, c in enumerate(broad):
		if c == 'ɾ' and (i-1 < 0 or word[i-1] not in 'aeɪiɒoʊu' or i+1 >= len(word) or word[i+1] not in 'aeɪiɒoʊu'):
			narrow += 'ɹ'
		else:
			narrow += c
	return broad, narrow


SOTHO_TRIGRAPHS = {
	'fsh':'fʃ', 'k\'h':'kʰ', 'psh':'pʃʰ', 'tlh':'t͡ɬʰ'}
SOTHO_DIGRAPHS = {
	'bj':'bj', 'ch':'t͡ʃʰ', 'hl':'ɬ', 'kh':'x', 'ng':'ŋ', 'ny':'ɲ', 'ph':'pʰ', 'qh':'ǃʰ',
	'nq':'ᵑǃ', 'sh':'ʃ', 'th':'tʰ', 'tj':'t͡ʃʼ', 'tl':'t͡ɬʼ', 'ts':'t͡sʼ', 'tš':'t͡sʰ'}
SOTHO_MONOGRAPHS = {
	'a':'ɑ', 'e':'e', 'g':'ɡ', 'j':'ʒ', 'k':'kʼ', 'o':'o', 'p':'pʼ', 'q':'ǃ', 'r':'ʀ', 't':'tʼ'}
SOTHO_EXCEPTIONS = {
	'lekʼɑ':'lɪkʼɑ', 'ʃebɑ':'ʃɛbɑ', 'pʼotsʼo':'pʼʊtsʼɔ', 'moŋolo':'mʊŋɔlɔ',
	'liʒo':'liʒɔ', 'pʼon̩t͡sʰo':'pʼon̩t͡sʰɔ', 'ɑbelɑ':'ɑbɛlɑ', 'moʒɑlefɑ':'mʊʒɑlɪfɑ',
	'ɬɑɬobɑ':'ɬɑɬʊbɑ', 'sexo':'sɪxɔ', 't͡sʼokʼot͡sʼɑ':'t͡sʼʊkʼʊt͡sʼɑ', 't͡sʰohɑ':'t͡sʰʊhɑ',
	't͡ɬʰɑho':'t͡ɬʰɑhɔ', 'xɑle':'xɑlɛ', 'ǃkʼoǃkʼɑ':'ǃkʼɔǃkʼɑ', 'leǃʰekʼu':'lɪǃʰekʼu',
	'bofʃwɑ':'bɔfʃwɑ', 'mol̩lo':'mʊl̩lɔ', 'pʰomɛl̩lɑ':'pʰʊmɛl̩lɑ', 'lefɑ':'lɪfɑ',
	'tʼɑt͡sʼo':'tʼɑt͡sʼɔ', 'let͡sʼo':'lɪt͡sʼɔ', 'seno':'sɪnɔ', 'elel̩lwɑ':'ɛlɛl̩lwɑ',
	'kʼelel̩lo':'kʼɛlɛl̩lɔ'} # not really exceptions, but the few words for which I know which sound the <e> and <o> make

def read_sotho(word):
	word = word.replace('&#39;', '\'').lower() # why do so many languages insist on using unicode instead of the ascii apostraphe? Even the IPA!
	broad = ""
	i = 0
	while i < len(word):
		if i+2 < len(word) and word[i:i+3] in SOTHO_TRIGRAPHS:
			broad += SOTHO_TRIGRAPHS[word[i:i+3]]
			i += 3
		elif i+1 < len(word) and word[i:i+2] in SOTHO_DIGRAPHS:
			broad += SOTHO_DIGRAPHS[word[i:i+2]]
			i += 2
		elif word[i] in SOTHO_MONOGRAPHS:
			broad += SOTHO_MONOGRAPHS[word[i]]
			i += 1
		else:
			broad += word[i]
			i += 1
	word, broad = broad, ""
	for i, c in enumerate(word): # special rules that I didn't want to treat as graphemes
		if c in 'eo' and i+1 < len(word) and word[i+1] in 'ɑeiou':
			broad += {'e':'j', 'o':'w'}[c]
		elif c == '\'' and i+1 < len(word) and word[i+1] in 'mnɲŋ':
			broad += word[i+1]+'̩'
		elif c == '\'':
			pass
		elif c == 'm' and i+1 < len(word) and word[i+1] == 'm':
			broad += word[i+1]+'̩'
		elif c == 'n' and i+1 < len(word) and word[i+1] in 'nɲŋ':
			broad += word[i+1]+'̩'
		elif c == 'l' and i+1 < len(word) and word[i+1] == 'l':
			broad += 'l̩'
		else:
			broad += c
	if broad in SOTHO_EXCEPTIONS:
		broad = SOTHO_EXCEPTIONS[broad] # this is accounting for the fact that I can't tell which sound <e> and <o> are supposed to make except for the examples I find on Wikipedia
	else:
		for old, new in SOTHO_EXCEPTIONS.items():
			broad = broad.replace(old, new)

	narrow = ""# I can't figure out if /x/->[kxʰ] and /ʒ/->[dʒ] are allophones or nonstandard variations.
	for i, c in enumerate(broad):
		if c == 'l' and i+1 < len(broad) and broad[i+1] in 'iu': # allophones, allophones
			narrow += 'd'
		elif c == 'w' and i+1 < len(broad) and broad[i+1] in 'ɑɛeɪiɔoʊu' and i-1 >= 0 and broad[i-1] not in 'ɑɛeɪiɔoʊu': # do whatever Dallas won't
			narrow += 'ʷ'
		elif c == 'j' and i-1 >= 0 and broad[i-1] == 'b': # change a sound every time
			narrow += 'ʒ'
		elif c == 'h' and i+1 < len(broad) and broad[i+1] in 'ɑɛeɪiɔoʊu' and i-1 >= 0 and broad[i-1] in 'ɑɛeɪiɔoʊu': # realise "p" just like "pine"
			narrow += 'ɦ'
		else: # LOOK OUT!
			narrow += c

	return broad, narrow # here come the allophoooooooooooooooooooooooones


JAVA_DIGRAPHS = {
	'ny':'ɲ', 'nc':'ɲt͡ʃ', 'nj':'ɲd͡ʒ', 'ng':'ŋ', 'kh':'x', 'sy':'ʃ', 'ai':'aj', 'th':'ʈ', 'dh':'ɖ'}
JAVA_MONOGRAPHS = {
	'a':'ɑ', 'e':'ə', 'é':'e', 'è':'ɛ', 'g':'ɡ', 'y':'j', 'c':'t͡ʃ', 'j':'d͡ʒ', 's':'ʂ', 'l':'ɭ', 'r':'ɽ'}

def read_javanese(word):
	broad = ""
	i = 0
	while i < len(word):
		if i+1 < len(word) and word[i:i+2] in JAVA_DIGRAPHS:
			broad += JAVA_DIGRAPHS[word[i:i+2]]
			i += 2
		elif word[i] in JAVA_MONOGRAPHS:
			broad += JAVA_MONOGRAPHS[word[i]]
			i += 1
		else:
			broad += word[i]
			i += 1

	narrow = ""
	for i, c in enumerate(broad):
		if c in 'bdɖɡ':
			narrow += {'b':'p','d':'t','ɖ':'ʈ','ɡ':'k'}[c]
		elif c in 'iu':
			if (i+1 == len(broad)-1 and broad[i+1] not in 'ɑeiouə') or \
					(i+2 < len(broad) and broad[i+1] not in 'ɑeiouə' and broad[i+2] not in 'ɑeiouə'):
				narrow += {'i':'ɪ','u':'ʊ'}[c]
			else:
				narrow += c
		elif c in 'eo':
			if (i+1 == len(broad)-1 and broad[i+1] not in 'ɑeiouə') or \
					(i+2 < len(broad) and broad[i+1] not in 'ɑeiouə' and broad[i+2] not in 'ɑeiouə') or \
					(i+2 < len(broad) and (broad[i+2] == 'ə' or broad[i+2] == c)) or \
					(i+2 < len(broad) and broad[i+2] in 'iu' and (i+3 == len(broad) or (i+3 < len(broad) and broad[i+3] in 'ɑeiouə'))):
				narrow += {'e':'ɛ','o':'ɔ'}[c]
			else:
				narrow += c
		elif c == 'ɑ':
			if i+1 == len(broad) or (i+3 == len(broad) and broad[i+2] == 'ɑ'):
				narrow += 'ɔ'
			else:
				narrow += 'ɑ'
		else:
			narrow += c
		if c in 'ɑeiouə' and i-1 >= 0 and broad[i-1] in 'bdɖɡ':
			narrow += '̤'

	return broad, narrow


def read(orthography, broad, lang):
	""" Convert a word in a language to IPA, usually straight from the orthography,
		but using a broad transcription as well in cases like Arabic. """
	if lang == 'zh-CN':
		return read_mandarin(orthography)
	elif lang == 'es':
		return read_spanish(orthography)
	elif lang == 'eo':
		return read_esperanto(orthography)
	elif lang == 'en':
		return read_english(orthography)
	elif lang == 'ar':
		return read_arabic(broad)
	elif lang == 'ig':
		return read_igbo(orthography)
	elif lang == 'st':
		return read_sotho(orthography)
	elif lang == 'jv':
		return read_javanese(orthography)
	else:
		epitranslated = EPITRANSLATORS[lang].transliterate(orthography.replace('&#39;',"'")) # TODO: epitran kind of sucks at Bengali... maybe I should do it myself
		if any([symb in epitranslated for symb in ['ऑ','ॉ','ऍ','ॅ']]): # I'm pretty sure this means it just didn't know how to say that in that language
			return '*', '*'
		return (epitranslated.replace('g','ɡ').replace('ঁ','̃').replace('ਂ','̃').replace('ੱ','ː').replace('ঃ','h').replace('ɔ্','').replace('š','ʃ').replace('Ṽ','ã').replace("'",'̩'),)*2


if __name__ == '__main__':
	for lang in LANG_CODES:
		table = pd.read_csv('../data/dict_{}.csv'.format(lang), header=None, names=['meaning','orthography','broad','narrow'], na_filter=False)
		for i, (meaning, orthography, broad, narrow) in list(table.iterrows()):
			if orthography and not narrow:
				table.iloc[i][['broad','narrow']] = read(orthography, broad, lang)
			print("In {}, {} is spelled <{}> and read /{}/ [{}]".format(lang, *table.iloc[i]))
		table.to_csv('../data/dict_{}.csv'.format(lang), header=False, index=False)
#get_language_info.py

import csv
import requests
import pickle
import re


try:
	with open('..\\data\\language_codes.pkl', 'rb') as f:
		lang_set = pickle.load(f)
except FileNotFoundError:
	print("Collecting set of all languages...")
	lang_set = set()
	for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		print("'{}' languages...".format(letter))
		r = requests.get('https://ethnologue.com/browse/names/{}'.format(letter))
		for lang_link in re.findall(r'\/language\/[a-z][a-z][a-z]', r.text):
			lang_set.add(lang_link[-3:])
	with open('..\\data\\language_codes.pkl', 'wb') as f:
		pickle.dump(lang_set, f)
print(lang_set)
print("{} languages of interest".format(len(lang_set)))

try:
	with open('..\\data\\ethnologue.pkl', 'rb') as f:
		data = pickle.load(f)
		print("{} languages loaded.".format(len(data)))
except FileNotFoundError:
	data = {}
	print("No languages loaded.")

i = 0
for lang_code in lang_set:
	if lang_code in data:
		continue #don't worry about it if you already have this one
	print("{}: ".format(lang_code), end='')
	try:
		r = requests.get('https://www.ethnologue.com/language/{}'.format(lang_code))
	except requests.exceptions.ConnectionError:
		raise Exception("No Internet connection!") #shorten the error message
	# if "Ethnologue has no page for" in r.text:
	# 	print("No Ethnologue entry")
	# 	continue #if it's not on Ethnologue, don't worry about it

	is_macro = '<h2>A macrolanguage of' in r.text

	name_text = r.text[r.text.index('<title>')+7 : r.text.index(' | Ethnologue</title>')]
	name = name_text

	if "Not an L1" in r.text:
		population = 0
	else:
		try:
			pop_text = r.text[r.text.index('<div class="field-label">Population</div') :]
		except ValueError:
			population = 0
		else:
			pop_text = pop_text[pop_text.index('<p>')+3 : pop_text.index('</p>')]
			if "all countries: " in pop_text:
				pop_text = pop_text[pop_text.index("all countries: ")+15 :]
			if "all languages: " in pop_text:
				pop_text = pop_text[pop_text.index("all languages: ")+15 :]
			if "L1: " in pop_text:
				pop_text = pop_text[pop_text.index("L1: ")+4 :]
			pop_text = pop_text.replace(',','').replace('.',' ').replace(';',' ')
			if ' ' in pop_text:
				pop_text = pop_text[:pop_text.index(' ')]
			try:
				population = int(pop_text)
			except ValueError:
				population = 0

	if not is_macro: #ethnologue doesn't have classification info for macrolanguages for some reason
		class_text = r.text[r.text.index('<div class="field-label">Classification</div>') :]
		class_text = class_text[class_text.index('<a href="') : class_text.index('</a>')]
		class_text = class_text[class_text.index('>')+1 :]
		classification = class_text.split(', ')
	else:
		classification = ['Macrolanguage']

	if is_macro:
		child_text = r.text[r.text.index('Includes: ') : ]
		child_text = child_text[: child_text.index('</p>')]
		relatives = [s[1:-1] for s in re.findall(r'\[[a-z][a-z][a-z]\]', child_text)]
	elif 'A member of macrolanguage' in r.text:
		mlang_text = r.text[r.text.index('A member of macrolanguage') :]
		relatives = mlang_text[mlang_text.index('[')+1 : mlang_text.index(']')]
	else:
		relatives = None

	data[lang_code] = (name, population, classification, relatives)
	print("{}".format(data[lang_code]))
	i += 1

	if i%12 == 0:
		print("Saving {} languages...".format(len(data)), end="\t")
		with open('..\\data\\ethnologue.pkl', 'wb') as f:
			pickle.dump(data, f)
		print("Saved!")

data['pan'] = ('Punjabi', data['pan'][1]+data['pnb'][1], data['pan'][2], None)
data.pop('pnb') #merge [pan] and [pnb], because Google Translate considers them one language, as do many of the people I've read on the Internet

print("Saving all languages...")
with open('..\\data\\ethnologue.pkl', 'wb') as f:
	pickle.dump(data, f)
print("Done!")

# choose_phonemes.py
#
# requires `phoible-phonemes.tsv` from https://github.com/phoible/phoible/releases/tag/v2014
# to be placed in `..\data\`

import csv
import requests
import matplotlib.pyplot as plt

from lang_data import POPULATIONS

MODIFIERS = {'ː', 'ˑ', 'ʷ', 'ʲ', 'ˠ', 'ˤ', 'ˀ'}

COMBOS = {('a','a̟','ɑ','ɐ'), ('e','e̞','ɛ'), ('o','o̞','ɔ'),
		('i','ɪ'), ('u','ʊ','ɯ'), ('j','i'), ('w','u'),
		('ʃ','s','ʂ','ʰ'), ('ʒ','z','ʐ','ʰ'), ('ts','t̪s̪','t̠ʃ','ʈʂ','ʰ'), ('dz','d̪z̪','d̠ʒ','ʰ'),
		('s','ts','t̪s̪','ʰ'), ('z','dz','d̪z̪','ʰ'), ('t̠ʃ','ʃ','ʈʂ','ʂ','ʰ'), ('d̠ʒ','ʒ','ʐ','ʰ'),
		('r','ɾ','ɽ'), ('l','ɾ','r'),  ('n','n̪'), ('m','ɱ'),
		('h','ħ','χ','x', 'ɦ'), ('ɦ','ʕ','ʁ','ɣ'), ('f','ɸ'), ('v','β'),
		('g','gʰ','kʰ'), ('d','d̪','dʰ','d̪ʰ','tʰ','t̪ʰ'), ('b','bʰ','pʰ'),
		('k','ʰ'), ('t','t̪','ʰ'), ('p','ʰ')}

DJASTIZ = {'/e/', '/a/', '/o/', '/i/', '/u/', '/j/', '/l/', '/w/', '/n/', '[m]', '/h/', '/s/', '/t̠ʃ/', '/k/', '/t/', '/p/'}

with open('..\\data\\phoible-phonemes.tsv', 'r', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter='\t')
	header = None
	data_sets = {}
	inventories = {}
	language_names = {}
	for row in reader:
		data_idx, lang_code, lang_name, phoneme, clazz = row[0], row[2], row[3], row[7], row[8]
		if header is None:
			header = row
			continue
		if lang_code not in inventories:
			data_sets[lang_code] = data_idx
			inventories[lang_code] = set()
			language_names[lang_code] = lang_name
		if data_sets[lang_code] == data_idx: #only use the first instance of each language
			for mod in MODIFIERS: #pull out some uncommon modifiers
				if mod in phoneme:
					phoneme = phoneme.replace(mod,'')
					inventories[lang_code].add('{}[{}]:'.format(clazz[0].upper(), mod))
			if clazz == 'tone': #with tones, the number matters more than the exact value
				for num_tones in range(10,-1,-1):
					if str(num_tones)+'T: ' in inventories[lang_code] or num_tones <= 0: #count tones
						inventories[lang_code].add(str(num_tones+1)+'T: ')
						break
			inventories[lang_code].add('['+phoneme+']:')

			for allophone_set in COMBOS:
				if phoneme in allophone_set:
					inventories[lang_code].add('/'+allophone_set[0]+'/:')
				elif 'ʰ' in allophone_set and 'ʰ' in phoneme and phoneme.replace('ʰ','') in allophone_set:
					inventories[lang_code].add('/'+allophone_set[0]+'/:')

phonemes = {}
total_pop = 0
for lang_code, inventory in inventories.items():
	if lang_code not in POPULATIONS:
		r = requests.get('https://www.ethnologue.com/language/{}'.format(lang_code))
		try:
			pop_text = r.text[r.text.index('<div class="field-label">Population</div')+41:]
		except ValueError:
			print("'{}':?, ".format(lang_code))
			continue
		pop_text = pop_text[pop_text.index('<p>')+3:pop_text.index('</p>')]
		if "all countries: " in pop_text:
			pop_text = pop_text[pop_text.index("all countries: ")+15:]
		if "L1: " in pop_text:
			pop_text = pop_text[pop_text.index("L1: ")+4:]
		pop_text = pop_text.replace(',','').replace('.',' ').replace(';',' ')
		if ' ' in pop_text:
			pop_text = pop_text[:pop_text.index(' ')]
		try:
			population = int(pop_text)
		except ValueError:
			population = 0
	else:
		population = POPULATIONS[lang_code]
	# print("'{}':{}, ".format(lang_code, population))
	for phoneme in inventory:
		phonemes[phoneme] = phonemes.get(phoneme,0) + population
	total_pop += population

num_who_must_learn = [0]*(len(DJASTIZ)+1) #find the number of humans who must learn _x_ new phonemes to speak Djastiz
avg_num_to_learn = 0
specific_needs = {}
for lang_code, inventory in inventories.items():
	num_to_learn = 0
	for phoneme in DJASTIZ:
		if phoneme+':' not in inventory:
			num_to_learn += 1
			if POPULATIONS[lang_code]:
				specific_needs[lang_code] = specific_needs.get(lang_code, []) + [phoneme]
	num_who_must_learn[num_to_learn] += POPULATIONS[lang_code]
	avg_num_to_learn += num_to_learn*POPULATIONS[lang_code]/total_pop

for i, num in enumerate(num_who_must_learn):
	if num == 0:
		break
	elif i == 0:
		print('{:.2f}% of humans can pronounce Djastiz words natively.'.format(num/total_pop*100))
	else:
		print('{:.2f}% of humans must learn {} new phonem{} to pronounce Djastiz words.'.format(num/total_pop*100, i, 'es' if i>1 else 'e'))
print('The average human must learn {:.1f} phonemes to pronounce Djastiz words.'.format(avg_num_to_learn))

print()

for lang_code, missing_phns in sorted(specific_needs.items(), key=lambda it:POPULATIONS[it[0]], reverse=True)[:10]:
	phn_list = ", ".join(missing_phns[:-1])+", or "+missing_phns[-1] if len(missing_phns)>1 else missing_phns[0]
	print("{} doesn't have {}".format(language_names[lang_code], phn_list))

print()

for phoneme in sorted(phonemes.keys(), key=lambda p:-phonemes[p]):
	print("{}\t{:.2f}%".format(phoneme, 100*phonemes[phoneme]/total_pop))

plt.pie(num_who_must_learn, labels=["Native"]+["{} phn.".format(i) for i in range(1,len(DJASTIZ)+1)], startangle=-90)
plt.axis('equal')
plt.show()

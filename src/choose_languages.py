#choose_languages.py

DEPTH = 2 #how many levels down to categorise
GROUP_CUTOFF = 2/3
LANGG_CUTOFF = 1/2

GOOGLE_TRANSLATE = { #ideally update this when they add more languages
		'afr', 'sqi', 'amh', 'ara', 'hye', 'aze', 'baq', 'bel', 'ben', 'bos', 'bul',
		'cat', 'ceb', 'nya', 'cmn', 'cos', 'hrv', 'ces', 'dan', 'nld', 'eng', 'epo',
		'est', 'fil', 'fin', 'fra', 'fry', 'glg', 'kat', 'deu', 'ell', 'guj', 'hat',
		'hau', 'haw', 'heb', 'hin', 'hmn', 'hun', 'isl', 'ibo', 'ind', 'gle', 'ita',
		'jpn', 'jav', 'kan', 'kaz', 'khm', 'kor', 'kur', 'kir', 'lao', 'lat', 'lvs',
		'lit', 'ltz', 'mkd', 'mlg', 'msa', 'mal', 'mlt', 'mri', 'mar', 'mon', 'mya',
		'nep', 'nob', 'pus', 'fas', 'pol', 'por', 'pan', 'ron', 'rus', 'smo', 'sco',
		'srp', 'sot', 'sna', 'snd', 'sin', 'slk', 'slv', 'som', 'spa', 'sun', 'swa',
		'swe', 'tgk', 'tam', 'tel', 'tha', 'tur', 'ukr', 'urd', 'uzb', 'vie', 'cym',
		'xho', 'yid', 'yor', 'zul'}

import pickle


with open('..\\data\\ethnologue.pkl', 'rb') as f:
	languages = pickle.load(f)

group_pops = {}
groups = {}
tot_pop = 0
for lang_code in languages:
	lang_name, population, classification, relatives = languages[lang_code]
	if classification == ['Macrolanguage']: #if it is a macrolanguage
		continue #don't count macrolanguages
	elif isinstance(relatives, str) and len(classification) <= DEPTH: #if it is _part_ of a macrolanguage and is shallow enough
		group_name = "/".join(classification) #that macrolanguage is its group
	else: #if it's just a normal language
		group_name = "/".join((classification+[lang_name])[:DEPTH])
	group_pops[group_name] = group_pops.get(group_name, 0) + population
	groups[group_name] = groups.get(group_name, []) + [lang_code]
	tot_pop += population
print("{} humans accounted".format(tot_pop))
tot_pop = 7000000000

cum_pop_0 = 0
useful_groups = []
for group_name, size in sorted(group_pops.items(), key=lambda item: item[1], reverse=True):
	cum_pop_0 += group_pops[group_name]
	print(size, group_name)
	useful_groups.append(group_name)
	if cum_pop_0 >= tot_pop*GROUP_CUTOFF:
		break

source_languages = {}
net_representation = 0
for group_name in useful_groups:
	short_group_name = group_name[group_name.rfind('/')+1:]
	if short_group_name in ['Southern','North','East','West','Central']:
		short_group_name += ' ' + group_name.split('/')[-2] #come up with a nice short name for this group
	num_lang = 0
	cum_pop_1 = 0
	for lang_code in sorted(groups[group_name], key=lambda lc: languages[lc][1], reverse=True):
		if languages[lang_code][3] in source_languages: #if we have already added this macrolanguage
			# print("Skip {} ({}) because we already have {}".format(languages[lang_code][0], lang_code, languages[lang_code][3]))
			continue #don't double-count
		elif languages[lang_code][3] in GOOGLE_TRANSLATE: #if Google Translate claims to have this macrolanguage
			# print("Note, {} ({}) is not in GT, but '{}' is.".format(languages[lang_code][0], lang_code, languages[lang_code][3]))
			lang_code = languages[lang_code][3] #I'm banking on the fact that its vocabulary will be recognisable to all
		elif lang_code not in GOOGLE_TRANSLATE: #if we just don't have this language
			# print("Aw, GT doesn't have {} ({}).".format(languages[lang_code][0], lang_code))
			continue #I can't use it, unfortunately
		lang_name, population, classification, relatives = languages[lang_code]
		num_lang += 1 #we have another language. Yay.
		cum_pop_1 += population
		source_languages[lang_code] = (None, population, short_group_name) #mark this language to be added, though we have no number yet
		net_representation += population #note the represented population
		if cum_pop_1 >= group_pops[group_name]*LANGG_CUTOFF:
			break
	if num_lang == 0:
		raise ValueError("Google Translate doesn't have ANY of the languages in the group '{}'! Your method is fundamentally flawed.".format(group_name))
	group_portion = group_pops[group_name]/cum_pop_0
	for lang_code in source_languages:
		if source_languages[lang_code][0] is None:
			lang_portion = source_languages[lang_code][1]/cum_pop_1*100
			source_languages[lang_code] = (group_portion*lang_portion, *source_languages[lang_code][1:])
	print("{} languages from the family {}, representing {:.2f}% of native speakers".format(num_lang, group_name, cum_pop_1/group_pops[group_name]*100))

print("\nCastis will have {} source languages, representing {:.2f}-{:.2f}% of humans:".format(len(source_languages), net_representation/tot_pop*100, cum_pop_0/tot_pop*100))
for lang_code in sorted(source_languages, key=lambda lc:source_languages[lc], reverse=True):
	print("{0:.2f}% - {3} ({1}, {2})".format(*source_languages[lang_code], languages[lang_code][0]))

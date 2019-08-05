# How to Speak Oltilip

This is the language specification for Oltilip, an international auxiliary language. Here you will find all of the information needed to learn and speak Oltilip, as well as some information about how Oltilip came to be. This document assumes that you speak English. If you're reading this, that seems like a pretty safe assumption.

## Disclaimer

Please do not actually learn this language. I created Oltilip to satisfy my personal desire for a language that _I_ thought was optimal. I publish it such that those who are interested can see my ideas and potentially gain something from them. However, were I to actually push it as a contender for the second language of humanity, it would be a waste of my time at best and another divisive factor in the already splintered auxlang community at worst. Therefore, I beseech you that if you want to support the idea of an international auxiliary language by learning one and communicating with it, I encourage you to look into [Elefen](elefen.org) or [Neo Patwa](http://patwa.pbworks.com/w/page/14800479/FrontPage) instead, as those are the two auxlangs other than my own that I currently favor most.

With that out of the way, let's get onto the language!

## Phonology and orthography

### Alphabet

Before you read any further, you'll need to know how to read, say, and write these words. Luckily, this is extremely easy. Oltilip uses only the seventeen sounds that are most common globally, each of which comes with a considerable amount of allowable variation. For example, while "pace", "base", and "Bess" sound different to most English speakers, all are acceptable pronunciations for Oltilip "pes", which means "fish". The writing system is a simple Latin-derived alphabet with one letter for every sound. It's so simple that a wise man can acquaint himself with it before the hour is over; even a stupid man can learn it in the space of two days.

| Name | Symbol | Alt. Symbols | Sound (English) | Sound ([IPA](1)) | Alt. Sounds ([IPA](1)| Inverse |
|------|--------|--------------|-----------------|------------|-------------|---------|
|   e  |   e    |    Є         |  *e*gg, fr*ay*  |     ɛ      |  e\~ɛ, ej   |    o    |
|   a  |   a    |    Ƌ, ɑ, α   | t*a*co, h*a*ck  |     a      |    a\~ɑ     |    a    |
|   o  |   o    |    O, σ      | *oa*t, *o*rgan  |     ɔ      |  o\~ɔ, ow   |    e    |
|   i  |   i    |    I, ι      |*ea*t, scr*ee*ch |     i      |    i\~ɪ     |    u    |
|   u  |   u    |    U, v      | fr*ui*t, *oo*ze |     u      |    u\~ʊ     |    i    |
|  yo  |   y    |    Y         |*y*ogurt, *y*ell |     j      |   j, ʲ, i   |    we   |
|  la  |   l    |    L         | *l*ime, fa*ll*  |     l      |    l\~r     |    ta   |
|  we  |   w    |    W, ɯ      | *w*ine, q*u*iet |     w      |   w, ʷ, u   |    yo   |
|  na  |   n    |    Λ         |*n*ectar, pai*n* |     n      |   n, ŋ\~ɴ   |    ko   |
|  me  |   m    |    M         |*m*elon, screa*m*|     m      |      m      |    pe   |
|  ho  |   h    |    Һ         | *h*oney, *h*ide |     h      |   x\~h, ɦ   |    co   |
|  co  |   c    |    C         |*ch*eese, *sh*riek|   t͡ʃ      |t͡ʃ\~t͡ʂ, ʃ\~ʂ |    ho   |
|  sa  |   s    |    S         | *s*alt, hi*ss*  |     s      |      s      |    fe   |
|  fe  |   f    |    F         | *f*ish, cou*gh* |     f      |    ɸ\~f     |    sa   |
|  ko  |   k    |    K, κ      | *c*ake, *g*rab  |     k      |   k kʰ ɡ    |    na   |
|  ta  |   t    |    T, τ      |  *t*ea, *d*eep  |     t      |   t tʰ d    |    la   |
|  pe  |   p    |    P, ρ      | *p*ear, *b*urst |     p      |   p pʰ b    |    me   |

If you're a linguist, the following [IPA](1) table may prove easier to read:

|               | Labial | Coronal | Palatal | Guttural |
|:--------------|:------:|:-------:|:-------:|:--------:|
|**Plosive**    |    p   |    t    |         |    k     |
|**Fricative**  |    f   |    s    |  t͡ʃ ⟨c⟩  |    h     |
|**Nasal**      |    m   |    n    |         |          |
|**Approximant**|    w   |    l    |   j ⟨y⟩  |          |

|         | Front | Back |
|:--------|:-----:|:----:|
|**Close**|   i   |  u   |
|**Mid**  |   e   |  o   |
|**Open** |   a   |      |

The "Inverse" column is not that important; it just comes up later in the derivational morphology section. You don't have to learn that part if you don't want to.

You'll notice that most of the letters match their IPA transcriptions as well as their English counterparts. The only things of which you need to be careful are ⟨j⟩, ⟨c⟩, and the vowels. There's a handy alphabet song in the main repository to help you remember them all if you like.

Note that while all of these symbols come from the Latin alphabet, the Latin alphabet is _not_ the Oltilip alphabet. The Oltilip alphabet does not include ⟨b⟩, ⟨d⟩, ⟨g⟩, ⟨q⟩, ⟨r⟩, ⟨v⟩, ⟨x⟩, ⟨y⟩, ⟨z⟩, or any capital letters. _Some_ capital Latin letters are acceptable substitutes for their lowercase forms, as indicated by the alternate symbols column, but these are merely to allow stylistic variation, and carry no meaning different from their lowercase counterparts. Furthermore, note that unlisted capital letters are too different to be easily readable by Oltilip-speakers who are unfamiliar with the entire Latin alphabet, and thus should not ever be used.

[1]: http://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/ "International Phonetic Alphabet"

### Punctuation

In addition to this subset of Latin letters, a subset of other Latin symbols may be used with Oltilip to aid parsing. None of these are strictly required, but it is important to understand what they mean in case you come across them in Oltilip texts.

| Name | Symbol | Usage | Example |
|------|--------|-------|---------|
| katilon         |        | Separates words or clusters of digits in long numbers
| pelapas         | '      | Precedes a _loanword_
| tyen            | .      | Follows the last word of a sentence or the ones digit of floating point numbers
| tapamila        | ,      | Follows the last word before a brief pause
| enefwesak kiles | (      | Precedes the first word of an inset sidenote
| enefwesak nules | )      | Follows the last word of an inset sidenote
| fulopas         | \~     | Denotes a range between two values
| men             | -      | Denotes the subtraction of two values or stands for the word "men" ("negative")
| aw              | +      | Denotes addition of two values or stands for the word "aw" ("and")
| funtanyopas     | /      | Stands for the word "pel" ("divided by")
| nul             | 0      | Stands for the word "nul" ("zero")
| kan             | 1      | Stands for the word "kan" ("one")
| tos             | 2      | Stands for the word "tos" ("two")
| san             | 3      | Stands for the word "san" ("three")
| fol             | 4      | Stands for the word "fol" ("four")
| lim             | 5      | Stands for the word "lim" ("five")
| cah             | 6      | Stands for the word "cah" ("six")
| pit             | 7      | Stands for the word "pit" ("seven")
| hat             | 8      | Stands for the word "hat" ("eight")
| mes             | 9      | Stands for the word "mes" ("nine")
| tes             | A      | Stands for the word "tes" ("ten")
| tup             | B      | Stands for the word "tup" ("eleven")
| set             | C      | Stands for the word "set" ("twelve")
| fak             | D      | Stands for the word "fak" ("thirteen")
| lef             | E      | Stands for the word "lef" ("fourteen")
| nak             | F      | Stands for the word "nak" ("fifteen")

### Extensions

Finally, there are twenty-seven more letters that may be used for transcribing foreign names in Oltilip. Guidelines on when to do this can be found in section ?. They fill out the simplified IPA tables below.

|                          | Labial | Alveolar | Postalveolar\~Retroflex | Palatal | Velar&tilde;Uvular | Pharangeal&tilde;Glottal |
|--------------------------|--------|----------|--------------|---------|-------|---------|
|**Nasal**                 | m      | n        | n     | ŋy      | ŋ     |        |
|**Plosive**               | p b    | t d      | t d   | ky gy   | k g   | ʔ      |
|**Affricate**             | pf bv  | ts dz    | tʃ dʒ | kxy gʀy | kx gʀ | ʔh     |
|**Fricative**             | f v    | s z      | ʃ ʒ   | xy ʀy   | x ʀ   | h ʕ    |
|**Lateral fricative**     | lf lv  | lh lʒ    | lh lʒ | lx lʀ   | lx lʀ |        |
|**Approximant**           | w      | ɹ        | ɹ     | y       | ɯ     | ʕ      |
|**Lateral approximant**   | lw     | l        | l     | ly      | lɯ    |        |
|**Tap/Trill**             | ʙ      | r        | r     |         | ʀ     |        |
|**Click/Implosive**       | \|     | \|       | \|    | \|      | \|    |        |
|**Secondary articulation**| ◌w     | ◌ɹ       | ◌ɹ    | ◌y      | ◌ʀ    | ◌ʔ     |

|             | Front | Central | Back |
|-------------|-------|---------|------|
|**Semivowel**| y ɥ   | y w     | ɯ w  |
|**Close**    | i ɥ   | ɨ ʉ     | ɯ u  |
|**Mid**      | e ø   | ə ə     | ɤ o  |
|**Open**     | a ɒ   | a ɒ     | a ɒ  |

|                   |    |          |   |
|-------------------|----|----------|---|
|**Voiceless**      | nh |**Stress**| ˈ |
|**Aspirated**      | th |**Long**  | əə|
|**Rhoticity**      | əɹ |**High**  | ˥ |
|**Nasalised**      | eŋ |**Mid**   | ˧ |
|**Nasal release**  | dn |**Low**   | ˩ |
|**Lateral release**| dl |

## Vocabulary

Oltilip has 426 basic roots, drawn from Chinese, Italic, Germanic, Indo-Iranian, Atlantic-Congo, Malayo-Polynesian, Esperanto, and onomotopoetic lexicons. The source languages were selected and weighted in order to give the most mnemonic value to the greatest number of people. These roots fall into five parts of speech—nouns, verbs, numerals, specifiers, and sentence particles—which will be explained in the next section. While these root words cover many concepts, with only 426, there are inevitably many lexical gaps and ambiguities. These are filled with Oltilip's powerful, multifaceted morphological derivation system. New words are derived in three main ways: _compounds_, _affixen_, and _loans_.

### Compound words

The most intuitive way to form a new word in Oltilip is with a simple compound. This involves combining two or more existing words to form a new one. It takes the part of speech of the second, and represents something between the meanings of both. For example, "pahopoltilum", meaning "underwear", is derived from "paho", meaning "to be under", and "poltilum", meaning "clothing".

### Affixen

### Loanwords

For words that describe deeply technical concepts like deoxyribonucleic acid, cultural concepts like ahupua&#8216;a, or a combination of the two like the oriental ladyfern, a class of word that is neither root nor  preferred method of denotation is the loanword, a word taken directly from other languages. Loanwords in Musical Djastiz use Modern Djastiz's phonology. The word should be taken from a language that has regional or historical ties to the concept. For example, a specific species of fox should have a word loaned from a language sung in a region where that fox is or was found. Gramatically, loanwords are equivalent to nouns. Note that this is also the preferred method for generating toponyms, even when the country in question uses a compound word in the native language. For example, "'doyc" means "German"

Like the compound words, the set of documented loanwords is not complete. They are meant to encompass the highly specific concepts that Djastiz cannot describe on its own, and thus to attempt to recond all of them in a Djastiz dictionary would be impossible. Instead, I have included some useful examples of loanwords in [loanword.csv](dictionary/loanword.csv).

## Grammar

The grammar of Chastisun is designed to be as simple as possible while enabling speakers to be either simple and vague or exact and precise at will. It can be summed up in the following Backus-Nur form.
         sentence ::= \[sentence-particle\] postposit-phrase\* \[verb-phrase postposit-phrase\*\]
 postposit-phrase ::= (noun-phrase | sentence) postposition
      noun-phrase ::= \[specifier\] (noun | pronoun | number | relative-phrase | noun-phrase)\*
      verb-phrase ::= verb+
  relative-phrase ::= postposit-phrase\* \[verb-phrase postpos-phrase\*\] \["l" postposition\]
           number ::= \[number "imal"\] \[\[neg\] digit+\] \["ljo" number\]
         X-phrase ::= \[qualifier | number\] \["bo"\] X-phrase ("ha" X-phrase)\+

If you don't know what any of that means, don't worry. Each type of phrase is described more explicitly in the following sections.

This may seem confusing to those more familiar with word-order-based systems, but the reliance on postpositions alone decreases the number of patterns and greatly simplifies the grammar overall. It can also be considered equivalent to many case systems.

### Sentence particles

A tense marker gives the general purpose of a sentence. It is the first thing in the sentence. There are ten tense markers, and each creates a fundamentally different kind of communication.
- `ȅ` is the _declarative_ tense marker. It precedes a sentence that conveys information. The event or fact described in a declarative sentence is true, according to the singer.
- `ȁ` is the _interrogative_ tense marker. It precedes a sentence that requests information. An interrogative sentence usually contains the word `pèm` at least once, though the position of `pèm` can also be implied. In either case, `pèm` represents a piece of information missing from the sentence that the singer would like to know.
- `jȕ` is the _imperative_ tense marker. It precedes a sentence that requests action. An imperative sentence describes an event or action that the singer wants to happen.
- `pā` is a bit more complicated. It does not create sentences at all, but rather _noun clauses_. These will be discussed in [&#167;2.3](#noun-phrases).
- `lȕ` is the _bureaucratic_ tense marker. It behaves similarly to `ȅ`, specifically in contexts where saying a sentence causes it to be true. Bureaucratic sentences are especially useful for proclamations, definitions, and assumptions in mathematical proofs.
- `mùről` behaves exactly like `jȕ`, but frames the request as less mandatory and more polite. The frequency with which one uses `mùről` versus `jȕ` completely depends on the society, and since no society actually sings Djastiz, I have no idea how useful this word is.
- `jȍ` is the _salutary_ tense marker. It is used to construct basic greetings. `jȍ` is a _simple tense marker_, which means that it can be used with simpler sentence patters. These will be discussed further in [&#167;2.7](#special-words).
- `lȍ` is the _antisalutory_ tense marker. It is used to construct basic parting statements and, like `lȍ`, is simple.
- `lȅ` is the _neutral exclamatory_ tense marker and is used to express general awe or surprise at something. It is also a simple tense marker.
- `lȁ` is the _positive exclamatory_ tense marker and is used to express general happiness or approval. It is also a simple tense marker.
- `pȕ` is the _negative exclamatory_ tense marker, which expresses general unhappiness or disapproval. It is also a simple tense marker.

In addition to labelling the type of sentence, the tense marker indicates the start of the sentence. The sentence ends with the predicate, which we will discuss briefly. Between these tokens lies the meat of the sentence: postpositional phrases.

### Postpositional phrases

Every postpositional phrase describes one aspect of the event described by the sentence, and comprises two parts: the _complement_, which is a noun phrase, and the _postposition_, which is drawn from the following list of fifteen. The postposition specifies what aspect of the sentence is being described, and the complement describes that aspect. These postpositional phrases may occur in any order. There are three classes of postpositional phrase.

_Argumentative postpositions_ also may only be included once per sentence, if that. Each one may or may not be _applicable_ based on the predicate. If an argumentative preposition is applicable, it may be included in the sentence, but does not need to be if its complement is implied. A proper Djastiz dictionary would list the applicable argumentative prepositions for every verb in the language, as well as their precise meanings in each case. Let's be real, though. There's no way I'm going to do that. Instead, I'll leave it up to the singers' discretion when each preposition is applicable. In general:
- `ó` denotes the _subject_ of the action, the agent that initializes and/or carries out the action (e.g. the planner of `ojȅl`). `ó` is almost always applicable.
- `ē` denotes the _direct object_, the object on which the subject acts or to which the action refers (e.g. the food of `molȁm`). `ē` is never applicable when `ó` is not.
- `à` denotes the _indirect object_ of the action, the concept that the subject indirectly affects or references (e.g. the origin of `le̋l`). It often functions in tandem with `ē` (e.g. the old and new values in `jaȕl`). `à` is never applicable when `ē` is not.

_Adjunctive prepositions_, by contrast, are always applicable, and can be used multiple times in one sentence if being used in different contexts (e.g. using `shug` once for the location in virtual space and again for the location in real space). They denote, in a sense, the "where, when, why, how" of the sentence.
- `ù` denotes the extent or quantity of the action. This can be a number or another noun to be compared against.
- `jé` denotes the location of the action in physical space.
- `ùm` denotes the date and/or time of the action.
- `lō` denotes the cause of the action.
- `jē` denotes the purpose of the action.
- `rē` denotes the context of the action, very much like "regarding ..." or "in the ... sense" in English.
- `rol` denotes the tool or medium of the action.
- `jol` denotes whether the action happened (generally only used in interrogative sentences, since it's universally implied to be `ű`).
- `pū` denotes the hypothetical conditions surrounding the action (very similar to English's "if").
- `mó` denotes the method of the action, usually a noun clause that happens with or before and is necessary for the main action.
- `mom` denotes the manner of the action, often a noun clause that describes the action.
- `jó` denotes the adressee of the sentence, if it is unclear or requires emphasis.
- `ōm` denotes the source of the information, inquiry, or command, if it is not the singer or requires emphasis.

### Predicates

There is not much to say about the predicate. The last thing in the sentence, it comprises a single verb. This verb describes the most fundamental meaning of the sentence beyond the tense: what kind of action or event is being described. Unlike in Modern Djastiz, in Musical Djastiz, the verb is mandatory.

### Noun phrases

Noun phrases are the primary building blocks with which one describes complex concepts. There are four ways to construct these.

The first, and by far the simplest, is a _noun_. There are hundreds from which to choose! Each one describes an instance or instances of a concept or class of objects. Often, however, the concept one wants will not be found in the list.

The next method is the prependix of a _qualifier_ to a noun phrase. There are six qualifiers, which primarily manipulate _sets_ (a set is just a noun phrase that describes a group of things) and logical operations.
- `él` creates a phrase that refers to anything but the meaning of the following noun phrase.
- `ló` creates a phrase that refers to all possible instances of the following concept together in a set.
- `mum` creates a phrase that refers to a single unspecified element of the following set or instance of the following concept. The sentence is true for one element of the set.
- `ré` creates a phrase that refers to an unspecified subset of the following set or unspecified instances of the following concept. The sentence is true for part of the set.
- `ūl` creates a phrase that refers to every element of the following set or instance of the following concept individually. The sentence is true for each element of the set.
- `ōl` emphasizes a particularly important or surprising noun phrase.

The third method is the appendix of a _modifier_. Modifiers are attached to the ends of noun phrases to create new noun phrases. There are two types of modifier, each of which has its own quirks, so they will be discussed at length in [&#167;2.4](#modifiers).

The fourth and perhaps most complicated method is a gerund. A noun clause comprises `pā` followed by a list of postpositional phrases and a verb. Noun clauses appear at first to be sentences with `pā` as their punctuation marker. However, do not be misled. These are nouns that refer to the meaning of the sentence they appear to be. They are commonly used with verbs such as `jaȕl` and `lȕm`.

The final method is _pronouns_, which function exactly as nouns do, but with meanings derived exclusively from context. There are nine of them.
- `ō` is the simplest pronoun. It carries no information, and acts as more of a placeholder than anything else.
- `òm` stands in for any noun that has been recently mentioned.
- `úl` refers to the singer or writer.
- `pò` refers to the listener or reader.
- `jul` refers to an agent other than the singer or listener.
- `jal` refers to the singer and others.
- `mè` refers to the listener and others.
- `rè` refers to the singer and the listener.
- `mā` refers to the singer, listener, and others.

Noun phrases can also technically be created with _conjunctions_, but then, so can prepositional phrases and modifiers and predicates. I'll explain those in a different paragraph.

### Numbers

number := (number <rad>)? <neg>? (digit)* (<paw> number)?

### Tips and tricks

That's all of the official grammar. You may find it rather short. "Where are the tenses, the passives, the participles?" you ask. While these do not exist explicitly in Oltilip, they can be expressed using preexisting structures. Therefore, while their inclusion here is not strictly necessary, I will explain them so that everyone understands best practices for such situations without needing derive them themselves.

Tenses are simple. If it is important to a sentence whether it happened in the past, present, or future, the dative postposition `eh` can be used with the appropriate word.

Passives are somewhat nonexistent in Launtoklian, since you can just switch the order anyway.

Participles in Launtoklian are represented with relative clauses.

Adverbs come in two flavours: things like "quickly" and things like "hopefully".

Directionals

Conjunctions

Other postpositions

Adjective derivations

The verb "to have"

The verb "to need"

## Flag

# Appendices

## Dictionary


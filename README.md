# Djastiz

So, you want to speak a better and more succinct version of Olde Djastiz. How do you do that? By speaking Modern Djastiz\*, that's how! What's Modern Djastiz? It's a high-level language optimised for efficiency that I invented. Here's how it works.

## Writing and pronunciation

Before you read any further, you'll need to know how to read, say, and write these words. Djastiz has 28 letters: three nasals, three unvoiced plosives, three voiced plosives, six unvoiced fricatives, six voiced fricatives, and seven vowels/approximants. It is written using a phonetic alphabet, which reads top-to-bottom, then left-to-right. The letters are as follows.
- [`nga`](writing/nga.svg) is Romanized "ng" and pronounced /&#627;/ in the [IPA][1].
- [`ne`](writing/ne.svg) is Romanized "n" and pronounced /n/ in the [IPA][1].
- [`mo`](writing/mo.svg) is Romanized "m" and pronounced /m/ in the [IPA][1].
- [`ko`](writing/ko.svg) is Romanized "k" and pronounced /k/ in the [IPA][1].
- [`tu`](writing/tu.svg) is Romanized "t" and pronounced /t/ or /t&#810;/ in the [IPA][1].
- [`pa`](writing/pa.svg) is Romanized "p" and pronounced /p/ in the [IPA][1].
- [`gr`](writing/gr.svg) is Romanized "g" and pronounced /g/ in the [IPA][1].
- [`de`](writing/de.svg) is Romanized "d" and pronounced /d/ or /d&#810;/ in the [IPA][1].
- [`bi`](writing/bi.svg) is Romanized "b" and pronounced /b/ in the [IPA][1].
- [`hu`](writing/hu.svg) is Romanized "h" and pronounced /x/ in the [IPA][1].
- [`thr`](writing/thr.svg) is Romanized "th" and pronounced /&theta;/ in the [IPA][1].
- [`fe`](writing/fe.svg) is Romanized "f" and pronounced /&#632;/ in the [IPA][1].
- [`yi`](writing/yi.svg) is Romanized "y" and pronounced /&#611;/ in the [IPA][1].
- [`dha`](writing/dha.svg) is Romanized "dh" and pronounced /&eth;/ in the [IPA][1].
- [`vo`](writing/vo.svg) is Romanized "v" and pronounced /&beta;/ in the [IPA][1].
- [`she`](writing/she.svg) is Romanized "sh" and pronounced /&#642;/ in the [IPA][1].
- [`ssa`](writing/ssa.svg) is Romanized "ss" and pronounced /&#643;/ in the [IPA][1].
- [`si`](writing/si.svg) is Romanized "s" and pronounced /s/ in the [IPA][1].
- [`zhr`](writing/zhr.svg) is Romanized "zh" and pronounced /&#656;/ in the [IPA][1].
- [`jo`](writing/jo.svg) is Romanized "j" and pronounced /&#658;/ in the [IPA][1].
- [`zu`](writing/zu.svg) is Romanized "z" and pronounced /z/ in the [IPA][1].
- [`rm`](writing/rm.svg) is Romanized "r" and pronounced /&#633;&#809;/ or /&#633;/ in the [IPA][1].
- [`iz`](writing/iz.svg) is Romanized "i" and pronounced /i/ or /j/ in the [IPA][1].
- [`uss`](writing/uss.svg) is Romanized "u" and pronounced /u/ or /w/ in the [IPA][1].
- [`ar`](writing/ar.svg) is Romanized "a" and pronounced /a/ or /&#600;/ in the [IPA][1].
- [`ey`](writing/ey.svg) is Romanized "e" and pronounced /e/ or /&#603;/ in the [IPA][1].
- [`ou`](writing/ou.svg) is Romanized "o" and pronounced /o/ in the [IPA][1].
- [`al`](writing/al.svg) is Romanized "l" and pronounced /l&#809;/ or /l/ in the [IPA][1].

If a single letter has multiple pronounciations, either can be used without affecting the meaning. Syllables are often built such that one pronounciation is easier to use than the other. Clusters of latin consonants that can be interpreted as a single phoneme should always be interpreted as a single phoneme; in the rare case that two adjacent romanised phonemes would normally appear to be a diagraph, for example a `ne` immediately preceding a `gr`, an apostraphe shall be used to prevent the confuson of this consonant cluster with a `nga`: `n'g`.
The actual Djastiz character for each letter in svg format can be found in the "writing" folder of this repository. While there are no punctuation glyphs in Djastiz, words are separated by spaces that occupy the same vertical space as a letter. In polysyllabic words, the stress is placed on the second syllable.

[1]: http://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/ "International Phonetic Alphabet"

## Grammar

The grammar of Modern Djastiz is designed to have as few rules as possible while remaining syllable-efficient and consise. The result is a language that is admittedly somewhat challenging to learn, but very easy to use once you know it. At least, I assume. I'll have more conclusive data once my child learns English. Anyway, on with the grammar! Each Djastiz sentence has several basic parts, the first of which is the _tense marker_.

### Tense markers

A tense marker gives the general purpose of a sentence. If included, it precedes the sequence of _postpositional phrases_ that compose the rest of the sentence. If omitted, as it often in the first sentence in a phrase, it is implied, usually as `dhi`. There are ten tense markers, and each creates a fundamentally different kind of communication.
- `dhi` is the _declarative_ tense marker. It precedes a sentence that conveys information. The event or fact described in a declarative sentence is true, according to the speaker.
- `ung` is the _interrogative_ tense marker. It precedes a sentence that requests information. An interrogative sentence usually contains the word `l` at least once, though the position of `l` can also be implied. In either case, `l` represents a piece of information missing from the sentence that the speaker would like to know.
- `bu` is the _imperative_ tense marker. It precedes a sentence that requests action. An imperative sentence describes an event or action that the speaker wants to happen.
- `e` is a bit more complicated. It does not create sentences at all, but rather _noun clauses_. These will be discussed in &#167;2.3.
- `yidh` is the _bureaucratic_ tense marker. It behaves similarly to `dhu`, specifically in contexts where saying a sentence causes it to be true. Bureaucratic sentences are especially useful for proclamations, definitions, and assumptions in mathematical proofs.
- `vub` behaves exactly like `bu`, but frames the request as less mandatory and more polite. The frequency with which one uses `vub` versus `bu` completely depends on the society, and since no society actually speaks Djastiz, I have no idea how useful this word is.
- `oth` is the _salutary_ tense marker. It is used to construct basic greetings. `oth` is a _simple tense marker_, which means that it can be used with simpler sentence patters. These will be discussed further in &#167;.
- `thu` is the _antisalutory_ tense marker. It is used to construct basic parting statements and, like `oth`, is simple.
- `ja` is the _exclamatory_ tense marker and is used to express general happiness or approval. It is also a simple tense marker.
- `oj` is the _antiexclamatory_ tense marker, which expresses general unhappiness or disapproval. It is also a simple tense marker.

In addition to labelling the type of sentence, the tense marker indicates the start of the sentence. The sentence is ended with the punctuation marker of the next sentence or with the silence after a person stops talking. Between these tokens lies the meat of the sentence: the postpositional phrases.

### Postpositional phrases

Every postpositional phrase describes one aspect of the event described by the sentence, and comprises two parts: the _complement_, which is a noun phrase, and the _postposition_, which is drawn from the following list of fifteen. The postposition specifies what aspect of the sentence is being described, and the complement describes that aspect. These postpositional phrases may occur in any order. There are three classes of postposition.

The _predicate_ acts as a postpositional phrase even though it does not actually have a postposition. A sentence can have at most one predicate, which is a single _[verb](dictionary/verb.csv)_ placed among the other postpositional phrases. It describes the most fundamental meaning of the sentence beyond the tense: what kind of action or event is being described.

_Argumentative postpositions_ also may only be included once per sentence, if that. Each one may or may not be _applicable_ based on the predicate. If an argumentative preposition is applicable, it may be included in the sentence, but does not need to be if its complement is implied. A proper Djastiz dictionary would list the applicable argumentative prepositions for every verb in the language, as well as their precise meanings in each case. Let's be real, though. There's no way I'm going to do that. Instead, I'll leave it up to the speakers' discretion when each preposition is applicable. In general:
- `r` denotes the _subject_ of the action, the agent that initializes and/or carries out the action (e.g. the planner of `rih`). `r` is almost always applicable.
- `u` denotes the _direct object_, the object on which the subject acts or to which the action refers (e.g. the food of `ukiaj`). `u` is never applicable when `r` is not.
- `i` denotes the _indirect object_ of the action, the concept that the subject indirectly affects or references (e.g. the order of `shaid`). It often functions in tandem with `iu` (e.g. the old and new values in `ry`). `i` is never applicable when `u` is not.

_Adjunctive prepositions_, by contrast, are always applicable, and can be used multiple times in one sentence if being used in different contexts (e.g. using `shug` once for the location in virtual space and again for the location in real space). They denote, in a sense, the "where, when, why, how" of the sentence.
- `ia` denotes the extent or quantity of the action. This can be a number or another noun to be compared against.
- `ep` denotes the location of the action in physical space.
- `os` denotes the date and/or time of the action.
- `uj` denotes the cause of the action.
- `ue` denotes the purpose of the action.
- `rk` denotes the context of the action, very much like "regarding ..." or "in the ... sense" in English.
- `or` denotes the method of the action, usually a noun clause that happened with or before the initial action.
- `im` denotes the tool or medium of the action.
- `iy` denotes whether the action happened (generally only used in interrogative sentences, since it's universally implied to be `kaup`).
- `er` denotes the hypothetical conditions surrounding the action (very similar to English's "if").
- `au` denotes the manner of the action, often a noun clause that describes the action.
- `eng` denotes the adressee of the sentence, if it is unclear or requires emphasis.

### Noun phrases

Noun phrases are the primary building blocks with which one describes complex concepts. There are four primary ways to construct these.

The first, and by far the simplest, is a _[noun](dictionary/noun.csv)_. There are hundreds from which to choose! Each one describes an instance or instances of a concept or class of objects. Often, however, the concept one wants will not be found in the list.

The next method is the prependix of a _qualifier_ to a noun phrase. There are six qualifiers, which primarily manipulate _sets_ (a set is just a noun phrase that describes a group of things) and logical operations.
- `be` creates a phrase that refers to anything but the meaning of the following noun phrase.
- `io` creates a phrase that refers to all possible instances of the following concept together in a set.
- `dhe` creates a phrase that refers to a single unspecified element of the following set or instance of the following concept. The sentence is true for one element of the set.
- `hi` creates a phrase that refers to an unspecified subset of the following set or unspecified instances of the following concept. The sentence is true for part of the set.
- `vu` creates a phrase that refers to every element of the following set or every instance of the following concept individually. The sentence is true for every element of the set.
- `se` emphasizes a particularly important or surprising noun phrase.

The third method is the appendix of a _modifier_. Modifiers are attached to the ends of noun phrases to create new noun phrases. There are two types of modifier, each of which has its own quirks, so they will be discussed at length in &#167;2.?.

The fourth and perhaps most complicated method is a noun clause. A noun clause comprises `e` followed by a list of postpositional phrases. Noun clauses appear at first to be sentences with `e` as their punctuation marker. However, do not be misled. These are nouns that refer to the meaning of the sentence they appear to be. They are commonly used with verbs such as `ij` and `ur`.

The final method is _pronouns_, which function exactly as nouns do, but with meanings derived exclusively from context. There are five of them.
- `f` is the simplest pronoun. It carries no information, and acts as more of a placeholder than anything else.
- `dh` stands in for any noun that has been recently mentioned.
- `sh` refers to the speaker or writer.
- `k` refers to the listener or reader.
- `m` refers to an agent other than the speaker or listener.
- `shm` refers to the speaker and others.
- `mk` refers to the listener and others.
- `ksh` refers to the speaker and the listener.
- `kshm` refers to the speaker, listener, and others.

Noun phrases can also technically be created with _conjunctions_, but then, so can prepositional phrases and modifiers. I'll explain those in a different paragraph.

### Modifiers

Modifiers are great ways to expand and enhance the meanings of nouns. There two types of modifiers. The simpler one is the _noun modifier_.

A noun modifier has two parts: a _fastener_ and a noun phrase. The fastener uses the following noun phrase to modify the preceding noun phrase in a specific manner, depending on the fastener. There are five fasteners that each represent a different method of modifying a noun.
- `ji` denotes the specific variety or attributes of the preceding noun phrase.
- `ir` specifies the amount, degree, or number of the preceding noun phrase.
- `o` indicates the specific instance of the preceding noun phrase.
- `va` draws eqaulity between the preceding and following noun phrases without really changing the meaning of the sentence. It is especially useful for sharing names (e.g. `flrjot va Esteban`).
- `es` indicates and extracts a specific element of a set.

The more versatile modifier is the _relative clause_. Relative clauses comprise `l`, a postposition, and then a list of postpositional phrases. Again, while these resemble full sentences, they are not. A modifier clause modifies a noun phrase by placing it inside another sentence. The result is two clauses that are true together. The first is the original sentence with the modifier clause simply removed. The second is the entire modifier with `dhi` prepended and the modified noun phrase inserted for `l`. This type of modifier draws an equality between the noun phrase and itself across the two clauses. While relative clauses seems at first glance to be far more complex than noun modifiers, they are, in fact, capable of creating some of the simplest and most useful noun modifications: _simple ergative relative clauses_, the analog to adjectives in other languages, for example, `dhap l r at`; and _relative verb noun definitions_, the analog to English's "-er" and "-ee", for example, `f l u jeuth`.

### Conjunctions

The last major grammatical structure to be discussed is the conjunction. Conjunctions are a small class of diverse words that transform phrases or sets of phrases. While they share some similarities, the two pairs of conjunctions are different enough that I might as well explain each separately.

The first and most recognizably conjugative conjunctions are `ni` and `a`. When `ni` precedes a series of noun phrases separated by `a`, they said series into a single set representing all of the noun phrases combined. They translate very cleanly to "both" and "and" in English, respectively. That set can then have its meaning easily tweaked using qualifiers. For example, `dhe ni mus a thengga`.

The other pair of conjunctions may be more difficult to understand for English speakers. This is the `yr` and `ssu` construction, which functions much like the quotation mark in English. Unlike the quotation mark, however, `yr`-`ssu` constructions must be spoken aloud. Any phrase in any language between the `yr` and the `ssu` should not be interpreted as actual Djastiz grammar, but rather as a sequence of letters or sounds. The entire phrase acts as a noun and references the phrase contained within. This is most commonly used for quoting dialogue and discussing language. To indicate that a single word inside a `yr`-`ssu` construct should be interpreted literally and not as part of the quote, precede it with the word `je`, for example, `dhi ij yr tshef je l u ssu u`. To describe the word or sound `je`, escape it by preceding it with `je`. For example, `raun yr dhi ij yr tshef je je l u ssu u ssu u`.

### Gerunds

Ther exists one major deviation from the rules laid out here, which exists as more of a convinience than any kind of nececity. This is the _gerund_. A gerund is a construct of nouns and a verb that can serve as the complement to an adjunctive postposition, replacing a `f` modified by a modifier clause. When a postpositional phrase takes the form `f l P0 N0 ia N1 u V0 P0`, where `P0` is an adjunctive postposition, `N0` and `N1` are noun phrases, and `V` is a transitive verb, it can be shortened to `N0 N2 V0 P1` without changing the meaning. This works well with several verbs that take said form often. For example, `lity ir od hiai utrd ep`. Note that this construction only works this particular way for verbs to which `r` and `u`, but not `i`, are applicable, and clauses where only the postpositions `ia` and `u` are used, in that order. Word order in gerunds depends predictably but stringently on the transitivity of the verb and the postpositions included. Below is a table describing how to interpret a gerund. The column header specifies the number of applicable argumentative prepositions of the verb (transitivity), the row label the number of noun phrases provided, and the cell the list of implied prepositions, in order. If a cell does not exist for a certain sentence pattern (for example, anything with a subject specified), then that pattern may not be phrased as a gerund.

|     |   0   |   1   |   2   |   3   |
|-----|-------|-------|-------|-------|
|**0**|       |       |       |       |
|**1**| `ia`  | `ia`  |  `u`  |  `u`  |
|**2**|  N/A  | `r ia`| `u ia`| `u i` |
|**3**|  N/A  |  N/A  |`r u ia`|`u i ia`|

### Special words

Most of the words discussed thus far have fallen into categories and followed simple rules. We now discuss a few of the more unique words and groups of words that do not accept labels so easily.

`oth`, `thu`, `ja`, and `oj` are the simple tense markers. Simple tense markers are used when a sentence is too common or basic to warrant a full list of prepositional phrases. Instead, one follows the marker with a single noun phrase. When using `oth`, the noun phrase represents the current occasion, and the full sentence forms a greeting or congratulation. `thu`, similary, precedes the current occasion Thus, `oth vorng` greets people during the day, `oth krismes` during Christmas, and `oth ngad` immediately after a graduation. `ja` and `oj`, on the other hand, express happiness or respect, or unhappiness or disgust, respectively, toward a noun phrase. For example, `ja iatpeuzpubuksedog` praises air conditioning, `ja hitlr` hails Hitler, and `oj k`. Simple punctuation markers can also be used with nothing following them at all. In that case, `oth` expresses a general greeting and `oj` an exclamation of general anger.

`l` is the question word, very similar to "what" in English. Rather than carrying information, like most words, `l` denotes a lack of information. `l` is used in two cases, both previously mentioned: standing in for desired information in sentences starting with `ung`, and beginning a relative clause as well as indicating the modified noun phrase's place within the clause.

Numbers can also be considered special words in that they concatenate with each other in a unique way. Quantities in Djastiz are described by a string of number words. The final quantity is obtained by summing all of the digits after applying a multiplier to each one greater than that of the next by a factor of the radix, which is ten by default. In other words, say a number in Djastiz by writing it in decimal notation and then reading off each digit in Djastiz in sequence. Extremely large and imprecise numbers can be described efficiently by dividing out a logical number of factors of the radix, and then appending the word `uo` and the number of powers divided. The decimal point is read `ho` and is placed among the digits as with standard numeral notation. Negative numbers should have `me` inserted at the beginning. Fractions can be expressed by describing the denominator as a unit. Finally, to use radices other than ten, the base plus the word `adh`. There exist enough words to easily use any radix from two to sixteen. For larger radices, the radix is typically said in base ten, though if you want, I guess you can nest them, if you need to represent 3,723 in base 0x3C for some reason. Does that sound complicated? It isn't. Some examples will probably help. `ang od`, `uf po tho od`, `flushifpo ir rh rh`, `rh adh re ngu adh uf od re`  and `ev ho od rh re uf rh zha re yu po`.

`skelf` is a bit of a meta-word. It tells the listener to ignore the previous few words spoken. This is used exclusively for error correction, so it rarely comes up in writing.

## Vocabulary

In the grammar section, we defined every word in the language save two groups: verbs and nouns. There are far too many of either to list here &ndash; hundreds upon hundreds. Instead, I will lay out the tools to interpret new verbs and nouns and create new ones when necessary.

### Verbs

As previously stated, verbs are used to create predicates. The list of all verbs is present in this repository at [verb.csv](dictionary/verb.csv). There are two main classes of verb: _dynamic_ and _stative_.

Dynamic verbs are more like the verbs an English-speaker might encounter in its own language. Each describes an action that changes with respect to time. The universe after the action occurs is typically different from the universe before.

Stative verbs tend to share more in common with English adjectives than English verbs. They indicate that the subject has some state, which may or may not change as time passes. When the state has a numeric parameter, such as the latitude in `bav`, that number can be specified by the complement of `ia`, and the reference, or zero, can be specified by the direct object. Thus, `reidien ir ho ang ia filidelfia u bav` means ".4 radians south of Philidelphia". When the state takes a non-numeric parameter, such as `thru`, the verb is a special kind of staive verb called a _copula_, and that parameter should be the object. When the state cannot be logically parametrised, it is called an _absolute_.

### Nouns

I actually have nothing more to say about nouns. They are completely intuitive and uninteresting, though I guess I should mention that you can find the full list in the file [noun.csv](dictionary/noun.csv), if you haven't guessed that yet.

### Pseudowords

_Pseudowords_ are common phrases that do not merit mention in a dictionary but do render as single words when written. These are the afforementioned relative verb noun definitions, the pronoun `f` modified by a relative clause with only a predicate. To save space, these may be written without whitespace between the characters. Thus, `f l u jeuth` may be written as a single word, `flujeuth`. They function just as nouns, as they would were the whitespace included. Pseudowords are very similar to _compound words_, but, as stated, are far too predictable and plentiful to be listed in a dictionary.

### Compound words

In addition to the basic, independent words, there are compound words. Compound words are formed by simply combining two or more preexisting words. A compound word may combine several common grammar tokens into a single word that has the same meaning as the combination of its parts, or it may combine two or more verbs, nouns, or pseudowords to create something new. The meaning and part of speech is closest to the first word, with the second word providing additional detail. There are thousands of them, supplying the many nuanced and specific concepts a complete langauge needs. The vast majority, however, are not documented here. That's because there are thousands of them, and I have a life. I recorded the ones I needed for various things in [compound_word.csv](dictionary/compound_word.csv), but I guess if you want to speak Djastiz, you can just come up with your own, provided they are logical. Submit a pull request if you think some compound word ought to be include din the main list. If it is a technical or regional term, though, beware, as a _loanword_ may be more appropriate.

### Loanwords

For words that describe deeply technical concepts like deoxyribonucleic acid, cultural concepts like ahupua&#8216;a, or a combination of the two like the oriental ladyfern, the preferred method of denotation is the loanword, a word taken directly from other languages (and modified to fit with Djastiz's phonology, of course). The word should be taken from a language that has regional or historical ties to the concept. For example, a specific species of fox should have a word loaned from a language spoken in a region where that fox is or was found. Note that this is also the preferred method for toponyms, even when the country in question uses a compound word in the native language. For example, while the United States of America could be described with the words `ngidh` and `flupshr`, the proper term in Djastiz is `iunaitedsteits`.

Like the compound words, the set of documented loanwords is not complete. They are meant to encompass the highly specific concepts that Djastiz cannot describe on its own, and thus to attempt to recond all of them in a Djastiz dictionary would be impossible. Instead, I have included some useful examples of loanwords in [loanword.csv](dictionary/loanword.csv)

### Causation and transitivity

It must be noted that, while in English, verbs often have multiple meanings for varying levels of transitivity (for example, the word "break" can mean either "to fall apart" or "to cause something else to fall apart"), in Djastiz, only the least transitive forms receive words. To describe a person causing something else to break, one must explicitly say, `sr e ingyeu u`, or the compound `sringyeu`. The purpose of this is to reduce ambiguity and redundancy. Two meanings are not necessary for this phenomenon, nor are two words. Furthermore, it prevents the occurrence of tritransitive and even potentially tetratransitive sentences (what if I were to mind-control your dog into forcing a child into making a vase break the plant inside it?), which would cause us to run out of argumentative prepositions. Therefore, if the transitivity of a Djastiz verb is unclear, always assume it to be as low as would make sense.

## Conventions, measurements, and coordinate systems

Djastiz indexes from zero. Obviously. `f o uf` can therefore translate to either "the first one" or "the second one" depending on how one does the translation. It literally means "the one that is number one", which would seem to imply "1°", or "first". However, in English, "first" refers to the instance that has no instances before it, whereas in Djastiz, `f o yu` refers to _that_ instance while `f o uf` refers to the one after it. A native Djastiz speaker typically counts finite objects by first pointing outside of the set and saying `yu`, and then pointing sequentially to the spaces between objects and saying a new number each time. The number of objects in the set is the number one says when pointing past the last one, on the opposite side of the set at which one started. If you're really good at counting, you can skip the `yu`, but it's important to always point between the objects and not at them, as normal people would, so as not to confuse your indices. Why would we do something so unintuitive and unusual? You tell me: what's the seventh year of the fifth decade of the eleventh century?

Djastiz also uses the metric system for all measurements of length, area, volume, mass, current, magnetic flux density, etc., with appropriate loanwords for each respective unit from French. Other units may, of course, be used, but metric is default. Djastiz does not, however, use the metric unit of time (seconds). Instead, times in Djastiz are typically represented in terms of powers of ten from the solar day. Unique words for the era (10<sub>5</sub> days, used for historical dates), the chunk (10<sub>3</sub> days, used for ages and long-term scheduling), the cycle (10<sub>1</sub> days, used for habitual and near-term scheduling), the day, the k&egrave; (10<sub>-2</sub> days, used for general scheduling), the span (10<sub>-3</sub> days, used for precise scheduling), and the snap (10<sub>-5</sub> days, used for human-perceptible timescales). The Gregorian calendar may be used with Latin loanwords for communicating with the outside world, or doing things that depend on the seasons. In case you were wondering, this time measurement system is called "Justin Time".

One other way that Djastiz differs from measurements in English is its greater number of coordinate words. While in English, the words "up", "down", "left", and "right" can mean different things in different contexts, in Djastiz, the corresponding words are precise. For example, "up" with respect to an elevator in English means a linear axis perpendicular to the local gravitational equipotential. "Up" with respect to a page, though, in fact means an angular direction that can be linearly up if the page is on a wall or forward if the page is on a table. Djastiz has separate words for these concepts: `rd` for the linear dimension, and `ssri` for the angular dimension. Always take care when speaking Djastiz to know whether to use Cartesian or spherical coordinates.

One more difference between location description in English and Djastiz are the typical positive directions. These do not usually affect speech, since words exist for both directions on every axis, but these conventions are important for mathematicians and computer scientists. The positive directions for all of Djastiz's coordinate systems are as follows: forward in time, linear down, linear right, forward, outward, angular down, linear right, counterclockwise, south, and east. Note that while the positive direction for altitude is down, positive numbers are often used to describe height above sea level, and building floors still count upward.

## Gestures

Like any self-respecting language, Djastiz comes with a variety of gestures to express common sayings or feelings without the need to use one's voice. The most common are as follows.
- When greeting someone, hold your hand in front of you and rub your forefinger and thumb or middle finger and thumb up and down.
- When bidding someone farewell, wave one or both arms up and down in front of you. Optionally, apply a wave effect to the arm motion that moves away from you. If using both arms, make sure to alternate them so as to give the impression of an octopus.
- When answering in the affirmative, display the back of your hand and splay the fingers.
- When answering in the negative, face your palm to the floor and gently shake the hand back and forth, holding it at a constant height.
- To display joy or excitement, hold your arm straight up with a clenched fist.
- To display sadness or disappointment, press a clenched fist into an open palm.
- To display approval or appreciation toward a person, place your palms together, holding them horizontally, and slide the top hand forward, off of the bottom one.
- To display disapproval or depreciation toward a person, point at them with two fingers and wag the fingers up and down in opposition to one another.

# How to Speak Chatisun

So, you want to sing a better and more succinct version of [Olde Djastiz](https://github.com/jkunimune15/Djastiz/tree/master). How do you do that? By speaking Chatisun, that's how! What's Chatisun? It's a high-level language optimised for efficiency that I invented. Here's how it works.

## Phonology and orthography

### Alphabet

Before you read any further, you'll need to know how to read, say, and write these words. Luckily, this is extremely easy. Chatisun uses only the seventeen most common sounds, and writes them with a basic one-letter-per-phoneme-one-phoneme-per-letter Latin-derived orthography. It's so simple that a wise man can acquaint himself with it before the hour is over; even a stupid man can learn it in the space of two days. The following tables sumarise the phonology using the [International Phonetic Alphabet](1):

|               | Labial | Coronal | Palatal | Guttural |
|:--------------|:------:|:-------:|:-------:|:--------:|
|**Plosive**    |    p   |    t    |         |    k     |
|**Fricative**  |    f   |    s   |tʃ &lt;c&gt;|  h     |
|**Nasal**      |    m   |    n    |         |          |
|**Approximant**|    w   |    l    |    j    |          |

|         | Front | Back |
|:--------|:-----:|:----:|
|**Close**|   i   |  u   |
|**Mid**  |   e   |  o   |
|**Open** |   a   |      |

If you don't know what any of that means, don't worry about it. Here is a more thorough table. Note that in addition to a name and a symbol, each letter has a "Recommended Pronunciation" and several "Possible Pronunciations". The possible pronunciations are just allowed variations on each sound for people who don't have the recommended pronunciation in their native tongue. You speak English, so you pretty much have all of the recommended pronunciations down, so just know that you might hear people of different backgrounds using some slightly different pronunciations of each letter. The "Inverse" and "Class" columns are not that important; they just come up later in the derivational morphology section. You don't have to learn that part if you don't want to.

| Name | Symbol | Rec. Pron. | Pos. Prons. | English example | Inverse | Class
|------|--------|------------|-------------|-----------------|---------|-------
|   e  |   e    |     ɛ      |    e\~ɛ     |      End        |    o    | Vowel
|   a  |   a    |     a      |    a\~ɑ     |      Off        |    a    | Vowel
|   o  |   o    |     ɔ      |    o\~ɔ     |     Organ       |    e    | Vowel
|   i  |   i    |     i      |    i\~ɪ     |      EAt        |    u    | Vowel
|   u  |   u    |     u      |    u\~ʊ     |      OOze       |    i    | Vowel
|  jot |   j    |     j      |   j, ʲ, i   |      Yell       |   wet   | Glide
|  lo  |   l    |     l      |    l\~ɾ     |      Limb       |    te   | Sonorant
|  wet |   w    |     w      |   w, ʷ, u   |     Wander      |   jot   | Glide
|  no  |   n    |     n      |   n, ŋ\~ɴ   |     Night       |    ko   | Sonorant
|  me  |   m    |     m      |      m      |      Meat       |    pe   | Sonorant
|  ho  |   h    |     h      |   x\~h, ɦ   |      Hack       |    co   | Sonorant
|  co  |   c    |    tʃ      |tʃ\~tʂ, ʃ\~ʂ |      CHop       |    ho   | Obstruent
|  se  |   s    |     s      |      s      |      Soon       |    fe   | Obstruent
|  fe  |   f    |     f      |    ɸ\~f     |      Fall       |    se   | Sonorant
|  ko  |   k    |     k      |   k kʰ ɡ    |      Kill       |    no   | Obstruent
|  te  |   t    |     t      |   t tʰ d    |      Tomb       |    lo   | Obstruent
|  pe  |   p    |     p      |   p pʰ b    |      Pool       |    me   | Obstruent

You'll notice that most of the letters match their IPA transcriptions as well as their English counterparts. The only things of which you need to be careful are &lt;j&gt;, &lt;c&gt;, and the vowels. There's a handy alphabet song in the main repository to help you remember them all if you like.

Note that while all of these symbols come from the Latin alphabet, the Latin alphabet is _not_ the Chatisun alphabet. The Chatisun alphabet does not include <b>, <d>, <g>, <q>, <r>, <v>, <x>, <y>, <z>, or any capital letters, so none of these should be present in a Chatisun text. It is acceptable to use all capital letters in lieu of lowercase letters as a stylistic choice, but if you do so, I recommend using a font where <E>, <A>, <N>, and <H> are easily recognisable from their lowercase counterparts, lest the text be indescipherable to some Chatisun-speakers.

[1]: http://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/ "International Phonetic Alphabet"

### Punctuation

In addition to this subset of Latin letters, a subset of other Latin symbols may be used with Chatisun to aid parsing. None of these are required, but it is important to understand what they mean in case you come across them in Launtoklian texts.

| Name | Symbol | Usage | Example |
|------|--------|-------|---------|
|      |        | Separates words or clusters of digits in long numbers
|      | '      | Precedes a _loanword_
|      | .      | Follows the last word of a sentence or the ones digit of floating point numbers
|      | ,      | Follows the last word before a brief pause
|      | (      | Precedes the first word of an ambiguously bounded phrase
|      | )      | Follows the last word of an ambiguously bounded phrase
|      | ~      | Denotes a range between two values
|      | -      | Precedes the digits of a negative number or denotes the subtraction of two values
|      | +      | Denotes addition of two values or stands in for the word `and`
|      | /      | Precedes the denominator of a fraction
|      | 0      | Zero
|      | 1      | One
|      | 2      | Two
|      | 3      | Three
|      | 4      | Four
|      | 5      | Five
|      | 6      | Six
|      | 7      | Seven
|      | 8      | Eight
|      | 9      | Nine
|      | A      | Ten (only in base twelve or sixteen)
|      | B      | Eleven (only in base twelve or sixteen)
|      | C      | Twelve (only in base sixteen)
|      | D      | Thirteen (only in base sixteen)
|      | E      | Fourteen (only in base sixteen)
|      | F      | Fifteen (only in base sixteen)

## Vocabulary

There are three broad classes of word in Chastisun: nouns, verbs, and particles. These words are drawn from Chinese, Italic, Germanic, Indo-Iranian, Semitic, Atlantic-Congo, and Esperanto lexicons. The source languages were carefully selected and weighted in order to give the most mnemonic value to the greatest number of people. Source words are modified when entering Chatisun to match its strict morphology. All morphemes start and end with a consonant and contain no consonant clusters, so consonant clusters indicate morpheme boundaries in compound words. Particles, meanwhile, either start or end with a vowel depending on whether they are a prefix-particle or a suffix-particle. The following section will discuss verbs and nouns, as well as their properties and various subdivisions.

### Verbs

As previously stated, verbs are used to create predicates. The list of all verbs is present in this repository at [verb.csv](dictionary/verb.csv). There are two main classes of verb: _dynamic_ and _stative_.

Dynamic verbs are more like the verbs an English-speaker might encounter in its own language. Each describes an action that changes with respect to time. The universe after the action occurs is typically different from the universe before.

Stative verbs tend to share more in common with English adjectives than English verbs. They indicate that the subject has some state, which may or may not change as time passes. When the state has a numeric parameter, such as the latitude in `bav`, that number can be specified by the complement of `ia`, and the reference, or zero, can be specified by the direct object. Thus, `reidien ir ho ang ia filidelfia u bav`. When the state takes a non-numeric parameter, such as `thru`, the verb is a special kind of stative verb called a _copula_, and that parameter should be the object. When the state cannot be logically parametrised, it is called an _absolute_.

### Nouns

If it is a binary state with no arguments, it should be a noun, not a verb.
I actually have nothing more to say about nouns. They are completely intuitive and uninteresting words that seed noun phrases, though I suppose I should mention that you can find the full list in the file [noun.csv](dictionary/noun.csv), if you haven't guessed that yet.

### Pseudowords

_Pseudowords_ are common phrases that do not merit mention in a dictionary but do render as single words when written. These are the afforementioned relative verb noun definitions, the pronoun `f` modified by a relative clause with only a predicate. To save space, these may be written without whitespace between the characters. Thus, `f l u jeuth` may be written as a single word, `flujeuth`. They function just as nouns, as they would were the whitespace included. Pseudowords are very similar to _compound words_, but, as stated, are far too predictable and plentiful to be listed in a dictionary.

### Compound words

In addition to the basic, independent words, there are compound words. Compound words are formed by simply combining two or more preexisting words. A compound word may combine several common grammar tokens into a single word that has the same meaning as the combination of its parts, or it may combine two or more verbs, nouns, or pseudowords to create something new. In the latter case, the meaning and part of speech is closest to the second word, with the first word providing additional detail. There are thousands of them, supplying the many nuanced and specific concepts a complete langauge needs. The vast majority, however, are not documented here. That's because there are thousands of them, and I have a life. I recorded the ones I needed for various things in [compound_word.csv](dictionary/compound_word.csv), but I guess if you want to sing Djastiz, you can just come up with your own, provided they are logical. Submit a pull request if you think some compound word ought to be included in the main list. If it is a technical or regional term, though, beware, as a _loanword_ may be more appropriate.

### Loanwords

Approved extensions to the Chatisun alphabet for more accurate transcription of loanwords:
ɒ y ɯ ŋ ʔ b d ɡ θ ʃ x v ð z ʒ ɣ ɽ ʙ r ǃ ˩ ˨ ˧ ˦ ˥

|                          | Labial | Dental | Alveolar | Postalveolar&tilde;Retroflex | Palatal | Velar&tilde;Uvular | Pharangeal&tilde;Glottal |
|--------------------------|--------|--------|----------|--------------|---------|-------|---------|
|**Nasal**                 | m      | n      | n        | n            | ŋj      | ŋ     |         |
|**Plosive**               | p b    | t d    | t d      | t d          | kj gj   | k g   | ʔ       |
|**Fricative**             | f v    | θ ð    | s z      | ʃ ʒ          | xj ɣj   | x ɣ   | h       |
|**Lateral fricative**     |        | lʃ lʒ  | lʃ lʒ    | lʃ lʒ        | lx lɣ   | lx lɣ |         |
|**Approximant**           | w      | ɹ      | ɹ        | ɹ            | j       | ɯ     |         |
|**Lateral approximant**   |        | l      | l        | l            | lj      | lɯ    |         |
|**Tap/Trill**             | ʙ      | r      | r        | r            |         | r     |         |
|**Click/Implosive**       | ǃ      | ǃ      | ǃ        | ǃ            | ǃ       | !     |         |
|**Secondary articulation**| ◌w     | ◌ɹ     | ◌ɹ       | ◌ɹ           | ◌j      | ◌ɣ    | ◌ʔ      |

|               | Front | Central | Back |
|---------------|-------|---------|------|
|**Approximant**| j y   | j w     | ɯ w  |
|**Close**      | i y   | i u     | ɯ u  |
|**Mid**        | e y   | a ɒ     | ɯ o  |
|**Open**       | a ɒ   | a ɒ     | a ɒ  |

|**Voiceless**      | nh |**Stress**| ' |
|**Aspirated**      | th |**Long**  | ee|
|**Rhoticity**      | aɹ |**High**  | ˥ |
|**Nasalised**      | en |**Mid**   | ˧ |
|**Nasal release**  | dn |**Low**   | ˩ |
|**Lateral release**| dl |

For words that describe deeply technical concepts like deoxyribonucleic acid, cultural concepts like ahupua&#8216;a, or a combination of the two like the oriental ladyfern, the preferred method of denotation is the loanword, a word taken directly from other languages. Loanwords in Musical Djastiz use Modern Djastiz's phonology. The word should be taken from a language that has regional or historical ties to the concept. For example, a specific species of fox should have a word loaned from a language sung in a region where that fox is or was found. Gramatically, loanwords are equivalent to nouns. Note that this is also the preferred method for generating toponyms, even when the country in question uses a compound word in the native language. For example, while the United States of America could be described with the words `ngidh` and `flupshr`, the proper term in Djastiz is `iunaitedsteits`. Loanwords use the phonology of Modern Djastiz, and contain no tones save the `moja`.

Like the compound words, the set of documented loanwords is not complete. They are meant to encompass the highly specific concepts that Djastiz cannot describe on its own, and thus to attempt to recond all of them in a Djastiz dictionary would be impossible. Instead, I have included some useful examples of loanwords in [loanword.csv](dictionary/loanword.csv).

### Causation and transitivity

It must be noted that, while in English, verbs often have multiple meanings for varying levels of transitivity (for example, the word "break" can mean either "to fall apart" or "to cause something else to fall apart"), in Djastiz, only the least transitive forms receive words. To describe a person causing something else to break, one must explicitly say, `sr e ingyeu u`, or the compound `sringyeu`. The purpose of this is to reduce ambiguity and redundancy. Two meanings are not necessary for this phenomenon, nor are two words. Furthermore, it prevents the occurrence of tritransitive and even potentially tetratransitive sentences (what if I were to mind-control your dog into forcing a child into making a vase break the plant inside it?), which would cause us to run out of argumentative prepositions. Therefore, if the transitivity of a Djastiz verb is unclear, always assume it to be as low as would make sense.

### Conventions, measurements, and coordinate systems

Djastiz indexes from zero. Obviously. `f o uf` can therefore translate to either "the first one" or "the second one" depending on how one does the translation. It literally means "the one that is number one", which would seem to imply "1°", or "first". However, in English, "first" refers to the instance that has no instances before it, whereas in Djastiz, `f o yu` refers to _that_ instance while `f o uf` refers to the one after it. A native Djastiz singer typically counts finite objects by first pointing outside of the set and saying `yu`, and then pointing sequentially to the spaces between objects and saying a new number each time. The number of objects in the set is the number one says when pointing past the last one, on the opposite side of the set at which one started. If you're really good at counting, you can skip the `yu`, but it's important to always point between the objects and not at them, as normal people would, so as not to confuse your indices. Why would we do something so unintuitive and unusual? You tell me: what's the seventh year of the fifth decade of the eleventh century?

Djastiz also uses the metric system for all measurements of length, area, volume, mass, current, magnetic flux density, etc., with appropriate loanwords for each respective unit from French. Other units may, of course, be used, but metric is default. Djastiz does not, however, use the metric unit of time (seconds). Instead, times in Djastiz are typically represented in terms of powers of ten from the solar day. Unique words for the era (10<sup>5</sup> days, used for historical dates), the chunk (10<sup>3</sup> days, used for ages and long-term scheduling), the cycle (10<sup>1</sup> days, used for habitual and near-term scheduling), the day, the k&egrave; (10<sup>-2</sup> days, used for general scheduling), the span (10<sup>-3</sup> days, used for precise scheduling), and the snap (10<sup>-5</sup> days, used for human-perceptible timescales). The Gregorian calendar may be used with Latin loanwords for communicating with the outside world, or doing things that depend on the seasons. In case you were wondering, this time measurement system is called "Justin Time".

One other way that Djastiz differs from measurements in English is its greater number of coordinate words. While in English, the words "up", "down", "left", and "right" can mean different things in different contexts, in Djastiz, the corresponding words are precise. For example, "up" with respect to an elevator in English means a linear axis perpendicular to the local gravitational equipotential. "Up" with respect to a page, though, in fact means an angular direction that can be linearly up if the page is on a wall or forward if the page is on a table. Djastiz has separate words for these concepts: `rd` for the linear dimension, and `ssri` for the angular dimension. Always take care when singing Djastiz to know whether to use Cartesian or spherical coordinates.

One more difference between location description in English and Djastiz is the typical positive directions. These do not usually affect speech, since words exist for both directions on every axis, but these conventions are important for mathematicians and computer scientists. The positive directions for all of Djastiz's coordinate systems are as follows: forward in time, linear down, linear right, forward, outward, angular down, linear right, counterclockwise, south, and east. Note that while the positive direction for altitude is down, positive numbers are often used to describe height above sea level, and building floors still count upward.

## Grammar

The grammar of Chastisun is designed to be as simple as possible while enabling speakers to be either simple and vague or exact and precise at will. It can be summed up in the following way.
             sentence ::=  clause-phrase | (sentence-particle.simple noun-phrase)
    clause-phrase ::= (sentence-particle)? (postpos-phrase)\* (verb-phrase (postpos-phrase)\*)?
   postpos-phrase ::=  complement-phrase postposition
complement-phrase ::=  noun-phrase | clause-phrase
      noun-phrase ::= (qualifier)? (noun | pronoun | relative-phrase | complement-phrase &lt;in&gt; | noun-phrase)\*
      verb-phrase ::=  verb (verb.auxiliary)\*
  relative-phrase ::= \[sentence-particle\] (postpos-phrase)\* \[verb-phrase (postpos-phrase)\*\] \["l" postposition\]
         X-phrase ::= "bo"? X-phrase "an" X-phrase
   Substance-rule : No phrase may be empty.
   Trail-off-rule : Any number of words can be removed from the start and end of a sentence as long as the meaning remains clear.

### Mood markers

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

### Modifiers

Modifiers are great ways to expand and enhance the meanings of nouns. There two types of modifiers. The simpler one is the _noun modifier_.

A noun modifier has two parts: a _fastener_ and a noun phrase. The fastener uses the following noun phrase to modify the preceding noun phrase in a specific manner, depending on the fastener. There are five fasteners that each represent a different method of modifying a noun.
- `am` denotes the specific variety or attributes of the preceding noun phrase.
- `ù` specifies the amount, degree, or number of the preceding noun phrase.
- `al` indicates the specific instance of the preceding noun phrase.
- `ú` draws equality between the preceding and following noun phrases without really changing the meaning of the sentence. It is especially useful for sharing names (e.g. `ōpèmólārȅm ú Esteban`).
- `è` indicates and extracts a specific element of a set.

The more versatile modifier is the _relative clause_. Relative clauses are simply lists of prepositional phrases that contain `pèm` in them somewhere followed by a verb. The `pèm` should be placed as close to the beginning of the relative clause as possible. It usually goes at the very front, adjacent to the modified noun phrase, but this is not always possible. Again, while these resemble full sentences, they are not. A modifier clause modifies a noun phrase by placing it inside another sentence. The result is two clauses that are true together. The first is the original sentence with the modifier clause simply removed. The second is the entire modifier with `ȅ` prepended and the modified noun phrase inserted for `pèm`. This type of modifier draws an equality between the noun phrase and itself across the two clauses. While relative clauses seems at first glance to be far more complex than noun modifiers, they are, in fact, capable of creating some of the simplest and most useful noun modifications: _simple ergative relative clauses_, the analog to adjectives in other languages, for example, `dhap l r at`; and _relative verb noun definitions_, the analog to English's "-er" and "-ee", for example, `f l u jeuth`.

### Conjunctions

The last major grammatical structure to be discussed is the conjunction. Conjunctions are a small class of diverse words that transform phrases or sets of phrases. While they share some similarities, the two pairs of conjunctions are different enough that I might as well explain each separately.

The first and most recognizably conjugative conjunctions are `ā` and `pe`. When `ā` precedes a series of phrases separated by `pe`, they combine said series into a single set representing all of the phrases combined. The input phrases are usually noun phrases, but practically anything can be fed in here so long as each phrase is of the same type. They translate very cleanly to "both" and "and" in English, respectively. That set can then have its meaning easily tweaked using qualifiers. For example, `dhe ni mus a thengga`.

The other pair of conjunctions may be more difficult to understand for English singers. This is the `é` and `ò` construction, which functions much like the quotation mark in English. Unlike the quotation mark, however, `é`-`ò` constructions must be sung aloud. Any phrase in any language between the `é` and the `ò` should not be interpreted as actual Djastiz grammar, but rather as a sequence of letters or sounds. The entire phrase acts as a noun and references the phrase contained within. This is most commonly used for quoting dialogue and discussing language. To indicate that a single word inside a `é`-`ò` construct should be interpreted literally and not as part of the quote, precede it with the word `rèl`, for example, `dhi ij yr tshef je l u ssu u`. To describe the word or sound `rèl`, precede it with `rèl`. For example, `raun yr dhi ij yr tshef je je l u ssu u ssu u`.

### Numbers

number := (number <rad>)? <neg>? (digit)* (<paw> number)?

### Special words

Most of the words discussed thus far have fallen into categories and followed simple rules. We now discuss a few of the more unique words and groups of words that do not accept labels so easily.

`oth`, `thu`, `ja`, and `oj` are the simple tense markers. Simple tense markers are used when a sentence is too common or basic to warrant a full list of prepositional phrases. Instead, one may follow the marker with a single noun phrase. When using `oth`, the noun phrase represents the current occasion, and the full sentence forms a greeting or congratulation. `thu`, similary, precedes the current occasion but forms a parting statement. Thus, `oth vorng` greets people during the day, `oth krismes` celebrates Christmas, and `thu ursh` sends people to bed. `ja` and `oj`, on the other hand, express happiness or respect, or unhappiness or disgust, respectively, toward a noun phrase. For example, `ja flrsrjarzyuo` praises air conditioning, `ja hitlr` hails Hitler, and `oj k` fucks you. Simple punctuation markers can also be used with nothing following them at all. In that case, `oth` expresses a general greeting and `oj` an exclamation of general anger.

`l` is the question word, very similar to "what" in English. Rather than carrying information, like most words, `l` denotes a lack of information. `l` is used in two cases, both previously mentioned: standing in for desired information in sentences starting with `ung`, and beginning a relative clause as well as indicating the modified noun phrase's place within the clause.

Numbers can also be considered special words in that they concatenate with each other in a unique way. Quantities in Djastiz are described by a string of number words. The final quantity is obtained by summing all of the digits after applying a multiplier to each one greater than that of the next by a factor of the radix, which is ten by default. In other words, say a number in Djastiz by writing it in decimal notation and then reading off each digit in Djastiz in sequence. Extremely large and imprecise numbers can be described efficiently by dividing out a logical number of factors of the radix, and then appending the word `uo` and the number of powers divided. The decimal point is read `ho` and is placed among the digits as with standard numeral notation. Negative numbers should have `me` inserted at the beginning. Fractions can be expressed by describing the denominator as a unit. Finally, to use radices other than ten, precede the number with the base in Djastiz plus the word `adh`. There exist enough words to easily use any radix from two to sixteen. For larger radices, the radix is typically said in base ten, though if you want, I guess you can nest them, if you need to represent 3,723 in base 0x3C for some reason. Does that sound complicated? It isn't. Some examples will probably help. `ang od`, `uf po tho od`, `flushifpo ir rh rh`, `rh adh re ngu adh uf od re`  and `ev ho od rh re uf rh zha re yu po`.

`skelf` is a bit of a meta-word. It tells the listener to ignore the previous few words sung. This is used exclusively for error correction, so it rarely comes up in writing.

### Tips and tricks

That's all of the official grammar. You may find it rather short. "Where are the tenses, the passives, the participles?" you ask. While these do not exist explicitly in Launtoklian, they can be expressed using preexisting structures. Therefore, while their inclusion here is not strictly necessary, I will explain them so that everyone understands best practices for such situations without needing derive them themselves.

Tenses are simple. If it is important to a sentence whether it happened in the past, present, or future, the dative postposition `ec` can be used with the appropriate word.

Passives are somewhat nonexistent in Launtoklian

Participles in Launtoklian are represented with relative clauses.

## Gestures

Like any self-respecting language, Djastiz comes with a variety of gestures to express common sayings or feelings without the need to use one's voice. The most common are as follows.
- When greeting someone, hold your hand in front of you and rub your forefinger and thumb or middle finger and thumb up and down.
- When bidding someone farewell, wave one or both arms up and down in front of you. Optionally, apply a wave effect to the arm motion that moves away from you. If using both arms, make sure to alternate them so as to give the impression of an octopus.
- When answering in the affirmative, display the back of your hand and splay the fingers.
- When answering in the negative, face your palm to the floor and gently shake the hand back and forth, holding it at a constant height.
- To display joy or excitement, hold your arm straight up with a clenched fist.
- To display sadness or disappointment, press a clenched fist into an open palm.
- To display approval or appreciation toward a person, place your palms together, holding them horizontally, and slide the top hand forward, off of the bottom one.
- To display disapproval or depreciation toward a person, slowly and gracefully raise your hands toward them while saying "oooooooooooh" quietly.

## Sun never sets clause

The final and most important rule is this: Launtoklian is defined, not by its users, but by this document. In order for an international auxiliary language to be effective, everyone must speak the same variety. That means that the final arbiter for what does and doesn't constitute correct Launtoklian is this. Anyone is, of course, free to interpret and use the language in any way they see fit. However, if their variation on Launtoklian contradicts this document, they cannot rightly assert their variation to be correct.

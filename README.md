# Djastiz

So, you want to speak a better and less biased version of Esperanto. How do you do that? By speaking Djastiz, that's how! What's Djastiz? It's a basic, unambiguous, non-redundant language that I invented. Here's how it works.

## Grammar

The grammar of Djastiz is designed to be nearly unambiguous and minimally redundant. As such, there are far more grammar tokens than in other languages. The primary advantage of this structure is increased control over which information is included and excluded. However, it can seem overwhelming at first. Worry not! Every Djastiz sentence can be broken down into several basic parts.

### Punctuation markers

Every full sentence in Djastiz starts with a _punctuation marker_. There are nine of them, and each creates a fundamentally different kind of sentence.
- `poj` is the _declarative_ punctuation marker. It precedes a sentence that conveys information. The event or fact described in a declarative sentence is true, according to the speaker.
- `zad` is the _interrogative_ punctuation marker. It precedes a sentence that requests information. An interrogative sentence usually contains the word `sob` at least once, though the position of `sob` can also be implied. In either case, `sob` represents a piece of information missing from the sentence that the speaker would like to know.
- `saz` is the _imperative_ punctuation marker. It precedes a sentence that requests action. An imperative sentence describes an event or action that the speaker wants to happen.
- `kit` is a bit more complicated. It does not create sentences at all, but rather _noun clauses_. These will be discussed in &#167;1.3.
- `ped` also does not create sentences, but _modifier clauses_. They are described in more detail in &#167;1.4.
- `pioip` is the _bureaucratic_ punctuation marker. It behaves similarly to `poj`, specifically in contexts where saying a sentence causes it to be true. Bureaucratic sentences are especially useful for proclamations, definitions, and assumptions in mathematical proofs.
- `shuaij` behaves exactly like `saz`, but frames the request as less mandatory and more polite. The frequency with which one uses `shuaij` versus `saz` completely depends on the society, and since no society actually speaks Djastiz, I have no idea how useful this word is.
- `daid` is the _salutary_ punctuation marker. It is used to construct simple greetings. `daid` is a _simple_ punctuation marker. These obey special rules and will be discussed again in &#167;1.6.
- `shuip` is the _exclamatory_ punctuation marker, and, like `daid`, is simple. It expresses concise feelings and opinions.

In addition to labelling the type of sentence, the punctuation marker acts as the sentence's opening bracket. The sentence can be ended by the fullstop token, `up`, by the punctuation marker of the next sentence, or just with the silence after a person stops talking. Between these tokens lies the meat of the sentence: a list of _prepositional phrases_.

### Prepositional phrases

Every prepositional phrase describes one aspect of the event described by the sentence, and comprises two parts: the _preposition_ and the _complement_, which is a _noun phrase_. The preposition specifies what aspect of the sentence is being described, and the complement describes that aspect. There are two types of preposition.

_Argumentative prepositions_ may only be included once per sentence. The first, and most important, is `e`. `e` precedes the _predicate_ of the sentence - the noun phrase that denotes the action in question. The other argumentative prepositions may or may not be _applicable_ based on the complement of the predicate. If an argumentative preposition is applicable, it may be included in the sentence, but does not need to be if its complement is implied. A proper Djastiz dictionary would list the applicable argumentative prepositions for every noun in the language, as well as their precise meanings in each case. Let's be real, though. There's no way I'm going to do that. Instead, I'll leave it up to the speakers' discretion when each preposition is applicable. In general:
- `bu` denotes the _subject_ of the action, the agent that initializes and/or carries out the action (e.g. the writer of `debag`). `bu` is almost always applicable.
- `iu` denotes the _direct object_, usually but not necessarily, inanimate. Use `iu` when an action is applied directly to something (e.g. the food of `ukiaj`).
- `si` denotes the _target_ of the action, usually an inanimate object, location, or concept. Use `si` when an action occurs toward some object or location (e.g. the destination of `ugi`). It often serves as the complement of `iu` (e.g. the old and new values in `ikaib`)
- `og` denotes the _reciprocator_ of the action, the agent that receives the action. Use `og` when an agent must carry out an opposite action when the subject carries out the action in question (e.g. the loser of `badiz`).

_Adjunctive prepositions_, by contrast, are always applicable, and can be used multiple times in one sentence if being used in different contexts (e.g. using `shug` once for the location in virtual space and again for the location in real space). They denote, in a sense, the "who, where, when, why, how" of the sentence.
- `shug` denotes the location of the action in physical space.
- `shok` denotes the date and/or time of the action.
- `shau` denotes the state of the action in any sense besides physical or temporal. It is a bit of a catch-all in terms of adjunctive prepositions.
- `sheb` denotes the cause of the action.
- `dij` denotes the purpose of the action.
- `set` denotes the context of the action, very much like "regarding ..." or "in the ... sense" in English.
- `zop` denotes the method of the action, usually a noun clause that happened with or before the initial action.
- `oush` denotes the tool or medium of the action.
- `shat` denotes whether the action happened (generally only used in interrogative sentences, since it's universally implied to be `kaup`).
- `jeu` denotes the extent or quantity of the action. This can be a number or another noun to be compared against.
- `kush` denotes the hypothetical conditions surrounding the action (very similar to English's "if").

### Noun phrases

Noun phrases are the primary building blocks with which one describes complex concepts. There are four primary ways to construct these.

The first, and by far the simplest, is a _noun_. There are hundreds to choose from! Often, however, the concept one wants will not be found in the list. The next method is the appendix of a _modifier_. Modifiers are attached to the ends of noun phrases to create new noun phrases. The third and perhaps most complicated is a noun clause. A noun clause comprises `kit`, a list of prepositional phrases, and `up`. Noun clauses appear at first to be sentences with `kit` as their punctuation marker. However, do not be misled. These are nouns that refer to the meaning of the sentence they appear to be. Furthermore, for noun clauses, the `up` is mandatory.

The fourth way is _pronouns_, which function exactly as nouns do, but with meanings that change from sentence to sentence. There are five of them.
- `ju` is the simplest pronoun. It carries no information, and acts as more of a placeholder than anything else.
- `bas` refers to the speaker or writer.
- `kek` refers to the listener or reader.
- `tuj` refers to an agent besides the speaker or listener. This is usually combined with `bas` and `kek` to form constructs like "we" and "ye" in English.
- `sob` denotes a lack of information and has special rules in special contexts, one of which has already been discused.

Noun phrases can also technically be created with _conjunctions_, but then, so can prepositional phrases and modifiers. I'll explain those in a different paragraph.

### Modifiers

Modifiers are great ways to expand and enhance the meanings of nouns. There are several types of modifiers for uses in different contexts.

The most versatile of modifiers is the modifier clause. Modifier clauses comprise `ped`, a list of prepositional phrases, and `up`. Again, while these resemble full sentences, they are not. A modifier clause modifies a noun phrase by placing it inside another sentence. Modifier clauses usually contain a prepositional phrase with a complement of `sob`. When a noun is modified by a modifier phrase in a sentence, that sentence can be broken into two sentences that, combined, are equivalent to the original sentence. The first is the original sentence with the modifier clause simply removed. The second is the modifier clause with `poj` substituted for `ped` and the modified noun phrase substituted for `sob`. The `sob` propositional phrase is sometimes omitted, its preposition implied. The `up` is mandatory for modifier clauses, as with noun clauses.

You may wonder, why would a person ever use this construction? Why not simply use two sentences and be done with it? Because, foolish reader, that would defeat the point of modifiers! These clauses have the unique ability of showing equality between the noun phrase in question in the sentence and the modifier clause without having to resort to ambiguous _article_ trickery (more on that later). They are also extremely handy for common noun transformations such as the "-er" suffix in English (e.g. to change swimming to swimmer, change `zoshet` to `ju ped e zoshet bu sob up`, or `je zoshet up` for short (more on _contractions_ later)).

The next type of modifier is much simpler, but also the most ambiguous part of Djastiz. This is the _fastener modifier_. A fastener modifier comprises a _fastener_ and a noun phrase, and it draws a simple relationship between the noun phrases in and affected by the modifier. It should be noted that, unlike other modifiers, fasteners can also modify prepositions and punctuations (usually with things like `podi` and `sabus`), which makes them extremely versatile and useful. Beware, though, for there is no firm order-of-operations for nested fasteners, making phrases like `pobok dik asheiashu dik oudush` ambiguous. While contextual clues are usually enough to avoid confusion from these statements, care must be taken whenever using fasteners, and modifier clauses should be used whenever one thinks a phrase may be misconstrued. There are five different fasteners.
- `dik` alters the meaning of a noun phrase by denoting the specific variety or attributes.
- `aub` specifies the amount, degree, or number of the preceding noun phrase.
- `shos` focuses a noun phrase from describing a concept or category to a specific instance.
- `aus` draws an equality between two noun phrases without really changing the meaning of the sentence. It is especially useful for sharing names (e.g. `abosh aus pi Esteban id`).
- `jap` identifies a specific element of a _set_ (a set is just a noun phrase that describes a group of things).

For fastener constructions that are too common to warrant even a fastener, there are the simplest modifiers: _articles_. Articles are unique one-word modifiers that replace common `shos` constructions, manipulate sets, and other nifty things like that. Articles always take precedence over fasteners, so using fasteners together with articles is not ambiguous. There are nine articles.
- `zut` describes an instance of a noun phrase near or associated with the speaker.
- `eik` describes an instance of a noun phrase near or associated with the listener.
- `puk` describes an instance of a noun phrase neither near or associated with the speaker nor the listener.
- `jes` describes an instance of a noun phrase previously mentioned in the conversation.
- `guz` describes an instance of a noun phrase not previously mentioned in the conversation.
- `zai` describes the set of all instances of a noun phrase.
- `sak` describes a single unspecified element of a set.
- `bet` describes an unspecified subset of a set.
- `pip` describes each and every element of a set individually.

I guess _prefixes_ could be counted as a fourth kind of modifier, but they're pretty different, so I discuss them in &#167;2.1.

### Conjunctions

The last major grammatical structure to be discussed here is the conjunction. Conjunctions are a small class of diverse words that transform phrases or sets of phrases. While they share some similarities, the three conjunctions are different enough that I might as well explain each separately.

The first and most recognizably conjugative conjunction is the `to`-`ish`-`id` construction: `to`, followed by a list of `ish`-separated phrases, followed by `id`. All of the inner phrases must be of the same type (e.g. noun phrase, modifier clause, preposition), and the construction acts as the same type of each of its components, with a meaning equivalent to the combination of the meanings of all of the inner phrases. In other words, `to` means "both", and `ish` means "and", assuming there is an `id` on the end. It should be noted that `to`-`ish`-`id` constructions can be used with set-manipulation articles and, in fact, do so quite well. For example, `to oudis ish iogu id pip` refers to hopes and dreams individually.

The second conjunction may be more difficult to understand for English speakers. This is the `aj`-`id` construction, which functions much like the quotation mark in English. Unlike the quotation mark, however, `aj`-`id` constructions must be spoken aloud. Any phrase in any language between the `aj` and the `id` should not be interpreted as actual Djastiz grammar, but rather as a sequence of letters or sounds. The entire phrase acts as a noun and references the phrase contained within. This is most commonly used for quoting dialogue and discussing language. `aj`-`id` constructions also concatenate with each other and other noun phrases, like so: `zad iu aj peigsaz e ukiaj iu id sob`

The final conjunction has no analog in English. `pi`-`id` constructions act similarly to `aj`-`id` constructions, but rather than describing the syllables contained between the `pi` and `id`, it describes the object named by said syllables. Whenever one wants to discuss a person, country, book, or corporation `pi` and `id` must be used so as not to confuse the named object with the literal meaning of the name.

### Special words

Most of the words discussed thus far have fallen into categories and followed simple rules. We now discuss a few of the more unique words that do not accept labels so easily.

`daid` and `shuip` compose the entirety of the simple punctuation markers. Simple punctuation markers are used when a sentence is too common or basic to warrant a full list of prepositional phrases. Instead, one follows the marker with a single noun phrase. When using `daid`, the noun phrase represents the current occasion, and the full sentence forms a greeting or congratulation. Thus, `daid zidug` greets people during the day, `daid pi Christmas id` during Christmas, and `daid iatshutua` immediately after a graduation. `shuip`, on the other hand, expresses happiness or respect toward a noun phrase. For example, `shuip iatpeuzpubuksedog` praises air conditioning, `shuip pi Hitler id` hails Hitler, and `iatshuip kek` fucks you (see &#167;2.2). Simple punctuation markers can also be used independently, `daid` expressing a general greeting and `shuip` an exclamation of general happiness.

`sob` is the question word, very similar to "what" in English. Rather than carrying information, like most words, `sob` denotes a lack of information. `sob` is only used in `zad` and `ped` clauses, but neither clause requires a `sob`. In many cases, the position of `sob` can be inferred from contextual clues (e.g. `shat sob` is rarely necessary).

Numbers can also be considered a special word in that they concatenate with each other in a unique way. Djastiz uses base-ten by default (though any other base can be used fairly easily if one simply chooses words for digits above 9), and large numbers are expressed by listing their digits from largest power to smallest power, each digit followed by the word for its place. Fractions can be expressed with the word `igib`, and decimal points with `bajut`. For example, `daiau doze shauiz`, `toza aishep jopa kodid shauiz doze ketop`, `shauiz doze shauiz igib jopa`, and `eiesh bajut shauiz oposh abou toza oposh poiub abou suzut jopa`. Numbers larger than 9,999 can be expressed by saying things like `doze aishep aishep` for the 10,000,000 place, or simply in scientific notation (if I ever figure out how math works in this language).

`touk` is a bit of a meta-word. It tells the listener to ignore the previous few words spoken. This is used exclusively for error correction, so it rarely comes up in writing.

`je` is Djastiz's only contraction. It is short for `ju ped e`, and serves a very specific purpose. When `je` is followed by a single noun (note that modifiers and clauses may not be used here) and preposition, the phrase reads as `ju ped e`, the noun, the preposition, `sob up`. It is extremely useful for describing professions and objects associated with actions. For example, while Djastiz has no single word for "customer", `je pipez bu` works just fine. Note that while `je` is derived from `ju ped e`, they do not mean the same thing, as `je` also contains the `sob up` after the noun and preposition.

## Vocabulary

In the grammar section, we defined every word in the language save two groups: nouns and prefixes. Prefixes will be defined in a bit, but there are far too many nouns to list here - hundreds upon hundreds. Instead, I will lay out the tools to interpret new nouns and create one's own when necessary.

### Types of nouns

While all nouns behave the same way grammatically, an English-speaker perusing the list may believe that some do not belong under the category "nouns". To acknowledge the discrepancy between my and English's definition of "noun", I now explain the different kinds of nouns one might encounter and how they work.

First, there is the type of noun English-speakers are all familiar with - things like `oigut` and `atas`, which describe types of person place or thing. These are fairly self-explanatory, so I'll move on.

Next, there are nouns like `idauz` and `ditab`, which describe actions. "Actions&#8253;" I hear you shouting. "That sounds like the textbook definition of verbs to me! What's going on here?" to which I reply, "Shut up and let me finish. I just said my definition of 'noun' was different from English's, and I'm about to explain why, you obnoxious brat." As I was saying, these words describe actions, but grammatically, they behave the same as any other noun. They form noun phrases and complement prepositions. These words tend to complement `e` more than they do `bu` and `iu`, but any noun can complement any preposition, so long as the meaning is clear. Nouns in Djastiz all define concepts, even if some of those concepts are not usually described with "nouns". It should be noted that some nouns of this second group, notably `kishij` and `shiabu`, are quite apt at describing paths and positions when used inside noun clauses. For example, `poj e ugi si kit iu jaieddouiatkidash si ashebiapeu up`.

The third largest group of nouns is things along the lines of `pubuk` and `doziz`. These words describe qualities of objects and states, which seems okay to most English-speakers, but something must be said of the combination of these words with `e`. When a sentence contains a predicate that represents a quality of an object, it means that the subject possesses that quality, either to the extent designated by the `jeu` complement or to some implied high extent.

### Prefixes

While the existing nouns can describe a great many concepts and contexts given the rules outlined above, one will very frequently need words that are related to but different from existing words. One can describe a hot pan with `jaiedtuze dik pubuk`, for example, but how does one describe a cold pan? With `jaiedtuze dik iatpubuk`, of course! `iatpubuk` is an _expansion_ of `pubuk`, accomplished through the prefix `iat`. Prefixes modify words by preceding them and thus changing the meaning in some simple fashion. There are six of them.
- `zoj` changes a word to mean anything but its original meaning.
- `iat` changes a word to mean its opposite.
- `dou` changes a word to mean a more extreme version of its original meaning.
- `peig` changes a word to encompass a range of meanings similar to its original meaning.
- `guis` changes a word to refer to the maximum possible state of its original meaning.
- `tius` changes a word to denote the action or concept associated with its original meaning becoming true. For example, since `ozi` means "altitude", `tiusozi` means "rising".

Note that applying a prefix to a word creates a new word, not a phrase, and prefixes may not modify other prefixes. Therefore, any chain of prefixes should be evaluated last-first.

### Compound words

In addition to the basic words, both found in the dictionary and created by combining those with prefixes, there are thousands of _compound words_. Compound words are formed by simply combining two preexisting words. The meaning is closest to the first word, with the second word providing additional detail. Don't go thinking you can just slap any two words together willy-nilly, though! Compound words are an elite sect, and new ones can only be created with the consent of the entire Djastiz-speaking population (me). There is a list of existing compound words available for use; I just haven't written it out. Therefore, simply exercise your best judgement to decide when a compound word is probably appropriate.

### Technical nouns

It is a common practice among English-speaking practitioners of technical fields to, whenever a new phenomenon or concept is discovered or invented, simply take a word from colloquial English that describes it approximately and ascribe it a new, more specific and technical meaning. A fabulous example is, in physics, the concept of power, the time-derivative of energy ("derivative" and "energy" being two similarly defined words). Its meaning is somewhat similar to the colloquial meaning of "power", but really, the colloquial meaning of "power" is more accurately described as "control" or "chaos". This practice is called _overloading_, and I avoid it as much as possible.

Instead of forcing said practitioners to reuse words, Djastiz contains a cache of some 100,000 words specifically set aside for such usage. If you are a practitioner of a technical field and feel that a technical concept requires a word (or even if you think I missed a non-technical word), by all means, submit a pull-request! One person is not enough to fill this part of the dictionary.

### Causation and transitivity

It must be noted that, while in English, verbs often have multiple meanings for varying levels of transitivity (for example, the word "break" can mean either "to fall apart" or "to cause something else to fall apart"), in Djastiz, only the least transitive forms receive words. To describe a person causing something else to break, one must explicitly say, `poj e kepo iu kit e egai`. The purpose of this is to reduce ambiguity and redundancy. Two meanings are not necessary for this phenomenon, nor are two words. Furthermore, it prevents the occurrence of tritransitive and even potentially tetratransitive sentences (what if I were to mind-control your dog into forcing a child into making a vase break the plant inside it?), which would cause us to run out of argumentative prepositions. Therefore, if the transitivity of a Djastiz noun is unclear, always assume it to be as low as would make sense.

## Writing and pronunciation

Djastiz has a relatively simple written language. It uses a phonetic alphabet, and is written top-to-bottom, then left-to-right. There are 15 letters:
- `id` is Romanized "i" and pronounced 'i' in the [IPA][1].
- `e` is Romanized "e" and pronounced '&#603;' in the [IPA][1].
- `aj` is Romanized "a" and pronounced '&#592;' in the [IPA][1].
- `og` is Romanized "o" and pronounced '&#596;' in the [IPA][1].
- `up` is Romanized "u" and pronounced 'u' in the [IPA][1].
- `kush` is Romanized "k" and pronounced 'k' in the [IPA][1].
- `guz` is Romanized "g" and pronounced 'g' in the [IPA][1].
- `to` is Romanized "t" and pronounced 't' in the [IPA][1].
- `dik` is Romanized "d" and pronounced 'd' in the [IPA][1].
- `pi` is Romanized "p" and pronounced 'p' in the [IPA][1].
- `bu` is Romanized "b" and pronounced 'b' in the [IPA][1].
- `si` is Romanized "s" and pronounced 's' in the [IPA][1].
- `zai` is Romanized "z" and pronounced 'z' in the [IPA][1].
- `shau` is Romanized "sh" and pronounced '&#643;' in the [IPA][1].
- `ju` is Romanized "j" and pronounced '&#658;' in the [IPA][1].

The actual Djastiz character for each of these in svg format can be found in the "written language" folder of this repository. While there are no punctuation letter in Djastiz, words are separated by spaces of the same height as a letter. Compound words and expansions are single words and therefore do not contain spaces.

[1]: http://www.internationalphoneticalphabet.org/ "International Phonetic Alphabet"

## Gesturing

Hello

Goodbye


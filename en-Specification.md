# How to Speak Oltilip

This is the language specification for Oltilip, an international auxiliary language. Oltilip was designed to facilitate international communication across all humankind, and as such, is designed to be as neutral, elegant, and easy-to-learn as possible. Here you will find all of the information needed to learn and speak Oltilip, as well as some information about how Oltilip came to be. This document assumes that you speak English. If you're reading this, that seems like a pretty safe assumption.

## Disclaimer

Please do not actually learn this language. I created Oltilip to satisfy my personal desire for a language that _I_ thought was optimal. I publish it such that those who are interested can see my ideas and potentially gain something from them. However, were I to actually push it as a contender for the second language of humanity, it would be a waste of my time at best and another divisive factor in the already splintered auxlang community at worst. Therefore, I beseech that if you want to support the idea of an international auxiliary language by learning one and communicating with it, you look into [Elefen](elefen.org) or [Neo Patwa](http://patwa.pbworks.com/w/page/14800479/FrontPage) instead, as those are the two auxlangs other than my own that I currently favor most.

With that out of the way, let's get onto the language!

## Phonology and orthography

### Alphabet

Before you read any further, you'll need to know how to read, say, and write these words. Luckily, this is extremely easy. Oltilip uses only the seventeen sounds that are most common globally, each of which comes with a considerable amount of allowable variation. For example, while "pace", "base", and "Bess" sound different to most English speakers, all are acceptable pronunciations for Oltilip "pes", which means "fish". Approximately half of all humans can distinguish between all of these sounds in their native phonology, and only 5% need to learn three or more new sounds. The writing system is a simple Latin-derived alphabet with one letter for every sound. It's so simple that a wise man can acquaint himself with it before the hour is over; even a stupid man can learn it in the space of two days.

| Name | Symbol | Alt. Symbols | Sound (English) | Sound ([IPA](1)) | Alt. Sounds ([IPA](1)| Inverse | Class |
|------|--------|--------------|-----------------|------------|-------------|---------|----------
|   e  |   e    |    Є         |   **e**gg, fr**ay**  |     e     |  ɛ\~e\~ej   |    o    | V |
|   a  |   a    |    Ƌ, ɑ, α   |  t**a**co, h**a**ck  |     a     |    a\~ɑ     |    a    | V |
|   o  |   o    |    O         |  **oa**t, **o**rgan  |     o     |  ɔ\~o\~ow   |    e    | V |
|   i  |   i    |    I, ι      | **ea**t, scr**ee**ch |     i     |    ɪ\~i     |    u    | V |
|   u  |   u    |    U, v      |  fr**ui**t, **oo**ze |     u     |    ʊ\~u     |    i    | V |
|  yo  |   y    |    Y         |   so**y**, **y**ell  |     j     | i, ʲ, j\~ʝ  |    we   | G |
|  la  |   l    |    L         |  **l**ime, fa**ll**  |     l     |    l\~r     |    ta   | C |
|  we  |   w    |    W, ɯ      |  cho**w**, **w**eep  |     w     | u, ʷ, w\~ʋ  |    yo   | G |
|  na  |   n    |    Λ         | **n**ectar, pai**n** |     n     |   n, ŋ\~ɴ   |    ko   | C |
|  me  |   m    |    M         | **m**elon, screa**m**|     m     |      m      |    pe   | C |
|  ho  |   h    |    Һ         |  **h**oney, **h**ide |     h     |   x\~h, ɦ   |    co   | C |
|  co  |   c    |    C         |**ch**eese, **sh**riek|   t͡ʃ     |t͡ʃ\~t͡ʂ, ʃ\~ʂ |    ho   | C |
|  sa  |   s    |    S         |  **s**alt, hi**ss**  |     s     |      s      |    fe   | C |
|  fe  |   f    |    F         |  **f**ish, cou**gh** |     f     |    ɸ\~f     |    sa   | C |
|  ko  |   k    |    K         |  **c**ake, **g**rab  |     k     |  k, kʰ, ɡ   |    na   | C |
|  ta  |   t    |    T         |   **t**ea, **d**eep  |     t     |  t, tʰ, d   |    la   | C |
|  pe  |   p    |    P         |  **p**ear, **b**urst |     p     |  p, pʰ, b   |    me   | C |

The "Inverse" column is not that important; it just comes up later in the derivational morphology section. You don't have to learn that part if you don't want to.

If you're a linguist, the following [IPA](1) table may prove easier to read:

|               | Labial | Coronal | Palatal | Guttural |
|:--------------|:------:|:-------:|:-------:|:--------:|
|**Plosive**    |    p   |    t    |         |    k     |
|**Fricative**  |    f   |    s    |    c    |    h     |
|**Nasal**      |    m   |    n    |         |          |
|**Approximant**|    w   |    l    |    y    |          |

|         | Front | Back |
|:--------|:-----:|:----:|
|**Close**|   i   |  u   |
|**Mid**  |   e   |  o   |
|**Open** |   a   |      |

Most of the letters match their IPA transcriptions as well as their English counterparts. The only things of which to be careful are ⟨j⟩, ⟨c⟩, and the vowels. There's a handy alphabet song in the main repository to help you remember them all if you like.

Note that while all of these symbols come from the Latin alphabet, the Latin alphabet is _not_ the Oltilip alphabet. The basic Oltilip alphabet does not include ⟨b⟩, ⟨d⟩, ⟨g⟩, ⟨q⟩, ⟨r⟩, ⟨v⟩, ⟨x⟩, ⟨y⟩, ⟨z⟩, or any capital letters. _Some_ capital Latin letters are acceptable substitutes for their lowercase forms, as indicated by the alternate symbols column, but these are merely to allow stylistic variation, and carry no meaning different from their lowercase counterparts. Furthermore, note that unlisted capital letters are too different to be easily readable by Oltilip-speakers who are unfamiliar with the entire Latin alphabet, and thus should not ever be used.

[1]: http://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/ "International Phonetic Alphabet"

### Punctuation

In addition to this subset of Latin letters, a subset of other Latin symbols may be used with Oltilip to aid parsing. None of these are strictly required, but it is important to understand what they mean in case you come across them in Oltilip texts.

| Name | Symbol | Usage |
|------|--------|-------|
| katilon        |        | Separates words or clusters of digits in long numbers
| pelapas        | '      | Precedes a loanword
| tyen           | .      | Follows the last word of a sentence or the ones digit of floating point numbers
| tapamila       | ,      | Follows the last word before a brief pause
| tosak pelapas  | "      | Encloses a quotation
| nefwesak kiles | (      | Precedes the first word of an inset sidenote
| nefwesak nules | )      | Follows the last word of an inset sidenote
| fulopas        | \~     | Denotes a range between two values
| men            | -      | Denotes the subtraction of two values or stands for the word "men" ("negative")
| aw             | +      | Denotes addition of two values or stands for the word "aw" ("and")
| funtanyopas    | /      | Stands for the word "pel" ("divided by")
| nul            | 0      | Stands for the word "nul" ("zero")
| kan            | 1      | Stands for the word "kan" ("one")
| tos            | 2      | Stands for the word "tos" ("two")
| san            | 3      | Stands for the word "san" ("three")
| fol            | 4      | Stands for the word "fol" ("four")
| lim            | 5      | Stands for the word "lim" ("five")
| cah            | 6      | Stands for the word "cah" ("six")
| pit            | 7      | Stands for the word "pit" ("seven")
| hat            | 8      | Stands for the word "hat" ("eight")
| mes            | 9      | Stands for the word "mes" ("nine")
| tes            | A      | Stands for the word "tes" ("ten")
| tup            | B      | Stands for the word "tup" ("eleven")
| set            | C      | Stands for the word "set" ("twelve")
| fak            | D      | Stands for the word "fak" ("thirteen")
| lef            | E      | Stands for the word "lef" ("fourteen")
| nak            | F      | Stands for the word "nak" ("fifteen")

### Extensions

Finally, there are twenty-seven more letters that may be used for transcribing foreign names in Oltilip, though it is recommended that foreign names be Oltilipised into the seventeen basic letters when possible. The extensions here are only for cases where two related foreign words would be normally indistinguishable, or where the person named prefers that their name be pronounced with a particular phone. When these extensions are used, all Oltilip phonotactic restrictions are dropped. They fill out the simplified IPA tables below.

|                          | Labial | Alveolar | P.-alv.\~Retro. | Palatal | Velar\~Uvular | Phar.\~Glottal |
|--------------------------|--------|----------|--------------|---------|-------|---------|
|**Nasal**                 | m      | n        | n     | ŋy      | ŋ     |        |
|**Plosive/Implosive**     | p b    | t d      | t d   | ky gy   | k g   | ʔ      |
|**Affricate**             | pf bv  | ts dz    | tʃ dʒ | kxy gʀy | kx gʀ | ʔh     |
|**Fricative**             | f v    | s z      | ʃ ʒ   | xy ʀy   | x ʀ   | h ʕ    |
|**Lateral fricative**     | lf lv  | lh lʒ    | lh lʒ | lx lʀ   | lx lʀ |        |
|**Approximant**           | w      | ɹ        | ɹ     | y       | ɯ     | ʕ      |
|**Lateral approximant**   | lw     | l        | l     | ly      | lɯ    |        |
|**Tap/Trill**             | ʙ      | r        | r     |         | ʀ     |        |
|**Click**                 | !      | !        | !     | !       | !     |        |
|**Secondary articulation**| tw     | tɹ       | tɹ    | ty      | tʀ    | tʔ     |

|             | Front | Central | Back |
|-------------|-------|---------|------|
|**Semivowel**| y ɥ   | y w     | ɯ w  |
|**Close**    | i ɥ   | ɨ ʉ     | ɯ u  |
|**Mid**      | e ø   | ə ə     | ɤ o  |
|**Open**     | a ɒ   | a ɒ     | a ɒ  |

| Feature | Symbol | Feature | Symbol |
|-------------------|----|----------|----|
|**Voiceless**      | nh |**Stress**| ˈ  |
|**Aspirated**      | th |**Long**  | əə |
|**Rhoticity**      | əɹ |**High**  | ˥  |
|**Nasalised**      | eŋ |**Mid**   | ˧  |
|**Nasal release**  | dn |**Low**   | ˩  |
|**Lateral release**| dl |

### Phonotactics

Oltilip generally follows a simple yet permissive (C)(G)V(G)(C) syllable structure, where any letter can appear in any position according to its class. The only restrictions are the disallowance of double letters and the clusters "ey", "ow", "iy", "uw", "yi", and "wu" within roots. These restrictions are dropped for compound words, where such combinations may arise at morpheme boundaries, and loanwords, where root recognition is more highly valued. The one root that defies this syllable structure is the pronoun "l", which can be analysed as a syllabic consonant. However, because it is syntactically always adjacent to a consonant, it need never be pronounced as such. All nouns, pronouns, numerals, and postpositions end with consonants, while verbs and sentence particles end with vowels.

Note that while "w" and "y" are morphologically distinct from "u" and "i", they never contrast, so speakers of languages without glides in medial positions can use vowels instead.

Stress always falls on the penultimate vowel of a word, unless the IPA extensions are used and a stress marker indicates otherwise.

## Grammar

The grammar of Oltilip can be characterised as an analytic, active-stative, head-final system with free word order. In a nutshell, it can be described as:  

            sentence ::= \[sentence-particle\] postposit-phrase\* \[verb-phrase postposit-phrase\*\]
    postposit-phrase ::= noun-phrase postposition
           predicate ::= verb+
         noun-phrase ::= \[specifier\] (noun \| pronoun \| numeral \| relative-clause \| sentence \| noun-phrase)\*
     relative-clause ::= postposit-phrase\* \[verb-phrase postpos-phrase\*\] \["l" postposition\]
             numeral ::= \[numeral "imal"\] \{\["men"\] digit+\] \["lyon" numeral\]

Don't know what any of that means? Don't worry. Let's jump into it now.

### Sentence particles

A _sentence particle_, when included, is the first thing in a sentence or clause. It specifies the mood of that clause: whether it's a statement, a question, etc. There are six.
- **"sa"** marks a declarative sentence, or indicates acknowledgement when used alone;
- **"cu"** marks an interrogative sentence, or indicates confusion when used alone;
- **"na"** marks an imperative sentence, or indicates an implied command when used alone;
- **"pana"** marks a polite imperative sentence, or indicates an implied request when used alone;
- **"wa"** marks an exclamatory sentence, or indicates surprise when used alone; and
- **"ke"** marks a subordinate clause.

When these are used to mark sentences and clauses, the rest of the phrase comprises a series of _postpositional phrases_, optionally with a _predicate_ included.

### Postpositional phrases

Every postpositional phrase describes one aspect of the event or state described by the clause, and comprises two parts: the _complement_, which is a _noun phrase_, and the _postposition_, which is drawn from the following list of fifteen. The postposition specifies what aspect of the clause is being described, and the complement describes that aspect. These postpositional phrases may occur in any order. Postpositions can be categorised into two types

_Adjunctive postpositions_ have complements with predictable and general meanings, and can be used with any predicate, or multiple times with the same predicate if used in different contexts (e.g. using "yot" once for location in virtual space and again for location in physical space). There are eight of these.
- **"yan"** marks the extent or quantity of the action, either as a numeral or another noun against which to compare;
- **"yot"** marks the location of the action;
- **"wel"** marks the date or time of the action;
- **"ial"** marks the cause or purpose of the action;
- **"uat"** marks the tool or medium of the action;
- **"ayf"** marks the hypothetical conditions surrounding the action (like "if" in English);
- **"ip"** marks the manner or method of the action, usually as a suborditate clause; and
- **"ak"** marks something that is related to the action in some other way.

_Argumentative postpositions_ have complements with meanings specific to their predicate, and can only be used once per clause. The definition of each Oltilip verb describes which argumentative postpositions are applicable and what roles they mark, but they can generally be qualified as three classes of semantic role.
- **"es"** marks the agent, the entity that initialises and carries out the action;
- **"on"** marks the patient or experiencer, the entity whose state is changed or described by the action; and
- **"um"** marks the theme or stimulus, an entitty that is not directly involved in the action but is essential to it nonetheless.

When adjunctive postpositional phrases are included or omitted, it often appears to change the meaning of a sentence's English translation. This is because Oltilip uses the same word for what English treats as transitive and intransitive pairs of verbs. For example, the verbs for "enter" and "insert" are both "neki" in Oltilip; "it enters" is "et on neki", and "I insert it" is "min es et on neki".

### Predicates

The predicate of a clause describes the action or state being described in the most general sense. It usually comprises a single _verb_. In Oltilip, verbs do not conjugate for tense, aspect, or anything else, so "et es nyama" can mean "they had eaten", "they ate", "they are eating", "they eat", or "they will eat". Therefore, if the time of a predicate is important, make sure to manually and specifically include it with "wel".

More complex predicates can be formed by appending other verbs, which serve as auxiliary verbs. This is only valid for verbs that take clauses as arguments, such as "nyo", "ki", "nu", "calu", "powi", and "tewi". For example, since the sentence "et es pola min on" means "they speak to me", appending "nyo", "be false", to the predicate turns it into "et es pola nyo min on", which means "they do not speak to me". This is shorthand for subordinating the entire sentence to "nyo": "et es pola min on on nyo" translates to "it is false that they speak to me".

Unlike in most languages, the predicate can also be completely omitted in Oltilip. When it is, it can usually be inferred to be either the predicate of the last sentence or the copula "esta".

### Noun phrases

Noun phrases are the primary building blocks with which one describes complex concepts. There are many ways to construct these.

The first, and by far the simplest, is a _noun_. Each one describes an instance or instances of a concept or class of things. In Oltilip, nouns do not decline for number, gender, or anything else, so "won" can mean "people", "women", "men", "the person", "a woman", or "every man". Therefore, if the quantity or quality of a noun phrase is important, make sure to manually and specifically include it with the mechanisms described below.

Anywhere a noun can be used, one can also opt for a _pronoun_. Like nouns, Oltilip pronouns do not decline at all; most solely indicate person or definiteness. Some of them are fairly common and intuitive, while others are more complicated.
- **"min"**, "me", is the first person pronoun;
- **"puk"**, "you", is the second person pronoun;
- **"et"**, "it" or "that", is the third person, distal, and definite pronoun;
- **"ol"**, "this", is the proximal pronoun;
- **"wan"**, "one", is the indefinite pronoun;
- **"sif"**, "oneself", is the reflexive pronoun;
- **"kulan"** refers to the next item in the implied series;
- **"nitak"** refers to the previous item in the implied series;
- **"kon"** stands in for missing information in interrogative sentences; and
- **"l"** stands for the referenced noun in relative clauses.

_Relative clauses_ are another kind of noun phrase, and the most versatile. A relative clause is simply any clause, optionally using "ke" as its particle, with "l" optionally inserted as a noun as late as possible in it. It describes anything that could go where "l" is in a full sentence. This is commonly used with stative verbs such as "luci", which means "be red". Since "luci et on" means "it is red", "ke luci l on" or "luci l on" means "one that is red", or "red thing". It is also frequently used with the vague postposition "ak". Since "ciuh ak on et" describes some state of "it" generally related to plants, "ke ciuh ak l on" or "ciuh ak" means "one that is of or related to plants" or "botanical".

A similar but distinct kind of noun phrase is the _content clause_. A content clause is syntactically equivalent to a sentence, except that when it takes a patricle, it always take "ke". Semantically, it references the action or state described by that sentence as a noun. This structure is especially useful for verbs like "calu", "continue", which almost always take content clauses as arguments. The sentence "puk es nyama", "you eat", can be converted into a content clause and used as such as in "puk es nyama on calu": "you eating continues". This can equivalently be phrased as "puk es nyama calu", "you continue to eat".

Similar to pronouns are _numerals_, which specifically indicate the number of a noun phrase. They have special derivation rules and are therefore described in the next subsection.

Any noun phrase can also be preceeded by a specifier. Specifiers manipulate the meanings of noun phrases that describe sets, and each works in a pretty distinct way.
- **"en"**, "any", indicates that the sentence is true for one element of the noun phrase, regardless of which one is picked;
- **"ok"**, "each", indicates that the sentence is true for every element of the noun phrase individually;
- **"alkun"**, "some", specifies that the sentence is true for some subset of the noun phrase;
- **"sol"**, "only", indicates that the sentence is true for the given noun phrase and nothing else;
- **"ifen"**, "even", emphasises a noun phrase that is surprising or especially important;
- **"yo"** optionally starts a conjunctive phrase; and
- **"aw"** separates elements of a conjunctive phrase.

Conjunctive phrases combine noun phrases that reference different things into a single noun phrase. It takes the form "myawf aw pawaf aw pes" or "yo myawf aw pawaf aw pes". The exact meaning of the conjunction "aw", like that of the modern English "-slash-", is ambiguous. It can be made more specific by prepending "ok" or "kit" before the "yo" for an analogue to English's "and", or prepending "en", "kan", or "kon" for an analogue to English's "or".

Finally, noun phrases of all kinds can also be concatenated to form more specific ones. When two noun phrases are combined, the resulting meaning is the intersection of both. For example, it is not uncommon for a noun phrase to comprise a pronoun for its definiteness, a numeral for its number, multiple nouns for its class and gender, and a relative clause for added specificity, as in "ifen et tos supot myawf muti l on", "even the two orange tomcats".

### Numerals

The last Oltilip part of speech is the numeral. Oltilip contains many mechanisms for describing numbers in precise mathematical ways. However, for the non-mathemetician, most of this is unnecessary. Luckily, basic numbers are also extremely easy to construct. The ten basic numerals are the digits from zero to nine.

| Symbol | Word |
|-----|-----|
|  0  | nul |
|  1  | kan |
|  2  | tos |
|  3  | san |
|  4  | fol |
|  5  | lim |
|  6  | cah |
|  7  | pit |
|  8  | hat |
|  9  | mes |

Numbers larger than nine are described in positional notation, either with or without spaces:

| Symbol | Word |
|-----|--------|
|  10 | kannul |
|  11 | kankan |
|  12 | kantos |
|  20 | tosnul |
|  21 | toskan |
| 100 | kannulnul |
| 1 000 | kan nulnulnul |

This can quickly become unweildly for large orders of magnitude. For that reason, the prefix "lyon" exists. Appending to an existing numeral "lyon" plus another numeral raises its order of magnitude by the second amount. Thus, "lyon" can be translated as "times ten to the power" or "×10^". So where "kan lim" means "fifteen" and "tos" means "two", "kan lim lyon tos" means "fifteen times ten to the power two", "fifteen hundred", or "1 500". "lyontos" can also be used on its own to simply mean "one hundred".

For numbers smaller or more precise than one, the particle "tyen" serves as the radix point. "tyen lim" means "point five", "cah tyen tos hat" means "six point two eight", and "fol tyen nul" means "four point zero".

While it can usually be assumed that this is all in base ten, the system itself is radix-independent. To specify a radix, the base plus the suffix "imal" can be prepended to the number. Digits exist for bases up to 17<sub>10</sub>.

| Symbol | Word |
|-----|-----|
|  A  | tes |
|  B  | tup |
|  C  | set |
|  D  | fak |
|  E  | lef |
|  F  | nak |
|  G  | hes |

Thus, while "kan nul" usually means "tesimal kan nul", the atomic number of neon, it can also be made to mean "cahimal kan nul", the atomic number of carbon, "hesimal kan nul", the atomic number of sulfur, or even "tesimalcahnulimal kan nul", the atomic number of neodymium.

Negative numbers are formed by simply prepending "men" to their opposite, as in "men san". These can also be used with "lyon", as in "hat tyen mes lyon men kan tos". When it is useful to emphasize the sign of a positive number, this can be done with the otherwise meaningless prefix "pok", as in "pok kan aw men kan".

Fractions are formed with the separator "pel", which simply divides the numeral before it by the numeral after it. For example, "tostos pel pit". If no number precedes the "pel", then the numerator can be assumed to be one.

Finally, three subjective numerals exist for some situations when a number would not typically be used in English.
- **"pih"** means some small quantity;
- **"muc"** means some large quantity; and
- **"kit"** means the maximum possible quantity given the context.
These can be used in tandem with other numbers, as in "muc nul nul" for "many hundreds", but are usually used alone, often followed by the postposition "yan".

All numbers can be converted from cardinals to ordinals by appending "-ak".

### Do no wrong principle

The most important rule in Oltilip is that there are no rules. While the grammar here was designed to be as flexible as possible specifically to reduce the number of ways speakers can be wrong, it is still trivial and tempting to bend the rules. If you say something that does not precisely fit into the grammar outlined here, but it is still understandable within that framework, then you are correct. Oltilip is a means of communication, and as long as you are communicating to anyone else who has read this document, then you are speaking Oltilip.

### Tips and tricks

That's all of the official grammar. You may find it rather short. "Where are the tenses, the participles, the directionals?" you ask. While these do not exist explicitly in Oltilip, they can be expressed using preexisting structures. Therefore, while their inclusion here is not strictly necessary, I will explain them so that everyone understands best practices for such situations without needing ccome up with them themselves.

Tenses are simple. If it is important to a sentence whether it happened in the past, present, or future, the dative postposition "wel" can be used with the appropriate word. For generic past and future tense, "citu wel" and "huli wel" are the recommended forms.

Participles in Oltilip are usually unnecessary, as verbs resulting in state changes are usually derived from the state, and not the other way around. While the verb for "burn" is "cyauki", the English participle "burnt" simply translates to "cyau", "be burnt". In cases that cannot be handled with the removal of a suffix, relative clauses can serve the purpose of participles. Say one really needs to describe something that has recently been burned, and not just something burnt. The phrase "cyauki l on", "one that is burned", or more specifically "citu wel cyauki l on", "one that was burned", will serve that purpose well.

Adverbs in English come in two flavours: things like "quickly" and things like "hopefully". Adjectives-turned-adverbs like "quickly" are derived in Oltilip by simply using stative verbs along with the postposition "ip": "yala ip" means "in the manner of being quick". The second type, which really modifies an English sentence more than its verb specifically, typically mandates rephrasing: "I will hopefully get paid" becomes "I hope that I receive money", which is "min on cai ke min on tueki mailuat um um".

Directionals, usually realised in English with phrasal verbs as in "run away" or "sit down", are also translated using "ip", along with directional Oltilip verbs. The word for "run" is "fepucocalu", and the word for "go away" is "kuleki", so "run away" is simply "kuleki ip fepucocalu". Similarly, "sit down" is "pahoki ip swo".

Adpositions and cases describing location and motion like "atop" and "toward" are achieved through subordinate clauses passed to the postposition "yot". The sentence "they stand atop the mountain" translates to "et on upe pil um mace yot", literally "they stand in the place that is to be above the mountain". The sentence "you swim toward the island" translates to "puk on cwehila pihtayl um nitoki yot", literally "you swim in the place that is to approach the island". Similar temporal adpositions can be translated with "wel": "I will sleep until noon" translates to "min on tolmi nefuhalwel um kitcitu wel", literally "I sleep at the time that is being until noon".

The verb "to have", as you may notice, is missing from Oltilip's dictionary. The verb "tue" can be translated as "have", but that only applies to possession, and not to "have" as in "I have a sibling". Instead the verb "esta" should be used with the postposition "ak": "min ak esta pemamalon on", literally "a sister exists in a way that somehow involves me".

The verb "to need" is similarly absent from the vocabulary. The verb "cai", which literally means "want", can be used in many contexts where "need" would be used in English. However, true necessity as in "humans need food to survive" should be rephrased as a conditional: "won on nyamalon um tue nyo ayf, uhuki", literally "if humans don't have food, they die".

Dates and times in Oltilip can be expressed several ways. For maximal unambiguity, one would use the Oltilip equivalent of "on the fifty-sixth minute of the second hour of the twenty-first day of July": "pitak fikkwelwel ak toskanak sunkwelwel ak tosak tapakwelwel ak limcahak kankwelwel wel". Note that hours, minutes, and seconds index from zero by convention, and that months in Oltilip do not have names. This can all be shortened substantially by separating the date and time with a comma, and removing the units of the day, hour, minute, and second. This is analogous to the more common "on July twenty-first, two-fifty-six": "pitak fikkwelwel ak toskan, tos ak limcah wel".

## Vocabulary

Oltilip has 426 basic roots, drawn from Chinese, Italic, Germanic, Indo-Iranian, Atlantic-Congo, Malayo-Polynesian, Esperanto, and onomotopoetic lexicons. The source languages were selected and weighted in order to give the most mnemonic value to the greatest number of people. While these root words cover many concepts, with only 426, there are inevitably many lexical gaps and ambiguities. These are filled with Oltilip's morphological derivation system. New words are derived in three main ways: _inversion_, _compounds_, _affixes_, and _loans_.

### Inversion

Inversion is by far the least intuitive and most unique of the four. It is used to derive antonyms and opposites of verbs and nouns. For example, the word for "to be near", "nito", is derived by inverting the word for "to be far", "kule". This is accomplished by simply replacing every letter in "kule" with its inverse letter, as specified in the phonology table above. The "ke" goes to "na", the "u" goes to "i", the "la" goes to "ta", and the "e" goes to "o".

### Compound words

A more standard way to form a new word is with a simple compound. This involves combining two or more existing words to form a new one. It takes the part of speech of the second, and represents something between the meanings of both. For example, "pahopoltilum", meaning "underwear", is derived from "paho", meaning "to be under", and "poltilum", meaning "clothing".

### Affixes

A more precise way to derive new terms is through the addition of affixes. In Oltilip, all affixes are themselves words, and the result of adding one means the same thing as the base word and affix placed together in a sentence, albeit lexicalised. For example, if the relative "l es" is placed next to the verb "noki", which means "to teach", one gets "noki l es", which means "one who teaches". When "les" is used as a suffix, that phrase is lexicalised into "nokiles", which means "teacher". This form carries two concrete advantages over the phrase "noki l es"; specifically, "nokiles" cannot be misinterpreted as unconnected words in adjacent phrases should the surrounding grammar be complicated, and further can refer to the concept of a teacher even when there is no one in the discussion who is actively teaching. Learning a word like "nokiles" is also easier than repeatedly parsing a phrase like "noki l es".

There are ten suffixes that can turn verbs into nouns:
- **"-les"** references the agent of a verb, similar to "-er" in English;
- **"-lon"** references the patient of a verb, similar to "-ee" in English;
- **"-lum"** references the theme of a verb;
- **"-lyan"** references the extent to which a verb takes place;
- **"-lwel"** references the time at which a verb takes place;
- **"-lyot"** references the location at which a verb takes place;
- **"-lial"** references the cause because of which a verb takes place;
- **"-luat"** references the instrument by which a verb takes place; and
- **"-lip"** references the way in which a verb takes place.

There are four suffixes that can turn verbs into other verbs:
- **"-nyo"** describes the negative of a verb, similar to "non-" in English;
- **"-ki"** describes the inception of a verb, similar to "-ise" or "-en" in English;
- **"-nu"** describes the cession of a verb, similar to "de- -ise" or "un- -en" in English;
- **"-powi"** describes the potential of a verb, similar to "-able" or "-ible" in English; and
- **"-calu"** describes the continuation of a verb, similar to "-ing" in English.

Finally, there is one suffix that turns nouns into other nouns:
- **"-ak"** describes anything of or related to a noun, similar to "-al", "-ic", or "-'s" in English.

### Loanwords

For words that describe deeply technical concepts like "deoxyribonucleic acid", cultural concepts like "ahupua&#8216;a", or a combination of the two like "oriental ladyfern", a class of word that is neither root nor compound is needed. This is the _loanword_, a word taken directly from a specific language. The word should be taken from a language that has regional or historical ties to the concept. For example, the word for "persimmon", "'kaki", comes from the Japanese "柿" /kaki/, due to the persimmon's historical and economic ties to Eastern Asia.

Because these words have fewer phonotactic restrictions than base words, they may be marked with an apostrophe to distinguish them, much as italics are commonly used in English. Even with the looser restrictions, Oltilip's small phonology often forces loanwords to differ from their sources substantially, as "'fahanse" does from "France" /fʀɑns/. This is a worthwhile trade-off for the learnability of the phonology.

Loanwords are especially common as toponyms. The word for "Japan", "'nipon", comes directly from the Japnese word "日本" /nipːoɴ/. These are commonly compounded to form related words, such as "'niponwon" for "Japanese person", "'nipontilip" for "the Japanese language", and "'niponkwelyot" for "the Japanese archipelago". While it is less common, an ethnonym can also serve as the root off of which the toponym is derived, depending on the etymology of the endonym. For example, from "'alap" for "Arab", we get "'alaptec" for "Saudi Arabia", "'alaptilip" for "Arabic", and "'alapkwelyot" for "the Arabian peninsula".

## Common phrases

Here are some useful expressions in Oltilip.

| English | Oltilip |
|:--------|:--------|
| Hello. | wa cai. |
| Good morning. | wa fuhakilwel. |
| Good day. | wa fuhalwel. |
| Good evening. | wa sicakilwel. |
| Goodbye. | wa cai. |
| Good night. | cai ip tolmi. |
| Yay! | wa cai. |
| Fuck! | wa hau. |
| Welcome. | pana neki. |
| Please. | pana. |
| Thank you. | kanci. |
| You're welcome. | wawi nyo. |
| I'm sorry. | suotu. |
| Excuse me. | pana oketi. |
| You're excused. | sa oketi. |
| Is it okay? | cu oke. |
| It's okay. | sa oke. |
| What is your name? | puk um co kon on. |
| My name is "Chka-chka Slim Shady" | min um co "'cikacikaslimceyti" on. |
| I know a little Oltilip. | min on pih yan oltilip on no. |
| Please speak slower. | pana wata ip pola. |
| Where is the bathroom? | pukak mamalon on seksomailes um. |

## Flag

[The flag of Oltilip](https://github.com/jkunimune15/Djastiz/blob/international-djastiz/Flag.svg) is a white and azure bicolour, divided by a sinusoid. In the center, it bears an orange six-pointed star circumscribed by an azure and white circle. The white field represents peace, which Oltilip could facilitate, while the azure represents knowledge, which Oltilip could proliferate. The boundary between them is a sinusoid instead of the traditional straight line to represent the fluidity of Oltilip's grammar, and its free word order in particular. The circle represents the Earth---blue, white, and circular. The star both separates it into six sections, for the six continents, and bridges the gap between them. It represents both natural languages, which divide us, and Oltilip, which can link us together.

# Appendices

## Dictionary


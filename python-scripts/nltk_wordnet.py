#!/usr/bin/env python3
from nltk.corpus import wordnet

syns = wordnet.synsets("store")

# synset
print(syns)

# definition
print(syns[0].definition())

# the word
print(syns[0].lemmas()[0].name())

# example(s)
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
    if l.antonyms():
        antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))


# semantic similarity %
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("bat.n.01")
print(w1.wup_similarity(w2))

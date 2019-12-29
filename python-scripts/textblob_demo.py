#!/usr/bin/env python3
from textblob import TextBlob
blob = TextBlob(
    "Alexander was not useful at all. The cloud server is still not working. The team should work on this item again please. I think you are able to resolve it on a short period of time. But maybe we need to call to another help desk, a better with stronger support in this kind of incidents.")
# Sentences are a python list by default
print(type(blob.sentences))
print(len(blob.sentences))
# Words are not a python list by deaulf, you need to cast them to list
wordList = list(blob.words)
print(type(wordList))
print(len(wordList))
print(blob.noun_phrases)
# Noun phrases count returns a defaultdict but you can turn it to a dict
print(dict(blob.np_counts))
# Polarity score
print('All sentences polarity: ', blob.polarity)
print('All sentences sentiment: ', blob.sentiment)
# Polatity by sentence
for i, sentence in enumerate(blob.sentences):
    print('Sentence polarity', i+1, ':', sentence.polarity)
    print('Sentence sentiment', i+1, ':', sentence.sentiment)

print(blob.translate(to='es'))

print(blob.ngrams(n=3))

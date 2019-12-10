#!/usr/bin/env python3
import nltk
import random
from nltk.corpus import movie_reviews

# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories() for fileid in movie_reviews.fileids()]

documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words).most_common(3000)

word_features = [a for (a, _) in all_words]
# print(word_features)


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

features_set = [(find_features(rev), category)
                for (rev, category) in documents]

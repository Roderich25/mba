#!/usr/bin/env python3
import nltk
import random
from nltk.corpus import movie_reviews


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories() for fileid in movie_reviews.fileids()]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

feature_sets = [(find_features(rev), cat) for (rev, cat) in documents]

trainning_set  = feature_sets[:1900]
testing_set =  feature_sets[1900:]

# posterior = prior_ocurrences * likelihood / evidence
 
classifier = nltk.NaiveBayesClassifier.train(trainning_set)
print("NB accuracy", nltk.classify.accuracy(classifier, testing_set))
print(classifier.show_most_informative_features(10))
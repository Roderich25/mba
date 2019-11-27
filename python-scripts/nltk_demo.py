#!/usr/bin/env python3
# import nltk
# nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_text = '''Hello there Mr. Ávila, how are you?
                The weather is great and python is awesome.
                And the sky is blue.
                This is an example showing off stopwords filtering.
                '''

stop_words = set(stopwords.words('english'))
print(stop_words)
for sentence in sent_tokenize(example_text):
    print(sentence)

words = word_tokenize(example_text)

# filtered_words = []
# for w in words:
#     if w not in stop_words:
#         filtered_words.append(w)
# print(filtered_words)

filtered_words = [w for w in words if w not in stop_words]
print(filtered_words)

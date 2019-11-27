#!/usr/bin/env python3
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# example_words = ["python", "pythoner", "pythoning",
#                  "pythoned", "pythonic", "pythonly"]

# words_stem = [ps.stem(w) for w in example_words]
# print(words_stem)

sent = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(sent)
for w in words:
    print(ps.stem(w))

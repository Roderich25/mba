#!/usr/bin/env python3
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

# print(nltk.__file__)

sample_text = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample_text)
print(tok[5:12])

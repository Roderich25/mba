#!/usr/bin/env python3
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

"""
NE Type and Examples:

ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
"""


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged, binary=True)
            # namedEnt.draw()
            named_entities = []
            for tagged_tree in namedEnt:
                # print(tagged_tree)
                if hasattr(tagged_tree, 'label'):
                    entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
                    entity_type = tagged_tree.label()  # get NE category
                    named_entities.append((entity_name, entity_type))
            # print(named_entities)
            for tag in named_entities:
                if tag[1] == 'GPE':  # Specify any tag which is required
                    print(tag)

    except Exception as e:
        print(str(e))


process_content()

from collections import abc
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'


s = Sentence("Alpha Bravo Charlie Delta Echo Foxtrot")
print(s.words)
print(s[-1])
print(len(s))
print(s)

for w in s:
    print(w)

print(list(s))

print(issubclass(Sentence, abc.Iterable))
print(isinstance(s, abc.Iterable))

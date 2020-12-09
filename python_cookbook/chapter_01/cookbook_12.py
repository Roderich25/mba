

# 1.12 Determining the most frequently ocurring tems in a sequence

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes',    'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
print(word_counts)

top_three = word_counts.most_common(3)
print(top_three)

# number of ocurrences
print(word_counts['not'])
print(word_counts['eyes'])

# incrementing counts manually
more_words = 'why are you not looking in my eyes'.split(' ')
for word in more_words:
    word_counts[word] += 1

print(word_counts['not'])
print(word_counts['eyes'])

# another example | using `update` method
word_counts.update(more_words)
print(word_counts)

# another example | combining Counter's
a = Counter(words)
b = Counter(more_words)
print(a)
print(b)

c = a + b  # adding
print(c)

d = a - b  # substracting
print(d)

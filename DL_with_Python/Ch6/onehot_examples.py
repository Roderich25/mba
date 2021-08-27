import numpy as np
import string
from keras.preprocessing.text import Tokenizer

samples = ['The cat sat on the mat.', 'The dog ate my homework']


# Word-level onehot encoding

token_index = {}

for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = 1 + len(token_index)
print(token_index.items())
max_length = 10
results = np.zeros(shape=(len(samples),
                          max_length,
                          1 + max(token_index.values())
                          )
                   )


for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1.
print(results)


# Character-level onehot encoding

characters = string.printable
token_index = dict(zip(characters, range(1, 1 + len(characters))))
print(token_index)

max_length = 50
results = np.zeros(shape=(len(samples),
                          max_length,
                          1 + max(token_index.values())
                          )
                   )
for i, sample in enumerate(samples):
    for j, character in enumerate(sample):
        index = token_index.get(character)
        results[i, j, index] = 1.


print(results)


# Using Keras word-level onehot encoding
tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(samples)

sequences = tokenizer.texts_to_sequences(samples)

one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')

word_index = tokenizer.word_index

print(f'Found {len(word_index)} unique tokens:')
print(word_index)
print(one_hot_results)


# Word-level onehot encoding with hashing-trick

dimensionality = 100
max_length = 10
results = np.zeros((len(samples), max_length, dimensionality))
for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = abs(hash(word)) % dimensionality
        print(word, index)
        results[i, j, index] = 1.
print(results)

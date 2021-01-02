

# 2.14 Combining and concatenating strings

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(', '.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a, b))

c = 'Hello' 'World'
print(c)


# DON'T DO THIS: slower and inefficient due to memory copies and garbage collection
s = ''
for p in parts:
    s += p
print(s)


# another example
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))  # Still ugly
print(a, b, c, sep=':')  # Better


# version 1 (string concatenation)
# f.write(chunk1 + chunk2)

# version 2 (separate I/O operations)
# f.write(chunk1)
# f.write(chunk2)

# If the two strings are small, the first version might offer much better performance.
# If the two strings are large, the second version may be more efficient.

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())
print(text)

# redirect fragments to I/O
# for part in sample():
#   f.write(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    # f.write(part)
    print(part)

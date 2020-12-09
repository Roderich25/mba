

# 1.6 Mapping keys to multiple values in a Dictionary

from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
print(d)


e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['a'].add(3)
e['b'].add(4)
e['b'].add(5)
print(e)


# another way to do the same
d = {}  # aregular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(3)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(5)
print(d)

e = {}
e.setdefault('a', set()).add(1)
e.setdefault('a', set()).add(2)
e.setdefault('a', set()).add(3)
e.setdefault('b', set()).add(4)
e.setdefault('b', set()).add(5)
print(e)

# another example
pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# instead of this:
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

# do this:
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

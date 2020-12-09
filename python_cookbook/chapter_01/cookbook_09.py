

# 1.9 Finding commonalities in two dictionaries

a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

# keys in common
print(a.keys() & b.keys())

# keys in a but not in b
print(a.keys() - b.keys())

# key,value pairs in common
print(a.items() & b.items())

# new dictionary with keys removed
c = {key: a[key] for key in a.keys()-{'z', 'w'}}
print(c)

# `keys` and `items` methods support set operations but `values` method don't

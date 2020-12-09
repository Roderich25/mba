

# 1.10 Removing duplicates from a sequence while mainteining order

def dedupe1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe1(a)))  # only works if items are hashable

# dedupe for unhashable types


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


b = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4},
]

print(list(dedupe2(b, lambda d: (d['x'], d['y']))))
print(list(dedupe2(b, lambda d: d['x'])))


# another example | eliminating duplicates
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))  # but it doesn't preserve the order

# another example | dedupe2 is general purpose
with open('somefile.txt') as f:
    for i, line in enumerate(dedupe2(f)):
        print(f'#{i:02} {line}', end='')

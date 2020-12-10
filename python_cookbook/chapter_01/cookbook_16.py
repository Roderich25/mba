

# 1.16 Filtering sequence elements

from itertools import compress
import math
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# list comprehesion, avoid for large results
pos = [n for n in mylist if n > 0]
print(pos)

neg = [n for n in mylist if n < 0]
print(neg)

# generator expression
pos = (n for n in mylist if n > 0)
print(pos)
for p in pos:
    print(p)

# using `filter`
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
    except ValueError:
        return False
    else:
        return True


ivals = list(filter(is_int, values))
print(ivals)

# another example
mylist_sqrt = [math.sqrt(n) for n in mylist if n > 0]
print(mylist_sqrt)

# another example
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

# another example
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 N ADDISON',
    '4801 N BROADWAY',
    '1039 N GRANDVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)
output = list(compress(addresses, more5))
print(output)



# 1.19 Transforming and reducing data at the same time

import os

nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)

# another examples

files = os.listdir()
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python!')


s = ('ACME', 50, 123.45)
print(', '.join(str(x) for x in s))


portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)


s = sum((x*x for x in nums))  # pass generator expression as argument
s = sum(x*x for x in nums)  # more elegant syntax
# using list comprehension, avoid with large list not efficient
s = sum([x*x for x in nums])


# Original: returns 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# Alternative: returns {'name':'AOL', 'shares':20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)

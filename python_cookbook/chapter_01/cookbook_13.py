

# 1.13 Sorting a list of dictionaries by a common key
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
# `itemgetter` runs a little bit faster than using lambda expressions
# rows_by_lfname = sorted(rows, key=lambda d: (d['lname'], d['fname']))
# print(rows_by_lfname)

# another example
min_row = min(rows, key=itemgetter('uid'))
max_row = max(rows, key=itemgetter('uid'))
print(min_row)
print(max_row)

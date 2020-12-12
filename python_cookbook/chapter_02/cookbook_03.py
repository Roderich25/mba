

# 2.3 Matching strings using shell wildcard patterns
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.TXT'))

addresses = [
    '5412 N CLARK ST',
    '5148 N CLARK ST',
    '5800 E 58TH',
    '2122 N CLARK AVE',
    '5645 N RAVENSWOOD',
    '1060 N ADDISON ST',
    '4801 N BROADWAY',
    '1039 N GRANDVILLE AVE'
]
print([addr for addr in addresses if fnmatch(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9]*CLARK*')])

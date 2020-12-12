

# 2.2 Matching text at the start or end of a string
import os
import re
from urllib.request import urlopen


filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# filenames = os.walk('.')
# for root, dirs, files in filenames:
#     for f in files:
#         print(os.path.join(root, f))
filenames = [os.path.join(root, f)
             for root, dirs, files in os.walk('.') for f in files]
somefiles = [name for name in filenames if 'cookbook_0' in name]
print(somefiles)
print(all(name.endswith('.py') for name in somefiles))


# another example
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
test = url.startswith(tuple(choices))
print(test)


# another example | using slices
filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')


# another example | using regular expressions
url = 'http://www.python.org'
match = re.match('http:|https:|ftp:', url)
print(match.group())

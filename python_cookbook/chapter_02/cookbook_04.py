

# 2.4 Matching and searching for text patterns
import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))
print(text[10:])

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


# another example | match method looks only at the beginning of the string
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')


# another example | find_all method find all ocurrences of a pattern
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
alldates = datepat.findall(text)
print(alldates)


# another example | using capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('12/14/2020')
print(m)
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
print(year, month, day)

# find all matches (notice splitting into tuples)
alldates = datepat.findall(text)
print(alldates)
for m, d, y in datepat.findall(text):
    print(f'{y}-{m}-{d}')

for m in datepat.finditer(text):
    print(m.groups())


# another example
m = datepat.match('12/14/2020abcdef')
print(m)
print(m.groups())

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m = datepat.match('12/14/2020abcdef')
print(m)
m = datepat.match('12/14/2020')
print(m)

alldates = re.findall(r'(\d+)/(\d+)/(\d+)', text)
print(alldates)



# 2.10 Working with unicode characters in regular expressions
import re

num = re.compile('\d+')

# ASCII digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))
arabic = re.compile('[\u0600-\u06ff-\u0750-\u077f-\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
print(pat.match(s.upper()))
print(s.upper())

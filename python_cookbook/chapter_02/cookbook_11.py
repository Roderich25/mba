

# 2.11 Stripping unwanted characters from strings

# whitespace stripping
import re

s = '   hello world  \n'
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())


# character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

# another example
s = '  hello      world   \n'
print(s.strip())
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s).strip())

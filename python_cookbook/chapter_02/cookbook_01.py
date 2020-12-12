

# 2.1 Splitting strngs on any of multiple delimiters
import re

line = 'asdf fjdk; afed, fjek,asdf,     foo: bar'
fields = re.split(r'[\s:;,]\s*', line)
print(fields)


# another example | capture group
fields = re.split(r'(;|:|,|\s)\s*', line)
print(fields)

values = fields[::2]
print(values)
delimiters = fields[1::2] + ['']
print(delimiters)

reform = ''.join(v+d for v, d in zip(values, delimiters))
print(reform)


# another example | noncapture group
fields = re.split(r'(?:\s|,|;|:)\s*', line)
print(fields)

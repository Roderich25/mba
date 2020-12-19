

# 2.9 Normalizing unicode text to a standard representation
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(ascii(t1))
print(t1 == t2)

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(ascii(t3))
print(t3 == t4)


# another example
s = '\ufb01'  # a single character
print(s)
print(len(s))

t = unicodedata.normalize('NFD', s)
print(t)
print(len(t))

t = unicodedata.normalize('NFKC', s)
print(t)
print(len(t))

t = unicodedata.normalize('NFKD', s)
print(t)
print(len(t))

# another example
t1 = unicodedata.normalize('NFD', s1)
c = ''.join(c for c in t1 if not unicodedata.combining(c))
print(c)

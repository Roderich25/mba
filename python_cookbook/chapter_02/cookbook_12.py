

# 2.12 Sanitizing and cleaning up text
import unicodedata
import sys

s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)

cmb_chrs = dict.fromkeys(c for c in range(
    sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))


# another example
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# Arabic digit
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))


# another example
print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))


# faster than `translate` for trivial replacement
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

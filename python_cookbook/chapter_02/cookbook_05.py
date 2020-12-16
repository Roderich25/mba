

# 2.5 Searching and replacing text
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
text = text.replace('yeah', 'yep')
print(text)


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))


# another example | using re compile method
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\2-\1', text))


# another example | using month_abbr mapping
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return f'{m.group(2)} {mon_name} {m.group(3)}'


print(datepat.sub(change_date, text))


# another example
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)

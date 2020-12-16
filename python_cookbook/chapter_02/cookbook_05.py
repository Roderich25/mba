

# 2.5 Searching and replacing text
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
text = text.replace('yeah', 'yep')
print(text)


text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)


# another example | using re compile method
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\2-\1', text))


# another example | using mont_abbr function
def change_date(m):
    pass



# 2.5 Searching and replacing text
import re

text = 'yeah, but no, but yeah, but no, but yeah'
text = text.replace('yeah', 'yep')
print(text)


text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)

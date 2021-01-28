

# 2.16 Reformatting text to a fixed number of columns
import os
import textwrap


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."


print(textwrap.fill(s, 70))

print(textwrap.fill(s, 40))

print(textwrap.fill(s, 40, initial_indent='\t'))

print(textwrap.fill(s, 40, subsequent_indent='\t'))

print(os.get_terminal_size().columns)

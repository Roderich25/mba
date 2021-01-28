

# 2.17 Handling HTML and XML entities in text
import html

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))


s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

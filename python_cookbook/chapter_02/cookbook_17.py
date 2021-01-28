

# 2.17 Handling HTML and XML entities in text
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))


s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = "Spicy &quot;Jalape&#241;o&quot."
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))

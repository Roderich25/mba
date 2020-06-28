from lxml import html
import requests

page = requests.get('http://www.reforma.com')
tree = html.fromstring(page.content)

news = tree.xpath('//div[@id="contenido"]//div[@id="zonaprime"]//h1//a[@class="ligaonclick"]')
ps = tree.xpath('//div[@id="contenido"]//div[@id="zonaprime"]//p')
for new, p in zip(news, ps):
    print(' '.join(list(new.itertext())))
    print(' '.join(list(p.itertext())), end='\n\n')

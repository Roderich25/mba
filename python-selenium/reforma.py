from lxml import html
import requests

page = requests.get('http://www.reforma.com')
tree = html.fromstring(page.content)

main_tag = 'unodostres'  # 'zonaprime'
news = tree.xpath(f'//div[@id="contenido"]//div[@id="{main_tag}"]//h1//a[@class="ligaonclick"]')
ps = tree.xpath(f'//div[@id="contenido"]//div[@id="{main_tag}"]//p')
for new, p in zip(news, ps):
    print(' '.join(list(new.itertext())))
    print(' '.join(list(p.itertext())), end='\n\n')

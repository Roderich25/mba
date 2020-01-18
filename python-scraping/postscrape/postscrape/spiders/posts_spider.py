import scrapy
import os


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://blog.scrapinghub.com/page/1/',
        'https://blog.scrapinghub.com/page/2/'
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)


class MLSpider(scrapy.Spider):
    name = "ml"

    start_urls = [
        os.getenv('SCRAPY_ML')
    ]

    def parse(self, response):
        for post in response.css('.results-item'):
            yield {
                'item': post.css('.item__info .main-title::text').get(),
                'features': post.css('.item__info .item__attrs::text').get(),
                'price': post.css('.item__info .price__fraction::text').get()
            }
        next_page = response.css(
            '.andes-pagination__link.prefetch::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from scrapy.loader import ItemLoader

class LmruSpider(scrapy.Spider):
    name = 'lmru'
    allowed_domains = ['castorama.ru']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = [f"https://www.castorama.ru/catalogsearch/result/?q={kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@class='product-card__name ga-product-card-name']")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)


    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=JobparserItem(), response=response)
        loader.add_value('_id', response.url, re='-(\d+)\/$')
        loader.add_xpath('name', "//div[@class = 'product-essential__name hide-min-small']//text()")
        loader.add_xpath('price', "//span[@class = 'price']//text()")
        loader.add_xpath('photos', "//img[contains(@class, 'top-slide__img')]/@data-src")
        loader.add_value('url', response.url)
        yield loader.load_item()


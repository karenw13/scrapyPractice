import scrapy
from scrapy.loader import ItemLoader

from product_scraper.items import Product

class EcomSpider(scrapy.Spider):
    name = 'ecom_spider'
    allowed_domains = ['clever-lichterman-044f16.netlify.com']
    start_urls = ['https://clever-lichterman-044f16.netlify.com/products/taba-cream.1/']

    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('price', "//div[@class='my-4']/span/text()")
        l.add_xpath('title', '//section[1]//h2/text()')
        l.add_xpath('title', '//title')
        l.add_value('product_url', response.url)
        return l.load_item()
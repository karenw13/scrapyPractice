import scrapy

from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider
from product_scraper.items import Product

class SitemapSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = ['https://clever-lichterman-044f16.netlify.com/sitemap.xml']
    sitemap_rules = [
        ('/products/', 'parse_product')
    ]

    def parse_product(self, response):
        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('price', "//div[@class='my-4']/span/text()")
        l.add_xpath('title', '//section[1]//h2/text()')
        l.add_xpath('title', '//title')
        l.add_value('product_url', response.url)
        return l.load_item()
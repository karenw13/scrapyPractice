import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

def remove_dollar_sign(value):
    return value.replace('$', '')

class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(remove_dollar_sign)
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    product_type = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    no_of_reviews = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()

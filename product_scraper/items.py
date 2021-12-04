# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    name = scrapy.Field()
    ingredients = scrapy.Field()
    ingredients_list = scrapy.Field()
    description = scrapy.Field()
    img_url = scrapy.Field()
    label = scrapy.Field()


# class ProductScraperItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

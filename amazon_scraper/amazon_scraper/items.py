# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class AmazonSingleItem(scrapy.Item):
    name = Field()
    price = Field()
    images = Field()#change this is a list
    description = Field()
    reviews = Field()

class AmazonSearchResultItem(scrapy.Item):
    product_name = Field()
    rating = Field()
    price = Field()
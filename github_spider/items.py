# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RepoItem(scrapy.Item):
    url = scrapy.Field()
    star = scrapy.Field()
    fork = scrapy.Field()

class GithubSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()

    # name = scrapy.Field()
    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewalbumsItem(scrapy.Item):
    # define the fields for your item here like:
    artist = scrapy.Field()
    album_name = scrapy.Field()
    released_year = scrapy.Field()
    style = scrapy.Field()
    album_format = scrapy.Field()
    size =scrapy.Field()

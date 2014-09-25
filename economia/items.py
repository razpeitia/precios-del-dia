# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EconomiaItem(scrapy.Item):
    presentacion = scrapy.Field()
    origen = scrapy.Field()
    destino = scrapy.Field()
    pMin = scrapy.Field()
    pMax = scrapy.Field()
    precio = scrapy.Field()
    frec = scrapy.Field()
    obs = scrapy.Field()
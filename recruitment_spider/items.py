# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitmentSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_type = scrapy.Field()
    rec_title = scrapy.Field()
    company_name = scrapy.Field()
    company_location = scrapy.Field()
    job_desc = scrapy.Field()


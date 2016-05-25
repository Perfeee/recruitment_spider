#!/usr/bin/env python
# coding=utf-8
#Author: Perfe
#E-mail: ieqinglinzhang@gmail.com

import scrapy
import time
from recruitment_spider.items import RecruitmentSpiderItem
from bs4 import BeautifulSoup

class Recruitment_Spider(scrapy.Spider):
    name = "rec"
    allowed_domains = ["nlpjob.com"]
    start_urls = ["http://www.nlpjob.com/jobs/"]
    def parse(self,response):
        soup = BeautifulSoup(response.body,"lxml")
        span_list = soup.find_all("span",class_="row-info")
        for span_tag in span_list:
            yield scrapy.Request(url=span_tag.a["href"],callback=self.rec_parse)
        job_list_tag = soup.find("div",id="job-listings")
        yield scrapy.Request(url=job_list_tag.contents[-2],callback=self.parse)

    def rec_parse(self,response):
        item = RecruitmentSpiderItem()
        soup = BeautifulSoup(response.body,"lxml")
        item["job_type"] = soup.find("h2").img["alt"]
        item["rec_title"] = soup.find("h2").get_text().strip()
        item["company_name"] = soup.find("span",class_="fading").find_next_sibling().get_text()
        try:
            item["company_location"] = soup.find("strong").get_text()
        except:
            item["company_location"] = "无"
        item["job_desc"] = soup.find("div",id="job-description").get_text().strip()
        yield item

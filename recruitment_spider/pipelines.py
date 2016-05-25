# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from recruitment_spider.conf import Database_Conf
import pymysql
class RecruitmentSpiderPipeline(object):
    def __init__init(self):
        self.connection = pymysql.connect(host=Database_Conf["host"],user=Database_Conf["user"],password=Database_Conf["passwd"],db=Database_Conf["db"])
        self.cursor = self.connection.cursor()
    def process_item(self, item, spider):
        try:
            sql = "INSERT INTO A1 (job_type,rec_title,company_name,company_location,job_desc) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(sql,(item["job_type"],item["rec_title"],item["company_name"],item["company_location"],item["job_desc"]))
            self.connection.commit()
        except pymysql.Error,e:
            print("Error %d %s" % (e.args[0],e.args[1]))

        return item


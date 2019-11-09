# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import *
import pymongo
from scrapy.utils.project import get_project_settings
setting=get_project_settings()

class Spider1Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host=setting.get('MONGODB_HOST'), port=setting.get('MONGODB_PORT'))
        db = client[setting.get('MONGODB_DB')]
        self.mm_home = db['movies_data']

    def process_item(self, item, spider):
        if isinstance(item, Movies):
            self.mm_home.insert_one(dict(item))
        return item
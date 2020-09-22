# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request
class CarPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"images")
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    def process_item(self, item, spider):
        cate = item['cate']
        urls = item['urls']
        cate_path = os.path.join(self.path,cate)
        if not os.path.exists(cate_path):
            os.mkdir(cate_path)

        for url in urls:
            image_name = url.split("_")[-1]
            image_path = os.path.join(cate_path,image_name)
            request.urlretrieve(url,image_path)
        return item

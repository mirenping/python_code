# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item






def process_item(self, item, spider):
    return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    '''

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('sun0769.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
        
        
'''

# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from tutorial.items import SunItem


class SunSpider(CrawlSpider):
    name = 'sun0769'
    num = 0
    allow_domain = ['http://wz.sun0769.com/']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    rules = {
        Rule(LinkExtractor(allow='page')),
        Rule(LinkExtractor(allow='/html/question/\d+/\d+\.shtml$'), callback='parse_content')
    }

    _x_query = {
        'title': '//div[contains(@class, "pagecenter p3")]/div/div/div[contains(@class,"cleft")]/strong/text()',
        'content': '//div[contains(@class, "c1 text14_2")]/text()',
        'content_first': '//div[contains(@class, "contentext")]/text()'
    }

    def parse_content(self, response):
        bbs_item = SunItem()
        content = response.xpath(self._x_query['content_first']).extract()
        if len(content) == 0:
            content = response.xpath(self._x_query['content']).extract()[0].strip()
        else:
            content = content[0].strip()
        title = response.xpath(self._x_query['title']).extract()[0].strip()

        number = title.split(':')[-1]
        url = response.url
        bbs_item['url'] = url
        bbs_item['number'] = number
        bbs_item['title'] = title
        bbs_item['content'] = content

        yield bbs_item

import scrapy
from tutorial.items import RecruitItem
import re
class RecruitSpider(scrapy.spiders.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=0#a"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@class="even"]'):
            name = sel.xpath('./td[1]/a/text()').extract()[0]
            detailLink = sel.xpath('./td[1]/a/@href').extract()[0]
            catalog =None
            if sel.xpath('./td[2]/text()'):
                catalog = sel.xpath('./td[2]/text()').extract()[0]

            recruitNumber = sel.xpath('./td[3]/text()').extract()[0]
            workLocation = sel.xpath('./td[4]/text()').extract()[0]
            publishTime = sel.xpath('./td[5]/text()').extract()[0]
            #print name, detailLink, catalog,recruitNumber,workLocation,publishTime
            item = RecruitItem()
            item['name']=name.encode('utf-8')
            item['detailLink']=detailLink.encode('utf-8')
            if catalog:
                item['catalog']=catalog.encode('utf-8')
            item['recruitNumber']=recruitNumber.encode('utf-8')
            item['workLocation']=workLocation.encode('utf-8')
            item['publishTime']=publishTime.encode('utf-8')
            yield item

        nextFlag = response.xpath('//*[@id="next"]/@href')[0].extract()
        if 'start' in nextFlag:
            curpage = re.search('(\d+)',response.url).group(1)
            page =int(curpage)+10
            url = re.sub('\d+',str(page),response.url)
            print url
            yield scrapy.Request(url, callback=self.parse)
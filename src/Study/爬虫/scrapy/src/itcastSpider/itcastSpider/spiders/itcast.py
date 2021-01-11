# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        selectors = response.xpath('//div[@class="li_txt"]')
        result = {}
        for x in selectors:
            result['name'] = x.xpath('./h3/text()').get().split()
            result['job'] = x.xpath('./h4/text()').get().split()
            result['details'] = x.xpath('./p/text()').get().split()
            yield result

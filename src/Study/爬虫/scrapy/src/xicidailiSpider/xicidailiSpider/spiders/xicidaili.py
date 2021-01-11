# -*- coding: utf-8 -*-
import scrapy


# 创建爬虫类, 并且继承自scrapy.Spider
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'  # 爬虫名字 必须唯一
    allowed_domains = ['https://www.xicidaili.com/']  # 允许采集的域名
    start_urls = [f'https://www.xicidaili.com/nn/{i}' for i in range(1, 100)]  # 开始采集的网站

    # 解析想要数据 提取数据 或者 网址等 / response网页源码
    def parse(self, response):
        """提取数据"""
        # 提取IP PORT
        selectors = response.xpath('//tr')  # 选择所有的te标签
        for x in selectors:
            ip = x.xpath('./td[2]/text()').get()  # get 得到一个元素  getall()得到多个
            port = x.xpath('./td[3]/text()').get()

            # ip = x.xpath('./td[2]/text()').extract_first()
            # port = x.xpath('./td[3]/text()').extract_first()

            print(ip, port)



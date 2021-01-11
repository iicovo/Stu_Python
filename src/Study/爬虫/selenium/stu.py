# encoding:utf-8
from selenium import webdriver
from lxml import etree
import time


# 拉勾网
class lagouSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.lagou.com/zhaopin/go/?filterOption=3&sid=46172a3e82714b15abbe608f61324d35'

    def run(self):
        """运行"""
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div[2]').click()  # 弹窗点击
        time.sleep(2)
        source = self.driver.page_source  # 获取元素
        self.parse_list(source)  # 传入网页元素

    def parse_list(self, source):
        """解析"""
        html = etree.HTML(source)
        links = html.xpath("//a[@class_='position_link']/@href")


if __name__ == '__main__':
    spider = lagouSpider()
    spider.run()

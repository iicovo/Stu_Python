# encoding:utf-8
from selenium import webdriver
import time

url = 'https://music.163.com/#/playlist?id=2910497095'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_css_selector('.link.s-fc3').click()  # 点击登录
time.sleep(1)
driver.find_element_by_css_selector('.u-btn2.other').click()  # 选择其他方式

driver.find_element_by_id('j-official-terms').click()  # 点击同意

driver.find_element_by_css_selector('.u-mlg2.u-mlg2-wy').click()  # 网易账户登录
time.sleep(1)
username = driver.find_element_by_id('e')
username.send_keys('iicovo@163.com')
time.sleep(1)
kwd = driver.find_element_by_id('epw')
kwd.send_keys('Kong6666*')
time.sleep(1)
driver.find_element_by_css_selector('.js-primary.u-btn2.u-btn2-2').click()

# driver.refresh() # 刷新
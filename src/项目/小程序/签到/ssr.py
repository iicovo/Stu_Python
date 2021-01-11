# encoding : utf-8
import time
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome()
try:
    driver.get('https://xxjc.pro')
    print('获取网页成功!')
    time.sleep(1)
except:
    print('打不开链接,正在尝试更换链接!')
    driver.get('https://xxjc.vip')
    print('获取网页成功!')
    time.sleep(1)

try:
    # 登录
    driver.find_element_by_xpath('//*[@id="header"]/nav/ul/li[2]/a').click()
    inputname = driver.find_element_by_xpath('//*[@id="email"]')
    inputname.send_keys('599520857@qq.com')
    inputpwd = driver.find_element_by_xpath('//*[@id="passwd"]')
    inputpwd.send_keys('kkk00000')
    driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[6]/div/div/label/span[3]').click()
    driver.find_element_by_xpath('//*[@id="login"]').click()
    time.sleep(2)
    # 签到
    try:
        driver.find_element_by_xpath('//*[@id="checkin"]').click()
        print('签到成功!')
    except:
        print('今天已签到!')
except:
    driver.find_element_by_xpath('//*[@id="header"]/nav/ul/li[2]/a').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="checkin"]').click()
        print('签到成功!')
    except:
        print('今天已签到!')
driver.quit()

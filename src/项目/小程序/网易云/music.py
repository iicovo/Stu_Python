from selenium import webdriver
import time


class music:

    def __init__(self):
        self.url = 'https://tools.miku.ac/163_daka/'
        self.user = ''  ### 网易账号
        self.pwd = '' ### 网易密码

    def sign(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        try:
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button').click()
        except Exception:
            driver.refresh()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button').click()
        """输入信息"""
        input_user = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div[1]/div[3]/input')
        input_user.send_keys(self.user)
        input_pwd = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div[1]/div[5]/input')
        input_pwd.send_keys(self.pwd)
        time.sleep(2)
        """确认"""
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div[1]/button').click()
        time.sleep(5)
        driver.quit()


if __name__ == '__main__':
    a = music()
    for i in range(1, 3):
        a.sign()
        time.sleep(120)

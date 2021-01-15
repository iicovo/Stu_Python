from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--headless')  # 浏览器不提供可视化页面
option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
driver = webdriver.Chrome(options=option)

driver.execute_script(
    "document.querySelector('#username').style.display='block';")  # 显示隐藏元素
driver.execute_script("document.querySelector('#pwd').style.display='block';")

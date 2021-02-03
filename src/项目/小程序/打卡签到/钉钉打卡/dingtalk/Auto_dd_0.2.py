# encoding:utf8
import pyautogui as pa
import os
import time


def clock_in():
    """ 签到打卡 """
    run_software()  # 启动软件
    image_scan()


def run_software():
    """ 打开DD """
    path = 'E:/钉钉/DingDing/DingtalkLauncher.exe'
    os.system(path)
    time.sleep(5)


def shutdown():
    time.sleep(5)
    os.system("taskkill /F /IM Dingtalk.exe")  # 关闭钉钉
    print("打卡完成！")


def time_sleep():
    time.sleep(3)
    pa.scroll(-1000)  # 向下滚动页面


def image_scan():
    get_click('Work.png')  # 进入工作界面
    time.sleep(2)
    x, y = pa.position()  # 获取鼠标当前位置
    pa.moveTo(x + 100, y)  # 鼠标移动
    time_sleep()
    get_click('health.png')  # 进入健康打卡界面
    time_sleep()
    get_click('finish.png')  # 提交


def get_click(image):
    """ 鼠标移动点击操作 """
    time.sleep(3)
    work = pa.locateOnScreen(image)  # 识别图像在屏幕的坐标
    x, y = pa.center(work)  # 获取按钮的中心位置
    pa.click(x, y, duration=0.20)  # 点击


if __name__ == '__main__':
    clock_in()  # 打卡
    shutdown()  # 关闭

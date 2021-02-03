# encoding:utf-8
import pyautogui as pa
import os
import time


def clock_in():
    """ 签到打卡 """
    run_software()  # 启动软件
    image_scan()
    # Workclick()  # 点击 工作 按钮
    # table()  # 点击健康打卡表
    # check_table()  # 进入打卡表
    # check_table()  # 未填写表
    # fill_in()  # 填表


def run_software():
    """ 打开DD """
    path = 'E:/钉钉/DingDing/DingtalkLauncher.exe'
    os.system(path)
    time.sleep(5)


def shutdown():
    time.sleep(5)
    os.system("taskkill /F /IM Dingtalk.exe")  # 关闭钉钉
    print("打卡完成！")


def image_scan():
    get_click('Work.png')  # 进入工作界面
    get_click('click.png')  # 进入健康返校打卡界面
    get_click('write.png')  # 进入未填写表
    time.sleep(3)
    pa.scroll(-1000)  # 向下滚动页面
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

# def check_table():
#     """ 检测未填写表 """
#     writeTable = pa.locateOnScreen("write.png")  # 获取工作位置
#     x, y = pa.center(writeTable)  # 获取工作按钮的中心位置
#     pa.click(x, y, duration=0.20)  # 点击
#     time.sleep(3)
#
#
# def Workclick():
#     """ 点击工作按钮 """
#     workButton = pa.locateOnScreen("Work.png")  # 获取工作位置
#     x, y = pa.center(workButton)  # 获取工作按钮的中心位置
#     pa.click(x, y, duration=0.20)  # 点击
#     time.sleep(3)
#
#
# def table():
#     """ 点击填表 """
#     pos_table = pa.locateOnScreen("click.png")
#     x, y = pa.center(pos_table)
#     pa.click(x, y, duration=0.20)  # 点击
#
#

# def fill_in():
#     """ 填表 """
#     pa.scroll(-1000)  # 鼠标向下滚动
#     pos_button = pa.locateOnScreen('Button.png')
#     x, y = pa.center(pos_button)
#     pa.click(x, y, duration=0.20)  # 点击
#     time.sleep(3)

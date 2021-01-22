# encoding:utf-8
import pyautogui as pa

""" 常用操作 """
MouseX, MouseY = pa.position()  # 获取鼠标位置
print(MouseX, MouseY)

print(pa.onScreen(190, 200))  # 判断该位置是否在屏幕

wt, ht = pa.size()  # 获取屏幕宽高
print(wt, ht)

""" 鼠标操作 """
# - 鼠标移动，(x,y,duration) x,y:相对左上角屏幕坐标 duration：持续时间
pa.moveTo(100, 100, duration=0.025)  # 移动到 (100,100)

# -

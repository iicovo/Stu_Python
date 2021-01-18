# encoding:utf-8
import turtle as t

""" 初始化窗口 """
# 参数(width,heigh,startx,starty) 设置窗体大小及相对屏幕的窗体位置
# t.setup(width=800, height=500, startx=300, starty=200)
# t.screensize(800, 600, "green")  # 参数（宽，高，颜色）

""" 运动控制 """
# t.goto(100, 100)  # goto去某个坐标并画出路径
# t.fd()  # fd = forward  前进100像素长
# t.bk()  # bk = back 反方向前进

""" 方向控制 """
# t.circle(50, 45)  # 参数(距离，绝对角度)
# t.lt()  # le =left 参数(绝对角度)
# t.rt()  # le =right 参数(绝对角度)

""" 颜色设置 """
# t.colormode()  # 设置窗体颜色
# t.color()  # 设置

""" 画笔控制及设置 """
# t.pd()  # pd = pendown 画笔落下
# t.pu  # pu = penup 画笔抬起
# t.pensize()  # 设置画笔粗细
# t.pencolor()  # 设置画笔颜色


""" 蟒蛇绘制 """
t.setup(650, 350, 200, 200)
t.pu()
t.fd(-250)
t.pd()
t.pensize(25)
t.pencolor("purple")  # 画笔颜色改为紫色
t.seth(-40)  # 绝对角度
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80 / 2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2 / 3)

t.done()

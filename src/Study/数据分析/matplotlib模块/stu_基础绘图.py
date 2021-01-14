# encoding:utf-8

# 绘图子模块
from matplotlib import pyplot as plt

"""设置输出图片大小"""
plt.figure(figsize=(15, 8), dpi=80)

""" 数据在x轴的位置，是一个可迭代的对象 """
x = range(2, 26, 2)
""" 数据在y轴的位置，是一个可迭代的对象 """
y = [15, 13, 14, 5, 17, 20, 25, 26, 23, 22, 18, 15]

""" 设置字体格式 """
import matplotlib

font = {
    "family": "Microsoft YaHei",
    "weight": "bold",
    "size": "18",
}
matplotlib.rc("font", **font)
# matplotlib.rc("font", family="Microsoft YaHei",weight="bold",size="larger")
""" 另一种设置字体的方式 """
# from matplotlib import font_manager
# my_font = font_manager.FontProperty( fame="path") #传入字体文件地址

"""添加图表描述信息"""
plt.xlabel("时间h")  # x轴标签
plt.ylabel("气温°c")  # y轴标签
plt.title("今天气温变化图")  # 图表标题

""" 设置轴刻度"""
# x轴
x2 = [i / 2 for i in range(4, 48)]  # 列表推导式
# plt.xticks(x)
plt.xticks(x2[::2], rotation=0)  # 传入参数取步长2  rotation= 设置刻度旋转多少度 逆时针旋转

# y轴
plt.yticks(range(min(y), max(y) + 1, 3))

""" 绘图 """
plt.plot(x, y)  # 传入x和y，通过plot绘制出折线图

""" 保存图片 """
# 保存为常用格式图片 .png/.jpg
# plt.savefig('p1.png')
# 保存矢量图
# plt.savefig('p1.svg')


plt.show()  # 展示图形

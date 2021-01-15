# encoding:utf-8
import wordcloud  # 词云

""" 实例化对象 """
# wordcloud.WordCloud()

""" 加载词云文本 """
# .generate()

""" 保存为文件 """
# .to_file()

""" 词云设置 """
# width,height 设置词云显示大小
# min_font_size,max_font_size 指定词云中字体的 最小字号 和 最大字号
# font_path 指定词云中本地字体文件，传入的参数应为文件地址
# max_words 指定词云显示的最大单词数量，默认200
# stop_words 指定词云的排除词列表，即不显示的单词列表
# background_color 指定词云图片的背景颜色 默认黑色

""" 设置词云形状"""
# 默认为长方形
# from scipy.misc import imread
# mk = imread("t1.png")
# w = wordcloud.WordCloud(mask = mk)


w = wordcloud.WordCloud()
txt = "WordCloud by Python"
w.generate(txt)
w.to_file("观看效果.png")

# encoding:utf-8
import jieba

# 分词
jb = jieba.cut("大家好，我是结巴！")
print(list(jb))


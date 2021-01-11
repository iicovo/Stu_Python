# encoding:utf-8
import jieba

# 分词
jb = jieba.cut("大家好，我是结巴！")
print(list(jb))

filename = "E:\\Desktop\\二级基础.txt"

with open(filename, 'r', encoding="utf-8") as files:
    vocab = {}


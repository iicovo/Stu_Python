# encoding:utf-8
import jieba

"""" 文本词频分析实例 """

txt = open("E:\\Desktop\\t_jieba.txt", 'r', encoding="utf-8").read()
excludes = {'将军', '却说', '荆州', '二人', '不可', '不能', '如此'}  # 列出多余统计

words = jieba.lcut(txt)
counts = {}

# 合并统计人名
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rWord = "孔明"
    elif word == "关公" or word == "云长":
        rWord = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rWord = "刘备"
    elif word == "孟德" or word == "丞相":
        rWord = "曹操"
    else:
        rWord = word
    counts[rWord] = counts.get(rWord, 0) + 1

# 剔除多余统计
for word in excludes:
    del counts[word]

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}次".format(word, count))

"""
曹操         1451次
孔明         1383次
刘备         1252次
关羽          784次
张飞          358次
商议          344次
如何          338次
主公          331次
军士          317次
吕布          300次
"""

# encoding:utf-8
import jieba

"""" 文本词频分析实例 """

txt = open("E:\\Desktop\\t_jieba.txt", 'r', encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0)

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(len(items)):
    word, count = items[i]
    print("{}\t\t{}".format(word, count))

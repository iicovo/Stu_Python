# encoding:utf-8
import turtle
import random
import time
import jieba
import wordcloud

r = random.random()
print(r)

r1 = random.randrange(1, 10, 2)
print(r1)

list1 = ['张三', '李四', '王二']
r2 = random.choice(list1)
print(r2)

random.shuffle(list1)
print(list1)

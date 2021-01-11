# encoding:utf-8
import random


# 随机生成 0~1 之间的随机数
r = random.random()
print(r)

# 随机生成 在1-10之间且间隔为2 的随机数 (1,3,5,7,9)
r1 = random.randrange(1, 10, 2)
print(r1)

list1 = ['张三', '李四', '王二']
# 在列表中随机抽取
r2 = random.choice(list1)
print(r2)

# 打乱列表内容
random.shuffle(list1)
print(list1)

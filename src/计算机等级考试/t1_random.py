# encoding:utf-8
import random  # 随机数生成库

""" 扩展随机数函数 """

# randint(a,b) 生成[a,b]之间的整数
# randrange(n,m [,k]) 生成[n,m)之间 步长为k的整数
# choice() 随机选择序列中的一个元素
# shuffle() 将序列元素随机排列，返回打乱后的元素序列
# getrandbits(k) 生成一个k比特长的随机数
# uniform(a,b) 生成[a，b]之间的随机 小数


""" 简单使用 """

# 随机生成 0 ~ 1.0 之间的随机数
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

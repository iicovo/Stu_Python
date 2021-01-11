# encoding:utf-8

import os

# 1.操作系统相关内容

print(os.name)  # 操作系统
print(os.environ)  # 系统环境变量
print(os.sep)  # 查看系统分隔符
print(os.pathsep)  # 查看path分隔符
print(os.linesep)  # 查看换行符的分隔符

# 2.文件个目录的操作

os.mkdir("KGH")  # 当前目录下创建目录
os.rmdir("KGH")  # 当前目录下删除目录

os.remove(path)  # 删除文件或空文件夹
os.makedirs()  #创建多级目录
os.removedirs() #删除多级目录 要删除目录必须为空
os.stat() #查看目录状态
print(os.getcwd())  # 查看当前目录地址
os.rename()  # 重命名

# 3.os子模块 os.path

file = os.getcwd() + '/M1_os.py'
print(os.path.split(file))  # 分割文件
print(os.path.isdir(file))  # 判断是否为目录
print(os.path.isfile(file))  # 判断是否为文件
print(os.path.exists(file))  # 判断文件是否存在
print(os.path.getctime(file))  # 查看创建时间
print(os.path.getsize(file))  # 得到文件大小： 字节

# 4. os子模块 os.system
# 用来调用系统的模块

os.system('calc')  # 系统计算器
os.system("path.exe")  # 调用系统应用程序



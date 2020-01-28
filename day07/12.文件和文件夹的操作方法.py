# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

import os
# 1.文件重复名，原文件
# os.rename("a.txt","b.txt")
# os.rename("b.txt","c.xt")

# 2.删除文件
# os.remove("c.txt")

#3.创建文件夹
# os.mkdir("新建文件夹")

# 4.获得当前工作目录(默认是当前工程的根目录)
print(os.getcwd())

# 5.修改工作目录
os.chdir("E:\\hello")
print(os.getcwd())

os.rename("a.txt","b.txt")


# 6.列出目录下的列表
# print(os.listdir())


# 7.删除文件夹
# os.rmdir("新建文件夹")

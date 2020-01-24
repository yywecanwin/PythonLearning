# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/21

"""
步骤：
    1.打开文件
    2.读/写数据
    3.关闭文件

"""

# 1.打开文件
f = open("a.txt","w")
# print(f.read())

# 2.写数据
f.write("hello word1")
f.write("hello word2")
f.write("hello word3")

# 3.关闭文件
f.close()









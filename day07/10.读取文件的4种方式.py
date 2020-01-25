# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/24

"""
读取文件的四种方式
    1。一次读取几个字符
    2.一次读取一行
    3.一次读取所有字符
    4.按行读取所有行

"""

# 1。一次读取几个字符
f = open("a.txt","r")
print(f.read())

print("*" * 50)

# 2.一次读取一行
print(f.readline())
print(f.readline())
print(f.readline())
# line = f1.readline()
# print(line)

print("*" * 50)

# 3.一次读取所有字符
f = open("a.txt","r")
content = f.read()
print(content)
print(type(content)) # <class 'str'>


# 4.按行读取所有行
f = open("a.txt","r")
result = f.readlines()
print(result) # ['Android\n', 'javaEE\n', '理解\n', '读取一行']
print(type(result)) # list


f.close()




# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28

s1 = "hello python"

# 1.查找"o"在s1中第一次出现的位置：s1.find()
print(s1.find("aa")) # -1
print(s1.find("o",6,11)) # 10
print(s1.find("pyt"))  # 6
print(s1.rfind("pyt")) # 6

"""
index()方法，找不到将会报错
"""
# print(s1.index("o", 6, 11))
# print(s1.index("aa"))

#统计"o"出现的次数
print(s1.count("o"))
print(s1.count("o",6,12))

#分割的方法：s.split(str)
s2 = "hello python android"
# 分割的结果是一个列表，把分割出来的几部分字符串作为元素放到列表中了
list1 = s2.split(" ")
print(list1) # ['hello', 'python', 'android']
print(type(list1)) # <class 'list'>

# 这个方法只能分割出三部分：左边部分，自己，右边部分
list2 = s2.partition(" ")
print(list2) # ('hello', ' ', 'python android')
print(type(list2)) # <class 'tuple'>







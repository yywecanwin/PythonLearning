# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/10

"""
set集合
    也是一个容器，可以存储多个元素，可以是任何类型得
    没有索引
    特点：
        set中不能存储重的元素，自动去重，重复的元素只保留一个

定义格式：
    set 集合名 = {元素1，元素2，。。。。。}
    定义空的set集合
    set集合名 = set()

"""

set1 = {10,"hello",True}
print(set1) # {True, 10, 'hello'}
print(type(set1)) # <class 'set'>

# 自动去重
set2 = {10,"hello",True,10,"hello"}
print(set2) # {'hello', True, 10}

set3 = {30,50}
set2.update(set3)
print(set2) # {True, 50, 10, 'hello', 30}

set4 = set("hello")
print(set4)

print("*" * 10)
for s in set4:
    print(type(s)) # <class 'str'>
    print(s) # 去掉重复的字母,其他字母随机排序







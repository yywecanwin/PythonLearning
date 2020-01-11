# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/11

"""
数据类型转换的格式：
    目标数据类型（数据）
"""


# set->list
set1 = {10,20,30}
list2 = list(set1)
print(list2) # [10, 20, 30]

set2 = set(list2)
print(set2) #{10, 20, 30}

list3 = {10,20,30,40,10}
set3 = set(list3)
print(set3) # {40, 10, 20, 30}
list4 = list(set3)
print(list4) # [40, 10, 20, 30]

d = [1,2,3,4,15]
e = tuple(d)
print(e) # (1, 2, 3, 4, 15)

f = list(e)
print(f) # [1, 2, 3, 4, 15]

h = set(e)
print(h) # {1, 2, 3, 4, 15}














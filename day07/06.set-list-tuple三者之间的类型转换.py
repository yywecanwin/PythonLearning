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












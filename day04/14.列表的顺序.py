# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/5

"""
排序:
    可以按照升序/降序排序.
"""

list1 = [10,45,32,12,3,4]
# 按照有小到大的升序排序
list1.sort()
print(list1) # [3, 4, 10, 12, 32, 45]

# 倒序排序: 由大到小的排序,降序
list1.sort(reverse=True)
print(list1) # [45, 32, 12, 10, 4, 3]

list2 = ["Python", "中国", "Android", "abc", "JavaEE", "C++", "Php"]
list2.sort()
print(list2) # ['Android', 'C++', 'JavaEE', 'Php', 'Python', 'abc', '中国']

print(ord("中")) # 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值










# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/10

"""
列表推导式的格式：
    列表名 = [x for x in range()函数]
    每次循环都得一个数字，然后把x作为元素添加到列表中

在列表推导式中使用 if语句
    列表名 = [x for x in range()函数 if 条件]
"""
list1 = [x for x in range(1,5)]
print(list1) # [1, 2, 3, 4]

list2 = [x+2 for x in range(1,5)]
print(list2) # [3, 4, 5, 6]

list3 = [x for x in range(20) if x % 2 == 0]
print(list3) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a = [x for x in range(1,101)]
print(list(range(0,len(a),3))) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

print(range(0,len(a),3)) # range(0, 100, 3)

print(a[0:3]) # [1, 2, 3]
print(a[3:6]) # [4, 5, 6]
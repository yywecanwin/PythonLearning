# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

list1 = [1,2,5,3]

print(list1) # [1, 2, 5, 3]

del list1[2]
print(list1) # [1, 2, 3]

a = 10
print(a)
del a

dict1 = {"name":"vivi"}
print(dict1) # {'name': 'vivi'}
del dict1["name"]
print(dict1) # {}


"""多维列表/元组访问的示例"""
tuple1 = [(2,3),(4,5)]
print(tuple1[0]) # (2, 3)

print(tuple1[0][1]) # 3





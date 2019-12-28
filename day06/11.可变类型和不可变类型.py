# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/28

"""
不可变类型
    如果改变了类型的数据的值，地址 也发生了变化，这种类型的数据，是不可变类型的数据
    常见类型
        int float bool str tuple

可变类型
    如果改变了该类型的数据的值，地址，没有 发生了变化，这种类型的数据，是可变类型的数据
    常见类型
        列表，字典，set集合

"""

a = 10
print(id(a)) # 140729720616048
a = 20
print(id(a)) # 140729720616368

print("*" * 50)

str1 = "hello"
print(id(str1)) # 2759820335400
str1 = "python"
print(id(str1)) # 2759938968632

print("*" * 50)

list1 = [10,20]
print(id(list1)) # 2327360791048
list1.append(30)
print(list1) # [10, 20, 30]
print(id(list1)) # 2327360791048

print("*" * 50)

dict1 = {"name":"爽儿","age":18}
print(id(dict1)) # 2327364323152
dict1['gender'] = "女"
print(dict1) # {'name': '爽儿', 'age': 18, 'gender': '女'}
print(id(dict1)) # 2327364323152



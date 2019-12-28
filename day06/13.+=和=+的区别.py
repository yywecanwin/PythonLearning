# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/28

"""
    a += 1
    a = a + 1
这两个写法对应 不可变类型的 数据，是没有区别的

"""

a = 10
print(id(10)) # 140729127384176
a += 1
print(id(a)) # 140729127384208

str1 = "hello"
print(id(str1)) # 1272621586728

str1 += "python"
print(str1) # hellopython
print(id(str1))

print("--------------------------")

list1 = [10,20]
print(id(list1))
# 只是把第二个列表中的元素放到第一个列表中,第一个列表的地址没有变,没有产生第三个列表
list1 += [30,40]
print(list1) # [10, 20, 30, 40]
print(id(list1))

# 是把两个列表中的元素都放到第三个列表中，产生了第三个列表，把三个列表赋值给了list1
list1 = list1 + [30,40]
print(list1) # [10, 20, 30, 40, 30, 40]
print(id(list1))










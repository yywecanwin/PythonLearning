# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/28

"""
Python中只有引用传递没有传递
也就是说在调用函数传递实参时，给形参传递的的实参的地址，而不是具体的数据值
"""
# def sum(a,b):
#     print("**********",a,b) # 10 20
# sum(10,20)

def print_list(list2=[]):
    list2.append(2)
    print("*" * 20)
    print("2222222222",list2) # [10, 20, 2]
    # print("3333333333",id(list2)) # 2265949823496

list1 = [10,20]
# print("1" * 10)
# print("44444444444",id(list1)) # 1832262197832
print_list(list1)
# list1 = [10,20]
# print("555555555555",id(list1)) # 2266071070728
# print_list()
# print("666666666666666",list1) # [10, 20]



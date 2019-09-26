# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""

数据类型转换的格式
    目标数据类型(数据)
    意思是说，把"数据"转换成 "目标数据类型"
需求
    从键盘上录入一个苹果的价格：9.50元，重量：4.50斤
    打印应付金额

"""
#1.录入苹果的价格
price = input("请录入苹果的价格：")

#把price转成float类型的小数
price  = float(price)
print(price)
print(type(price))

# 2.录入苹果的重量
weight  = input("请录入苹果的重量：")

# 把weight转成float类型的小数
weight  = float(weight)
print(weight)
print(type(weight))

# 3.计算应付金额
money = price * weight
print(money)


i = float("10.0")
print(i)
print(type(i))


# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/24

a = 10
b = 20

# 1、借助一个中间变量
# temp = a
# a = b
# b = temp
# print(a) # 20
# print(b) # 10

# 2.借助两个变量的和
# c = a + b
# b = c - a
# a = c - c - a
# c - a
# a = c - a
# b = c - b
# print(a)
# print(b)

#3.利用自动解包

a,b = b,a

print(a) # 20
print(b) # 10

x,y,z = 1,2,3

print(x)
print(y)
print(z)

z,y,x = 1,2,3
print(x)
print(y)
print(z)











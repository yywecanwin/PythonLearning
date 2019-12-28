# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/24

"""
小数点：
    -5-256
段字符串：
    长度不超过20的字符串

在python解释器一启动的时候，就会把小数字和段字符串放到缓冲区（小数字对象池和段字符串对象池）

"""

a = 10
b = 10

#获得数据的地址：调用id（数据）
print(id(10)) # 140729718322288
print(id(a)) # 140729718322288
print(id(b)) # 140729718322288

#大数字是在第一次使用时才被缓存，以后再用到这个数字时，就是用刚才缓存的那个数字
c = 10000
d = 10000
print(id(10000)) # 2755939753872
print(id(c)) # 2755939753872
print(id(d)) # 2755939753872

print("*" * 50)

# 短字符串对象池
s = "hello"
s2 = "hello"
print(id("hello")) # 2792835340416
print(id(s)) # 2792835340416
print(id(s2)) # 2792835340416

print("-" * 50)

s3 = "hellohellohellohellohellohello"
s4 = "hellohellohellohellohellohello"
print(id("hellohellohellohellohellohello")) # 2605583258448
print(id(s3)) # 2605583258448
print(id(s4)) # 2605583258448














# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28
"""
定义字符串的4种格式
    一对单引号，或者一对双引号，或者3对单引号 引住的任何内容，都是字符串
    第4种定义格式：使用字符串的格式化操作符
"""
str1 = 'hello'
print(str1)
print(type(str1))

str2 = "python"
print(str2)
print(type(str2))

str3 = "yao'is'good'man'"
print(str3)
print(type(str3))

str5 = ''''py"123"th"on'''
print(str5)
print(type(str5))

# 第4种定义格式:使用字符串的格式化操作符
name = "yaoyao"
str6 = "%s is a good man" % name
print(str6)
print(type(str6))

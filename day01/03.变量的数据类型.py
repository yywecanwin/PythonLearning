# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/26

# 定义 int类型,float类型,bool类型,str类型

i = 10

# 通过type(数据或者变量.可以获得数据类型)
# 先调用type(10)得到10的类型,然后再把类型赋值给变量result
result  = type(10)
print(result) # <class 'int'>


pi = 3.14
# 调用type(pi)得到pi类型
print(type(pi))


b1 = True
b2 = False
print(type(b1)) # <class 'bool'>
print(type(b2)) # <class 'bool'>


str1 = "hello"
print(type(str1)) # <class 'str'>



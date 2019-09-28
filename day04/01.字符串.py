# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28

name = "yaoyao"
age = 18
print("姓名是%s，年龄%d" % (name,age))

# f-strings
f_string1 = f"姓名是{name},年龄是{age}"
print(f_string1)

f_string2 = f"3 + 5 = {3 + 5}"
print(f_string2)
print(type(f_string2))

a = 10
b = 20
f_string3 = f"a + b的和是：{a + b}"
print(f_string3)


# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

print("开始执行。。。。。")
try:
    print(10/0)

except ZeroDivisionError as ze:
    print("在第6行的位置出现了如下错误：")
    print(ze)

try:
    f = open("a.txt","r")
except FileExistsError as fnfe:
    print(fnfe)

print("执行结束。。。")


# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

# True 非0数字
# 使用一个非0数字，进行条件判断，这个非0数字是作为True来使用的
if 0:
    print("关系表达式的结果为Fales")
else:
    print("关系表达式的结果为True")

print(0 and True) # 0
print(1 and 0) # 0
print(1 and 10) # 10

print(1 or 10) # 10
print(0 or 10) # 10

# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""
if语句实现三目运算符（三元运算符）
    a if a > b  else b
    向判断 a > b是否成立，如果成立计算的结果是a的值，否则就是b的值
"""

a = 20
b = 10
result = a if a > b else b
print(result) # 20

result2 = a + 10  if a < b else b + 200
print(result2) # 210


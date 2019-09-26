# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""
and	   x and y	布尔"与"： 并且的意思
    如果 x 为 False，x and y 返回 False，否则它返回 y 的值。
    True and False， 返回 False。
or	x or y	布尔"或"：
    如果 x 是 True，它返回 True，否则它返回 y 的值。
    False or True， 返回 True。
not	not x	布尔"非"：
    如果 x 为 True，返回 False 。
    如果 x 为 False，它返回 True。
    not True 返回 False, not False 返回 True

"""

a = 10
b = 20
c = 30


# and
# 如果 x 为 False，x and y 返回 False，否则它返回 y 的值。
print((a > b) and (b > c)) # False and (b > c)->False
print((a < b) and (b > c)) # True and False->False
print((a < b) and (b < c)) # True and True->True

# or
print((a > b) or (b > c)) # False or False->False
print((a < b) or (b > c)) # True or (b > c)->True
print((a < b) or (b < c)) # True or True->True

# not 非,取相反的意思
print(not (a > b)) #  not False -> True
print(not (a < b)) #  not True -> False




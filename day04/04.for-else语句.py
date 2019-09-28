# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28
"""
for .....else...格式:
    for 变量 in 容器：
        重复执行的代码块
        else:
            如果for循环不是通过break结束的时候，一定执行的代码块

需求：
    判断字符串中是否包含m

"""

s = "hello pymthon"

for c in s:
    if c == "m":
        print("字符串中包含m")
        break
else:
    print("字符串中没有包含 m")

# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28
"""
在嵌套的循环语句中
    continue 和 break只对离它最近的那一层循环语句起作用
"""

i = 1
while i <= 3:
    print("yao is a good man ,i=%d" % i)
    j = 1
    while j <= 3:
        if j == 2:
            j += 1
            continue
        print("=" * 20 + "i=%d,j=%d" % (i,j))
        j += 1
    i += 1
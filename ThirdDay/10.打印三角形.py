# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27
"""
*
* *
* * *
* * * *
* * * * *

每一行中的 * 的个数 与 行号相等

"""
i = 1
while i <= 5:
    j = 0
    while j < i:
        print("*",end="")
        j += 1
    # 换行
    print(end="\n")
    i += 1



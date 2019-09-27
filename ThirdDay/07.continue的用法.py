# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27
"""
continue：
    继续的意思
    只能用再    循环语句中，不能单独使用
    可以结束本次循环，继续下一次循环
"""

i = 1
while i <= 5:
    if i == 3:
        i += 1
        # 终止本次循环语句
        continue
    print("yao is a good man %d" % i)

    i += 1



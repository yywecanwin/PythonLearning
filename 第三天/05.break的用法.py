# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""
break:
    终断，结束的意思
    只能用在 循环语句中，不能单独使用，
    可以终止整个循环语句，不再循环了

"""

i = 1
while i <= 5:
    if i == 3:
        #终止整个循环语句
        break;
    print("yao is a good man %d " % i)
    i += 1









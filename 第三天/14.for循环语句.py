# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28
"""
for循环语句
    与while循环一样都是用来重复执行某一段代码
    格式：
        for 变量名 in range(开始数字，结束数字)或者容器：
            重复执行的代码块
        range(开始数字，结束数字)：用来得到某个范围的数据区间
        比如：
            range(1,10),得到的是[1,10)
            range(10)得到的是：[0,10)
"""
# 第一次执行 for i in range(1, 6) 时,做了3件事情:
# 1.执行range(1, 6) 得到一个数据区间[1,6)
# 2.从这个区间中取出第1个数字:1
# 3.定义变量 i,赋值为1

sum = 1
for i in range(1,9): #for i in [1,8)
    print("**",i)
    sum += i
print(sum)
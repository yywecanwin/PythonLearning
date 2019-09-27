# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""
需求 ：
    求1到5的累加和
    0 + 1 + 2 + 3 + 4 + 5
    sum = 0
    sum = sum + 1 # 1
    sum = sum + 2 # 3
    sum = sum + 3 # 6

"""
# 1.定义一个变量i表示1到100之间的某一个数字，默认为1
i = 1

# 2.定义一个变量sum表示 累加的和，默认为0
sum = 0

# 3 while循环5次
while i <= 5:
    #4.在循环语句中，让sum累加i
    sum += i # sum = sum + i
    #5.在循环语句中让i加1
    i += 1
# 6.再循环语句结束后，打印sum的值
print("累加和为：%d" % sum)








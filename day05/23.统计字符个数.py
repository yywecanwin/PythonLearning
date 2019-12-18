# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
题目:
    从键盘上录入一个字符串,统计字符串中大写字母,数字和其他字符的个数

分析步骤:
    1.从键盘录入一个字符串
    2.定义4个变量upper_count,lower_count,num_count,other_count
        分别用来存储大写字母,小写字母,数字和其他字符的个数
    3.遍历字符串
    4.在循环里面得到里面的元素,判断该元素是大写字母,小写字母,数字和其他字符
    5.在循环里面,根据判断的结果让对应的个数加1
    6.打印 大写字母,小写字母,数字和其他字符的个数

"""
# 1.从键盘录入一个字符串
str1 = input("请录入一个字符串")

# 2.定义4个变量upper_count,lower_count,num_count,other_count
#         分别用来存储大写字母,小写字母,数字和其他字符的个数
upper_count = 0
lower_count = 0
num_count = 0
other_count = 0

# 3.遍历字符串
for c in str1:
    #  4.在循环里面得到里面的元素,判断该元素是大写字母,小写字母,数字和其他字符
    if c.isupper():
        upper_count += 1
    elif c.islower():
        lower_count += 1
    elif c.isdigit():
        num_count += 1
    else:
        other_count += 1

print(f"大写字母的个数:{upper_count}")
print(f"小写字母的个数:{lower_count}")
print(f"数字的个数:{num_count}")
print(f"其他字符的个数:{other_count}")


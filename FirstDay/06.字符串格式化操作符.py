# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/26

#如果输出的字符串中包含某一个变量的值,就需要使用字符串的格式操作符
"""
格式化操作:
    %d 整数
    %s 字符串
    %f 小数
"""
age = 50
print("我的年龄是%d岁" % age) # 我的年龄是50岁
print("我的年龄是%d岁" % 50) # 我的年龄是50岁

username = "小庄"
print("用户的姓名是%s" % username)

pi = 3.1415
#如果是保留n位小数,在%的后面f的前面添加 .n
print("圆周率是%.2f" % pi)


num = 5
print("数字是%06d" % num)# 000005

age1 = 30
user_name = "铁娃"
print("我的姓名是%s,年龄是%d岁" % (user_name, age1))




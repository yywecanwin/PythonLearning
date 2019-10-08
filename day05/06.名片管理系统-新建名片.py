# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/8

"""
需求：
    向系统中录入名片，并保存
分析步骤：
    1、定一个列表card_list，用来存储所有的名片
    2、写一个无限循环
    3、在循环语句中，提示绿录入名的5个信息
    4、在循环语句中使用一个字典把5对信息存储取来，表示创建一个名片
    5、在循环语句中，把字典添加列表中


"""

# 1、定义一个列表card_list,用来存储所有的名片；
card_list = []
# 2、写一个无限循环
while True:
    is_input = input("是否要录入名片")
    if is_input == "yes":
        #3、在循环语句中，提示录入名片的6个信息
        company = input("请录入公司名称：")
        name = input("请录入姓名：")
        title = input("请录入职位：")
        tel = input("请录入手机号码：")
        email = input("请录入邮箱：")
        address = input("请录入公司地址：")
        #4、在循环语句中使用一个字典把5个信息存储取来，表示创建一个名片
        card = {"company":company,"name":name,"title":title,"tel":tel,"email":email,"address":address}
        #5、在循环语句中。把字典添加列表中
        card_list.append(card)
        print(card_list)
    else:
        break











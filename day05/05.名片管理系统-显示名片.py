# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/8

card_list = [
            {'company': '阿里巴巴集团', 'name': 'Jack.Ma', 'title': 'CEO', 'tel': '18888888888',
              'email': 'jack@alibaba.com', 'address': '杭州市阿里科技园1号楼9层'},
            {'company': '阿里巴巴集团', 'name': '张勇', 'title': '执行CEO', 'tel': '17777777777',
              'email': 'zhangyong@alibaba.com', 'address': '杭州市阿里科技园1号楼9层'}
            ]


# 1、遍历列表得到 名片（字典）

for card in card_list:
    # 2把名片显示出来

    company = card.get("company")
    name = card.get("name")
    title = card.get("title")
    tel = card.get("tel")
    email = card.get("email")
    address = card.get("address")

    # 2.1从字典中取出公司名称，姓名、职位、手机邮箱
    print(company,end="")
    print(name.rjust(10),end="")
    print("职位：" + title,end="")
    print("邮箱：" + email,end="")
    print("地址：" + address)


















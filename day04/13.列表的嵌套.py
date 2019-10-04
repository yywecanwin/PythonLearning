# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/4

# 如果列表中的元素还是列表，你的列表就是嵌套的列表
name_list = [["孙俪", "谢娜", "贾玲"], ["蓉蓉", "百合", "露露"]]
print(name_list[0]) #['孙俪', '谢娜', '贾玲']
print(name_list[0][0]) # 孙俪
print(type(name_list[0])) # <class 'list'>
print(type(name_list[0][0])) # <class 'str'>

print(name_list[0][1]) # 谢娜

#遍历列表
for i in name_list:
    print(i) # ['孙俪', '谢娜', '贾玲'] ['蓉蓉', '百合', '露露']
    # 遍历每一个列表中的元素
    for e in i:
        print(e)






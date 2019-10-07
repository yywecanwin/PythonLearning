# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/7

dict1 = {"name": "yao", "age": 20, "gender": "男", "height": 172}
# 方法一：
# 1、先得到所有的key组成的列表
key_list = dict1.keys()
print(key_list) # dict_keys(['name', 'age', 'gender', 'height'])
print(type(key_list)) # <class 'dict_keys'>
#2.遍历列表，得到key
for key in key_list:
    #3.在循环语句中通过key得到value
    value = dict1.get(key)
    # print("%s=%s" % (key,value))
    print(f"{key}={value}")

print("***"*10)

# 方法二：
#1.先得到所有的键值对组成的列表
item_list = dict1.items()
# print(item_list) # dict_items([('name', 'yao'), ('age', 20), ('gender', '男'), ('height', 172)])
# print(type(item_list)) # <class 'dict_items'>
# 2.遍历列表，遍历出键值对
# for key_value in item_list:
#     #key_value 是一个元组，比如：{'name','yao'}，第一元素key，第二个元素是value
#     #3.从键值对中取出key和value
#     key = key_value[0]
#     value = key_value[1]
#     print(f"{key}={key_value}")


for key,value in item_list: # key,value = 'name','yao'
    # key_value是一个元组，比如：('name','yao'),第一个元素是key，第二个元素是value
    # 3.从键值对中取出key和value
    # key = key_value[0]
    # key = key_value[1]
    print(f"{key}={value}")

# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/7

dict1 = {"邓超": "孙俪", "张杰": "谢娜", "吴京": "谢楠"}

#1、添加键值对的格式：字典名[新的key] = 值
dict1["李晨"] = "冰冰"
print(dict1)

#2.字典里只能修改value,不能修改key
#修改键值对中的value，字典名[已存在的key] = 新的值
dict1["张杰"] = "热巴"
print(dict1)

#3.珊瑚键值对，通过key删除键值对
dict1.pop("张杰")
print(dict1)

#删除最后一个键值对
dict1.popitem()
print(dict1)

#清空键值对
dict1.clear()
print(dict1)

#4、查找value，通过key查找：字典名[key]
# 如果key不存在，会报错
dict2 = {"阿杰": "爽儿", "阿琦": "千寻"}
print(dict2["阿杰"])
# print(dict2["阿奇"])

# 通过 字典名.get(key) 得到value，如果key不再得到的是None
print(dict2.get("阿杰"))
print(dict2.get("小王"))





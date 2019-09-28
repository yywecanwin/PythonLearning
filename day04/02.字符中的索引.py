# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28

string = "hello python"

# 根据索引查找元素，格式为：字符串名[索引]
#得到索引为0的元素
str1 = string[0]
print(str1) # h
print(type(str1)) # <class 'str'>

print(string[7]) # y

# 得到字符串的长度:len(字符串)
# len()函数：计算字符串的长度
length = len(string)
print(length) # 12

# 最后一个元素的索引是 长度-1：length-1
print(string[length-1]) # n
print(string[len(string)-1]) # n

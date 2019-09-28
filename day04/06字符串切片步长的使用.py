# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28
"""
字符串切片步长的格式：
    字符串名[开始索引：结束索引：步长]

    假如步长是n
    从 开始索引对应的元素截取，一直截取到 结束索引 对应的元素
    先 截取出 开始索引对应的元素，然后每次都是向后数n个元素，第n个元素是谁把谁截出来
    最后按照截取的先后顺序，组成一个字符串，这个字符串，就是截取的结果

"""
# 步长默认就是1,
s = "hello python"
print(s[2: 10: 2]) # lopt
print(s[2: 10: 1]) # llo pyth

print("************")
# 步长可以为 负数, 表示倒序截取
print(s[9: 2: -2]) # hy l
print(s[2: 10: -2]) #
print(s[-2: 3: -2]) # otpo

# 字符串的翻转（逆序）
print(s[::]) # hello python
print(s[::-1]) # nohtyp olleh

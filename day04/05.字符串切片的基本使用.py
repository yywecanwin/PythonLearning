# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28
"""
字符串切片的基本使用
    就是截取字符串

    切片的格式：
        字符串名[开始索引:结束索引]

        从开始索引 对应的元素截取，一直截取到结束索引对应的元素
        包含 开始索引 对应的元素，不包含结束索引 对应的元素

"""
s = "hello python"

# 从索引为1的元素截取到最后一个元素
print(s[1:10]) # ello pyth

# 从索引为6的元素截取到最后一个元素

print(s[6:12]) # python

# 如果截取到最后一个元素，结束索引可以不写
print(s[6:]) # python

#如果是从第一个元素开始截取，开始索引可以不写
print(s[0:10]) # hello pyth
print(s[:10]) # hello pyth

# 从都头截到尾
print(s[:]) # hello python

# 索引可以为 负数 , 倒数第一个元素的索引为-1,倒数第二个元素的索引为-2,往左依次减1

print(s[-10: -2]) # llo pyth
print(s[3: -2]) # lo pyth
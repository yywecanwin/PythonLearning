# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/29

# 1.判断字符串是否都是由字母组成的: s1.isalpha()
s1 = "hellopython"
print(s1.isalpha())

# 2.判断字符串是否都是由数字组成的: s1.isdigit()
s2 = "123456"
print(s2.isdigit())
print(s2.isdecimal())

# 3.判断字符串中的字母 是否都是大写,或者小写
s3 = "HEL123LO"
s4 = "hel123<>&?lo"
print(s3.isupper())
print(s4.islower())

# 4.判断字符串是否以另外一个字符串开头 或者 结尾
s5 = "hello world android java"
print(s5.startswith("hello"))
print(s5.startswith("h"))

print(s5.endswith("java"))
print(s5.endswith("d"))
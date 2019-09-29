# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/29

# 1.替换的方法：s1.replace(oldstr.newstr)
s1 = "helloapythoan"
reslut = s1.replace("oa","www",3)
print(reslut) # hellwwwpythwwwn

# 2.大小写转换的方法
s2 = "helLo123PYthon"
print(s2.upper()) # HELLO123PYTHON
print(s2.lower()) # hello123python

# 3.去掉空格
s3 = "  hello python "
print("a" + s3.strip() + "b")
print(s3.replace(" ", ""))

# 4对齐的方法

s4 = "hello"
print(s4.rjust(15)) # hellopython
print(s4.center(16))
print(s4.rjust(15))
print(s4.center(16))
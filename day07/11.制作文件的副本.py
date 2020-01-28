# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28


#1.打开原文件
f = open("a.txt","r")


# 2.得到原文件的路径，拆分出原文件名和扩展名（E:\\a.txt）
print(f.name)
print(type(f.name))

# 完整的路径
path = f.name # a.txt
index = path.rfind(".")
print(index) # 1

# 截取出，前面的部分
pre_fix = path[:index]
print(pre_fix) # a
# 截取出.后面的部分
last_fix = path[index:]
print(last_fix) # .txt


# 3.并接副本文件的路径
# E:\\a-副文本.txt
copy_path = pre_fix + "_副文本" + last_fix

# 4.打开副本文件
copy_file = open(copy_path,"w")


# 5.从原文件种读取所有数据
data = f.read()

# 6.把读到的数据写到副本文件中
copy_file.write(data)

# 7.关闭两个文件
f.close()
copy_file.close()





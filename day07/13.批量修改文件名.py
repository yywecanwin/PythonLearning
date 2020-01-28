# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

"""
E:\01-基础班课件\01-基础班（课件）\01-基础班（课件）\day07_文件操作\05_资料\图片
"""

import os

file_list = os.listdir("E:\\01-基础班课件\\01-基础班（课件）\\01-基础班（课件）\\day07_文件操作\\05_资料\图片")
print(file_list)

# 指定当前工作目录到:E:\01-基础班课件\01-基础班（课件）\01-基础班（课件）\day07_文件操作\05_资料\图片
os.chdir("E:\\01-基础班课件\\01-基础班（课件）\\01-基础班（课件）\\day07_文件操作\\05_资料\\图片")

for file_name in file_list:
    print(file_name)
    # 得到最后一个.对应的索引
    index = file_name.rfind(".")
    # 截取出.前面的部分
    pre_fix = file_name[:index]
    # 截取出.后面的部分
    last_fix = file_name[index:]

    # 并接出修改后的文件名
    new_name = pre_fix + "姚嵇" + last_fix

    # 对文件重命名
    os.rename(file_name,new_name)



    pass








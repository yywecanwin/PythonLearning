# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/4

list1 = ["yao","is","a","good","man"]

# 方式一：while循环语句
#作为元素的索引
i = 0
# while循环4次，len(列表名)
while i < len(list1):
    # 根据索引得到元素，列表名[索引]
    print(list1[i])
    i += 1

print("____________________")

# 方式二：for循环遍历
for e in list1:
    print(e)
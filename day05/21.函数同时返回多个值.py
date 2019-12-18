# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18
"""
函数同时返回多个值
"""

def get_num(a,b):
    s = a + b
    avg = s / 2
    multip = a * b

    #在返回之前,python解释器会自动对return后面的数据进行组包成一个元素
    return s,avg,multip # return (s,avg,multip)
result = get_num(12,12)
print(result) # (24, 12.0, 144)
print(type(result)) # <class 'tuple'>




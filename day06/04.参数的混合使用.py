# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/20

def sum_nums_3(a,*args,b=22,c=33,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

sum_nums_3(100,200,300,400,500,b=1,c=2,d=3,e=6)
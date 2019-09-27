# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

import random

# 1.从键盘上一个1-3之间的数字表示自己出的泉
self  =  int(input("请出拳"))

# 2.定义一个变量赋值为1，表示电脑的出泉
#得到一个1-3之间的随机数作为电脑出的拳
computer = random.randint(1,3)
#3.比较胜负
# 3.1比较自己赢的情况
if (self == 1 and computer == 2) or \
        (self == 2 and computer == 3) or \
        (self == 3 and computer == 1):
    print("哈哈哈,我又赢了!!! 不玩了!!")
elif self == computer:
    # 3.2 比较平局的情况
    print("平局!!!,再战一盘!!!!")
else:
    # 3.3 剩下的就是输的情况
    print("不行!!! 别走!!我要与你战斗到天亮!!!!")

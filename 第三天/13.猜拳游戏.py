# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/28

import random

# 写一个死循环
while True:
    # 1.从键盘录入一个1-3之间的数字表示自己出的拳
    self = int(input("请出拳"))
    # 2.定义一个变量赋值为1，表示电脑出的拳
    computer = random.randint(1,3)
    print(computer)
    if((self == 1 and computer == 2) or (self == 2 and computer == 3) or (self == 3 and computer == 1)):
        print("我又赢了，我妈喊我 回家吃饭了")
        break
    elif self == computer:
        print("平局，我们在杀一盘")
    else:
        print("不行了，我要和你杀到天亮")
        break


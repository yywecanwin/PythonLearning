# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27
"""
要想得到一个随机数,需要使用以下两个步骤:
    1.导入工具包:
        import random
    2. 调用工具包中的一个功能,得到某个范围内的随机数
        random.randint(开始数字,结束数字)
        包含开始数字和结束数字.
"""

import random

num = random.randint(1, 10)
print(num)

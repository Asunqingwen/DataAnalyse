# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 0019 16:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 随机漫步.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import random

import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in range(steps):
	step = 1 if random.randint(0, 1) else -1
	position += step
	walk.append(position)

plt.plot(walk[:100])

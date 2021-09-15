#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:27:28 2021

@author: Ariel
"""

# 用蒙特卡洛模拟的方法求π值
import random
import math

n = 1000000 #随机投掷100万次
r = 1.0 #内切圆边长设为1
a, b = (0.0, 0.0) #中心点坐标
x_neg, x_pos = a-r, a+r
y_neg, y_pos = b-r, b+r

count = 0.0
for i in range(0, n):
	x = random.uniform(x_neg, x_pos)
	y = random.uniform(y_neg, y_pos)

	if math.sqrt(x**2 + y**2) <= 1.0: #判定随机点与中心点的距离
	   count += 1

result = (count / n) * 4
print("Estimation of π is ", result)

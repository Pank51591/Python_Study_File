# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:26:17 2020
输入一个数，判断是否为素数

@author: pank
"""


num = int(input("输入一个数："))

for i in range(2, num):
    if num % i ==0:
        print("%d 不是素数" % num)
        break 
    else:
        print("%d 是素数" % num)
        break 
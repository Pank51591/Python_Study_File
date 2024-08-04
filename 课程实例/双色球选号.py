# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 08:28:53 2020

@author: lenovo
"""

from random import randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:  #列表
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]  #从1到33
    selected_balls = []  #创建一个空列表
    selected_balls = sample(red_balls, 6)  #对列表按给的的位数填充
    selected_balls.sort() #排序
    selected_balls.append(randint(1, 16))  #末位的两位数
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
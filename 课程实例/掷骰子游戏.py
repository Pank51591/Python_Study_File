# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:37:28 2020

@author: lenovo
"""

from random import randint

money = 1000

while money > 0:
    print("你的总资产是：%d" % money)
    need_go_on = False
    
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:  # 如果满足条件就继续往下执行，如果不满足的话就继续打印“请下注：”
            break 
        
    first = randint(1, 6) + randint(1, 6)
    print ("你摇出来的数是：%d" % first)
    
    if first == 7 or  first == 11:
        money += debt
        print("玩家胜！你的资产是： %d" % money)
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print("庄家胜！你的资产是：%d" % money)
    else:
        need_go_on = True
    
    while need_go_on:
        need_go_on = False
        count = randint(1, 6)  + randint(1, 6)
        print ("你摇出来的数是：%d" % count)
        
        if count == first:
            money += debt
            print("玩家胜！你的资产是： %d" % money)
        elif count == 7:
            money -= debt
            print("庄家胜！你的资产是：%d "% money)
        else:
            need_go_on = True
print("你 输 光 了 ！")
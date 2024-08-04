#AutoTraceDraw.py

import turtle as t       #使用别名

t.title("自动轨迹绘制")
t.setup(800,600,0,0)  #建立窗口      
t.pencolor("red")               
t.pensize(5)

#数据读取
datals = []             
f = open("data.txt","r")           #打开数据接口文件，然后通过for循环进行 分行读入，逐行处理
#for line in f.readlines()          #通过for循环，对文件 一次读入，分行处理
for line in f:
    line = line.replace("\n" , " ")   #元素替换，然后赋给line            
    datals.append(list(map(eval, line.split(","))))     #split函数是将每一行字符串按逗号分为若干个字符串，
                  #然后将该行转换为列表。map函数是将第一个元素的执行的eval函数的功能也作用给后面的每一个元素。
                  #最后再将一个新的列表放入到datals列表中。
f.close()

#自动绘制
for i in range(len(datals)):          #遍历二维列表
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])        
    t.fd(datals[i][0])
    if datals[i][1]:                  #检查第一个数据的值是否为 1
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

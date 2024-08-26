
from tkinter import *  #导入trkinter中的所有函数
import tkinter.messagebox
import tkinter #导入模块


top =  tkinter.Tk()

top.title("请选择你的家乡：")
top.geometry('300x200')  #设置窗口的大小

checkVar1 = IntVar()  #创建一个IntVar的变量，将用来表示是否选中
checkVar2 = IntVar()

def checkbutton_callback1():
    state = checkVar1.get()  #获取状态！
    if state == 1:
        print("湖北被选中")
    else:
        print("湖北取消选中")

def checkbutton_callback2():
    state = checkVar2.get()  #获取状态！
    if state == 1:
        print("广东被选中")
    else:
        print("广东取消选中")

#onvalue表示选中后的状态值（0-10）      #offvalue 表示未选中后的状态值
c1 = Checkbutton(top,text = "湖北",variable=checkVar1, onvalue = 1, offvalue = 0, command = checkbutton_callback1, height= 3, width = 5)  
c1.grid(row=0,column=0)
c2 = Checkbutton(top,text="广东",variable=checkVar2, onvalue=1, offvalue = 0, command = checkbutton_callback2, height=3, width = 5 )
c2.grid(row=1,column=0)                
                 


#c1.pack()  #居中摆放
#c2.pack()

top.mainloop()

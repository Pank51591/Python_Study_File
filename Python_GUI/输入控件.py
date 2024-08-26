from tkinter import *


top = Tk()   #创建应用程序主窗口
L1 = Label(top,bg="green",text="网站名1：")
#L1.pack(side= LEFT)
L1.grid(row =0,column=0)   #行/列

L2 = Label(top,bg="purple",text="网站名2：")
L2.grid(row=1,column=0)
#L2.pack(side= LEFT)

E1 = Entry(top,bd=3)  #bd:边框线条的宽度
#E1.pack(side= BOTTOM)
E1.grid(row=0,column=1)

E2 = Entry(top,bd=3)
E2.grid(row=1,column=1)
 
top.mainloop()
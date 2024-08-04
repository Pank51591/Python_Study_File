# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:44:20 2020
GUI应用通常是事件驱动式的，之所以要进入主事件循环就是要监听鼠标、
键盘等各种事件的发生并执行对应的代码对事件进行处理，
因为事件会持续的发生，所以需要这样的一个循环一直运行着等待下一个事件的发生。

@author: lenovo
"""

import tkinter as tk

class Application(tk.Frame):   # 基类 tk.Frame
    
    def __init__(self, master):
        super().__init__(master)   # 增量重载（派生类扩展定义与基类相同名称的方法）
        self.master = master   
        self.pack()
        self.create_widgets()

    def create_widgets(self):   #self 可以理解为一个装按钮的容器  
        """
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        
        """     #对按钮功能的两种书写方式
        
        self.hi_there = tk.Button(self, text="Hello World\n(click me)", 
                                  command=self.say_hi)
        self.hi_there.pack(side="top") 
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.pack(side="bottom")  #将按钮的位置设置在窗口的底部

    def say_hi(self):
        print("hi there, everyone!")

# 创建顶层窗口
root = tk.Tk()
root.title("请选择：")
root.geometry("300x200")
app = Application(master=root)   # 实例对象
app.mainloop()    # 开启主事件循环

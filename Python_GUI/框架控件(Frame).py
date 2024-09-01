from tkinter import *

def say_hi():
    print("hello ~!")

root = Tk()
root.geometry('320x200')
root.title("tkinter frame")

frame = Frame(root)     #创建一个主框架

Label3 = Label(root,text="主框架1",bg='green',font=("宋体",18)).pack()
frame.pack()


frame1 = Frame(frame)     #创建第二层框架1
frame2 = Frame(frame)     #创建第二层框架2


#在框架1中摆放的内容
label1 = Label(frame1,text="Label1",bg='red',justify=LEFT)
label1.pack(side=LEFT)

label2 = Label(frame1,text="Label2",bg='yellow',justify=LEFT)
label2.pack(side=LEFT)


#在框架2中摆放的内容
hi_there = Button(frame2,bg='green',text="say hi~",command=say_hi)
hi_there.pack(side=LEFT)

Label3 = Label(frame2,text='111111111')
Label3.pack(side=LEFT)

frame1.pack(padx=2,pady=2)    #padx:组件跟临近组件或窗体边界的距离
frame2.pack(padx=30,pady=30)

root.mainloop()

from tkinter import *

window = Tk()

window.title('My Window')

window.geometry('500x300')

l= Label(window,text = '    ',bg='green')
l.pack()

#
counter = 0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter += 1

#创建一个菜单栏，这里我们可以把他理解为一个容器
menubar = Menu(window)

filemenu = Menu(menubar,tearoff=0)

#将上面定义的空菜单命名为File，
menubar.add_cascade(label='File',menu = filemenu)

#在File中加入New,Open,Save等小菜单
filemenu.add_command(label = "New",command=do_job)
filemenu.add_command(label = "Open",command=do_job)
filemenu.add_command(label = "Save",command=do_job)
filemenu.add_separator()   #添加一条分割线
filemenu.add_command(label='Exit',command=window.quit) #

#创建一个Edit菜单项
editmenu = Menu(menubar,tearoff = 0)
#将上面定义的空菜单命名为 Edit,放在菜单栏中
menubar.add_cascade(label='Edit', menu = editmenu)

editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

#创建二级菜单
submenu = Menu(filemenu)
filemenu.add_cascade(label="Import",menu=submenu,underline =0)

submenu.add_command(label='Submenu_1',command=do_job)

window.config(menu=menubar)

window.mainloop()




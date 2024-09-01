from tkinter import *

window =  Tk()

window.geometry('500x300')

canvas1 = window.Canvas(window,bg='green',height= 200,width=500)

image_file = window.PhotoImage(file='pic.gif')    #图像位置 （相对路径）

image = canvas1.create_image(250,0,anchor='n',image=image_file)

x0,y0,x1,y1 = 100,100,150,150

line = canvas1.create_line(x0-)






import tkinter as tk
root = tk.Tk()

# 默认按钮
btn1 = tk.Button(root,background='red')
btn1
btn1['text'] = "按钮1"
btn1.pack()

if btn1['state'] == True:
    print(btn1.grid_info())


root.title('演示窗口')
root.geometry("300x150+1000+300")  
root.mainloop()

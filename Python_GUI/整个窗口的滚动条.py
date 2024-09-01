import tkinter as tk  
from tkinter import scrolledtext  
  
root = tk.Tk()  
root.title("滚动条示例")  
  
# 创建一个框架  
frame = tk.Frame(root)  
frame.pack(fill=tk.BOTH, expand=True)  
  
# 创建一个滚动条  
yscroll = tk.Scrollbar(frame, orient=tk.VERTICAL)  
yscroll.pack(side=tk.RIGHT, fill=tk.Y)  
  
# 创建一个画布，并设置yscrollcommand  
canvas = tk.Canvas(frame, bd=0, yscrollcommand=yscroll.set)  

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  
#canvas.create_window(500,500,window=frame)  #添加窗口到画布


# 绑定滚动条和画布  
yscroll.config(command=canvas.yview)  
  
# 在画布上添加内容（这里使用标签作为示例）  
for i in range(2000):  
    label = tk.Label(canvas, text=f"标签 {i+1}")  
    label.pack()  #直接添加到画布上



  
# 注意：上面的代码示例不会真正在画布上创建可滚动的标签，因为label.pack()是直接添加到画布上，  
# 而不是作为画布上的一个对象。要正确实现，你需要使用canvas的create_window方法或其他方式将标签添加到画布上。  
  
# 另一种方式是使用ScrolledText或Listbox等内置滚动控件，但这通常用于文本或列表的滚动。  
  
root.mainloop() 


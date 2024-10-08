
import tkinter
import tkinter.messagebox   #这个是消息框的内容


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag  #声明变量不在当前命名空间，而在上一层命名空间，但不在全局
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')  #Label widget which can display text and bitmaps.
    label.pack(expand=1)
    
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')   #
    
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
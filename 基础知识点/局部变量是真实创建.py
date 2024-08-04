ls = ["F","f"]
def func(a):
    ls = []      #真实创建局部变量
    ls.append(a)
    return
func("c")
print (ls)

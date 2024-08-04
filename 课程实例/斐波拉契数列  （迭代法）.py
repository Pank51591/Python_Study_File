m = eval(input ("请输入一个整数："))     #这个eval函数是必须的

def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1) + f(n-2)

a = f(m)
print ("{}".format(a))

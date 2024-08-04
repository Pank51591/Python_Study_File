#KochDrawV2.py
import turtle

def koch(size,n):           #size表示直线长度，n表示阶数
    if n==0:
        turtle.fd(size)
    else:                   #需要注意的是 for 循环的执行过程 （有3层循坏）
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3 , n-1)       #递归调用（这两个语句是连续的）

def main():
    turtle.setup(600,600)
    turtle.pencolor("purple")
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=3             #科赫雪花阶数
    koch(400,level)     #调用koch函数
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()     #最后隐藏海龟

main()

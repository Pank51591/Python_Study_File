# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:44:59 2020

静态方法采用<类名>.<方法名>（<参数列表>）或 <对象名>.<方法名>（<参数列表>）方法使用

@author: lenovo
"""

from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
    @staticmethod   #静态方法是定义在类中的普通函数，能够被所有实例对象共享
    def is_valid (a, b, c):
        return a+b>c and a+c>b and b+c>a 
    
    def perimeter(self):
        return self._a + self._b + self._c
    
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)  #实例对象
        print(t.perimeter())	
        print(t.area())
    else:
        print('无法构成三角形.')

def main2():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)   #实例对象
        # 也可以通过给类发消息来调用对象方法, 但是要传入接收消息的对象作为参数
        print(Triangle.perimeter(t))
        print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()
    main2()
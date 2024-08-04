#1、实例方法 （是类内部定义的函数，由实例对象所独享）
class DemoClass:

    def __init__ ( self,name ):   
        self.name = name
         #类的构造函数没有返回值

    def lucky(self):          #实例方法（相当于是一个函数）
        s = 0
        for c in self.name:
            s += ord (c) % 100
        return s         #实例方法需要与返回值
            
dc1 = DemoClass("老王")       #创建实例对象
dc2 = DemoClass("老李")
print(dc1.name,"幸运数字是：",dc1.lucky())
print(dc2.name,"幸运数字是：",dc2.lucky())     #实例方法的使用


#2、类方法（是与类对象相关的函数，由所有实例对象共享）
class DemoClass:
    count = 0
    def __init__ (self,name):   #类的构造函数
        self.name = name
        DemoClass.count += 1    #类属性的使用

    @classmethod   #类方法使用修饰器表示
    def getchrcount(cls):   #创建类方法|  cls表示类对象
        s = "零一二三四五六七八九十多"
        return s[DemoClass.count]     #返回第n个字符

de1 = DemoClass("老王")   #创建实例对象
de2 = DemoClass("老李")
print(de1.getchrcount())    #类方法的使用方法1
print(DemoClass.getchrcount())   #类方法的使用方法2   （两种方法返回结果相同）



#3、自由方法（是定义在类命名空间中的普通函数（可看成就是一个函数，不是方法））
class DemoClass:
    count = 0
    def __init__ (self,name):
        self.name = name
        DemoClass.count += 1        #类属性的使用

    def foo():                #创建自由方法
        DemoClass.count *= 200
        return DemoClass.count

dc1 = DemoClass("老王")
print(DemoClass.foo())        #自由方法的使用


#4、静态方法（是定义在类中的普通函数，能够被所有实例对象共享）
class DemoClass:
    count = 0
    def __init__ (self,name):
        self.name = name
        DemoClass.count += 1

    @staticmethod           #静态方法 修饰器
    def foo():         #创建静态方法|   只能操作类属性和其他类方法
        DemoClass.count *= 100
        return DemoClass.count

dc1 = DemoClass("老王")        #实例对象
print(DemoClass.foo())       #静态方法的使用1
print(dc1.foo())             #静态方法的使用2（ 调用第二次前，count的值已经变成了100） 


#5、保留方法（由双下划线开始和结束的方法，保留使用）
class DemoClass:
    count = 0
    def __init__(self,name):     #类的构造函数
        self.name = name
        DemoClass.count += 1

    def __len__(self):            #创建保留方法
        return len(self.name)     #返回字符串的长度值            

dc1 = DemoClass("老王")
dc2 = DemoClass("老李头")

print(len(dc1))
print(len(dc2))                  #保留方法的使用

























    


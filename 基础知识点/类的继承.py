#python类的继承 （代码复用的高级抽象）

#类继承的构建
class DemoClass:      #基类
    count = 0
    def __init__ (self,name):
        self.name = name
        DemoClass.count += 1
    def getName(self):
        return self.name

class HumanNameClass(DemoClass):    #派生类（类继承的构建）
    def printName(self):
        return str(DemoClass.count)+self.name+"同志"    #对基类属性的使用

dc1 = HumanNameClass("老王")         #派生类实例对象
print(dc1.getName())                 #对基类实例方法的使用
print(dc1.printName())               #对派生类实例方法的使用

#类继承关系的判断
print(isinstance(dc1,DemoClass))    #判断对象dc1是否是类DemoClass的子类实例
print(isinstance(dc1,HumanNameClass))   #判断对象dc1是否是HumanNameClass类的实例
print(issubclass(HumanNameClass,DemoClass))    #判断类HumanNameClass是否为DemoClass的子类

#objec类是Python最基础类的名字
print(object.__name__)    
print(object.__doc__)
print(object.__bases__)
print(object.__class__)
print(object.__module__)
print(object.__dict__)

#Python类对象的三个要素 以及两个与基础类有关的内置函数
print(id(dc1),type(dc1))             #获取实例对象的内存地址
print(id(DemoClass),type(DemoClass))
print(dc1 is DemoClass)              #判断实例对象与基类是否相等
print(type(object),type(type))       #类型函数


#类的重载（属性重载和方法重载）

   #属性重载
class DemoClass:
    count = 0           #类属性  被重载
    def __init__(self,name):     #构造方法  被重载
        self.name = name        #实例属性 被重载
        DemoClass.count += 1

class HumanNameClass(DemoClass):   #派生类
        count = 99     #类属性  被重载
        def __init__ (self,name):      #构造方法  被重载
            self.name = name        #实例属性 被重载
            HumanNameClass.count -= 1    #类属性用类名调用不容易被误解

        def printCount(self):
            return str(HumanNameClass.count) + self.name   #实例属性用对象名调用，容易被误解

dc1 = HumanNameClass("老王")
print(dc1.printCount())  #就近覆盖原则，优先使用派生类重定义的属性和方法

   #方法重载 (完全重载和增量重载)
class DemoClass:
    count = 0
    def __init__ (self,name):     #在派生类中被重载之后就不能再使用基类中的方法
        self.name = name
        DemoClass.count += 1
    def printCount(self):
        return str(DemoClass.count)+self.name

class HumanNameClass(DemoClass):
    def __init__ (self,name):
        self.name = name
        #DemoClass.count += 1
    def printCount(self):
        return super().printCount() + "同志"    #super() 增量重载（实际上返回了派生类对应的基类）

dc1 = HumanNameClass("老王")
print(dc1.printCount())         #输出结果为： 0老王同志


#类的多继承
class DemoClass:
    def __init__(self,name):
        self.name = name
    def printName(self):
        return self.name

class NameClass:
    def __init__(self,title):
        self.nick = title
    def printName(self):
        return self.nick + "同志"

class HumanNameClass(DemoClass,NameClass):  #多继承
    pass
dc1 = HumanNameClass("老王")
print(dc1.printName())   #printName()按照深度优先，从左至右查找  

#类的多继承的使用说明
class DemoClass:
    def __init__(self,name):
        self.name = name
    def printName(self):
        return self.name

class NameClass:
    def __init__(self,title):
        self.nick = title
    def printName(self):
        return self.nick + "同志"

class HumanNameClass(NameClass,DemoClass):   #多继承，super()也按深度优先，从左至右的方式寻找对应基类方法
    def printName(self):
        return super().printName() + "你好"  

dc1 = HumanNameClass("老王")
print(dc1.printName())        #结果为： 老王同志你好


















































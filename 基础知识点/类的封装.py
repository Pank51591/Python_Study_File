#Python类的封装  （属性和方法的抽象）

#私有类属性（仅供当前类访问的类属性，子类亦不能访问）
class DemoClass:       
    __count = 0            #私有类属性 加__
    def __init__ (self,name):
        self.name = name
        DemoClass.__count += 1         #私有类属性的内部使用

    @classmethod           #创建类方法
    def getCount(cls):
        return DemoClass.__count     #只能在私有类属性的内部使用

dc1 = DemoClass("老王")
dc2 = DemoClass("老李")
print (DemoClass.getCount())            #类的类属性的使用

#私有实例属性（仅供当前类内部访问的实例属性，子类亦不能访问）
class DemoClass:
    def __init__(self,name):
        self.__name = name       #私有实例属性定义

    def getName(self):   #实例对象
        return self.__name      #私有属性的内部使用
    
dc1 = DemoClass("老王")
dc2 = DemoClass("老李")
print(dc1.getName() , dc2.getName())     #对象方法
#print(dc1.__name , dc2.__name)    #错误   (类的外部无权限调用私有属性)
print(dc1._DemoClass__name)    #在类的外部访问私有属性需要加_<类名>__私有属性名

#私有方法（是类内部定义并使用的函数）
class DemoClass:

    def __init__(self,name):
        self.__name = name      #私有实例属性定义

    def __getName(self):        #私有方法的定义
        if self.__name != "":
            return self.__name     #私有实例属性的内部使用
        else:
            return "老张"

    def printName(self):        #公开方法
        return "{}同志".format(self.__getName())    #私有方法的使用

dc1 = DemoClass("老王")
dc2 = DemoClass("")
print(dc1.printName(),dc2.printName())     #在类的外部调用公开方法

#类的保留属性（为理解Pyhon类提供统一的属性接口）
class DemoClass:
    "A Demo Class"
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

dc1 = DemoClass("老王")
print(DemoClass.__qualname__ , DemoClass.__name__ , DemoClass.__bases__ ,DemoClass.__dict__)
print(dc1.__doc__ , dc1.__module__, dc1.__class__, dc1.__dict__)

#类的保留方法（python解释器预留的类方法）
class DemoClass:
    "A Demo Class"
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

dc1 = DemoClass("老王")
print(.__init__())







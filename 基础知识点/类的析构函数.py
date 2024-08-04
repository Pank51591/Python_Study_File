#类的析构函数（一般情况不需要撰写）
class DemoClass:
    def __init__(self,name):
        self.name = name

    def __del__(self):       #析构函数
        print("再见",self.name)

dc1 = DemoClass("老王")
dc2 = dc1          #此时的dc2并不是一个对象，而是一个指针
del dc1            #并不真正销毁对象，而是销毁引用
print(dc2.name)
del dc2            #只有实例对象被真实删除时，才调用析构函数内的语句


class DemoClass:
    def __init__(self,name):
        self.name = name

    def __del__(self):
        print("再见" , self.name)

dc1 = DemoClass("老王")
del dc1             #只有实例对象被真实删除时，才调用析构函数内的语句



#Python类的内存管理
import sys
class DemoClass:
    def __init__ (self,name):
        self.name = name
    def __del__ (self):
        return "再见" + self.name

dc1 = DemoClass("老王")
dc2 = dc1
print(sys.getrefcount(dc1))       #通过方法获得对象的引用次数（要减1）





















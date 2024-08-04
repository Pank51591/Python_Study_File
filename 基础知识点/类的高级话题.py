#类的高级话题

#命名空间的理解
count = 0    #模块的命名空间
def getCounting(a):
    count = 0     #第一层函数的命名空间
    if a != "":
        def doCounting():  
            #nonlocal count    #第二层函数命名空间（nonlocal 声明变量不在当前命名空间，变量在上一层命名空间，而不在全局）
            global count    #声明变量在全局命名空间
            count += 1
        doCounting()
    return count

print(getCounting("1"),count)
print(getCounting("2"),count)
print(getCounting("3"),count)    #用nonlocal 和 global声明命名空间所得到的结果不一样

#类的特征装饰器
class DemoClass:
    def __init__(self,name):
        self.name = name

    @property    #用于转换方法为属性
    def age(self):
        return self._age    #返回一个属性

    @age.setter     # <方法名>.setter 用于设定属性的赋值操作
    def age(self,value):    
        if value<0 or value>100:
            value = 30
        self._age = value    #对同名属性值的赋值操作进行处理

dc1 = DemoClass("老李")
dc1.age = -100       #在类的外部age 表现为属性
print(dc1.age)     #实例属性的使用

#自定义异常的类型
class DemoException(Exception):    #自定义一个异常类型（继承于Exception类）
    pass

try:    #捕捉这个异常
    raise DemoException()    #raise保留字专门用来在代码中产生异常

except DemoException:
    print("捕捉DemoExceoption异常")

class DemoException(Exception):
    def __init__(self,name,msg="自定义异常"):
        self.name = name
        self.msg = msg

try:
    raise DemoException("脚本错误")   #捕捉这个异常及异常对象e
except DemoException as e:     #try发生异常就执行except
    print("{}异常的警报是{}".format (e.name,e.msg))

#类的名称修饰(5种)

# _x
class DemoClass:
    def __init__(self,name):
        self.name = name
        self._nick = name +"同志"    #约定内部使用（但是没有约束）
    def getNick(self):
        return self._nick

dc1 = DemoClass("老李")
print(dc1.getNick())
print(dc1._nick)        #仍可以外部调用 （输出结果相同）

# x_
class DemoClass:
    def __init__(self,name):
        self.name = name
        self.class_ = name + "同志"    #仅是为了避免重名
    def getNick(self):
        return self.class_

dc1 = DemoClass("老李")
print(dc1.getNick())
print(dc1.class_)

# __x
class DemoClass:
    def __init__(self,name):
        self.name = name
        self.__nick = name + "同志"    #私有属性
    def getNick(self):
        return self.__nick

dc1 = DemoClass("老李")
print(dc1.getNick())
print(dc1._DemoClass__nick)    #调用的正确方式
#print(dc1.__nick)    #错误的引用方式

# __x__
class DemoClass:
    def __init__ (self,name):
        self.name = name
        self.__nick__ = name + "同志"    #正常的属性名称
    def getNick(self):
        return self.__nick__

dc1 = DemoClass("老李")
print(dc1.getNick())
print(dc1.__nick__)     #正确（区别于._x）

# _
class DemoClass:
    def __init__ (self,name):
        self.name = name
        _ = "同志"    #无关紧要的名字，以后不会用到
        self.__nick__ = name + _
    def getNick(self):
        return self.__nick__

dc1 = DemoClass("老李")
print(dc1.getNick())
print(dc1.__nick__)
































    
                

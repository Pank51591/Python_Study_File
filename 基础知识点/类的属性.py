#类的属性
class DemoClass:
    count = 0        #包含在类的整个空间中，这个变量叫做类属性
    def __init__ (self,name,age):     #类的构造函数
        self.name = name        #self.name 为类内部的实例属性
        self.age = age
        DemoClass.count += 1  # 类属性的使用方法
dc1 = DemoClass("老王",45)      # dc1为类的实例对象
dc2 = DemoClass("老李",52)
print("总数：",DemoClass.count)
print(dc1.name , dc2.name)    # 在类外部实例属性的使用方法

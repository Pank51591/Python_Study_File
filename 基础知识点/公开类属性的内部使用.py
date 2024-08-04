class DemoClass:
    count = 0   #公开类属性
    def __init__ (self,name):
        self.name = name
        DemoClass.count += 1    #类属性的内部使用
    
    def printCount(self):
        return str(DemoClass.count)+self.name

dc1 = DemoClass("老王")
print(dc1.printCount())

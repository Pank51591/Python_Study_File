#Python的多态

#方法参数类型的多态
class DemoClass:
    def __init__ ( self,name ):   
        self.name = name
            #类的构造函数没有返回值

    def __id__(self):    #重载了id（）函数对应的逻辑
        return len(self.name)
    
    def lucky (self,salt):    #需要方法能够处理不同的参数类型，如：整数，字符串和DemoClass类等
        s = 0
        for c in self.name:
            s += (ord (c)+id(salt)) % 100     #字符c的Unicode码和salt的地址码相加
        return s     #实例方法需要与返回值

dc1 = DemoClass("老王")
dc2 = DemoClass("老李")
print(dc1.lucky(10))
print(dc1.lucky("10"))
print(dc1.lucky(dc2))


#方法参数形式的多态
class DemoClass:
    def __init__ ( self,name ):   
        self.name = name
         #类的构造函数没有返回值

    def __id__(self):    #重载了id（）函数对应的逻辑
        return len(self.name)
    
    def lucky (self, salt = 0,more=9):    #需要方法能够处理可变参数
        s = 0
        for c in self.name:
            s += (ord (c)+id(salt) + more) % 100
        return s      #实例方法需要与返回值

dc1 = DemoClass("老王")
print(dc1.lucky())
print(dc1.lucky(10))
print(dc1.lucky(10,100))






















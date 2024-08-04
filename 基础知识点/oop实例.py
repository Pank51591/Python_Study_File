#面向对象的编程 
class Product ():                    #创建一个类
    def __init__(self , name):      #此处的__init__ 方法是类实例创建之后调用
        self.name = name
        self.label_price = 0
        self.real_price = 0
       
c = Product ("电脑")       
d = Product ("打印机")
e = Product ("投影仪")
c.labal_price,c.real_price = 10000,8000
d.labal_price,d.real_price = 2000,1000
e.label_price,e.real_price = 1500,900
s1 ,s2 = 0 , 0
for i in  [c, d, e]:
    s1 += i.label_price
    s2 += i.real_price
print(s1,s2)     

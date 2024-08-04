#引用：对象的指针

ls = [1,2,3,4]
lt = ls      #赋值
print(id(ls))
print(id(lt))

#不可变对象的引用：整数
a=10
b=a
c=10
print(id(a))
print(id(b))
print(id(c))

#不可变对象的引用：字符串
a = "Python计算生态"
b = a
c = "Python"
d = "计算生态"
e = c + d       #运算后产生的对象由解释器重新建立
f = "Python计算生态"
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))

#可变对象的引用
la = []
lb = la
lc = []    #每个可变对象都由解释器重新创建，不复用内存
print(id(la))
print(id(lb))
print(id(lc))

la = []
lb = la
lb.append(1)
print(la,id(la))
print(lb,id(lb))    #对象修改后，所有引用的引用值都被修改

#对象的拷贝（新的对象，内存空间有变化）

ls = ["Python",[1,2,3]]
la = ls.copy()
lb = ls[:]    #切片操作
lc = list(ls)    #列表lc
print("ls",id(ls),ls)
print("la",id(la),la)
print("lb",id(lb),lb)
print("lc",id(lc),lc)    #地址不一样，对象被复制

#浅拷贝
ls = ["Python",[1,2,3]]
la = ls.copy()
lb = ls[:]    #切片操作
lc = list(ls)    #列表lc

for i in [ls,la,lb,lc]:
    for c in i:
        print(c,id(c),' ',end=" ")
    print("",i,id(i))    #由结果可看出，列表被拷贝，但元素没有被拷贝 


lc[-1].append(4)       #修改的是元素所以四个列表结果相同
print(lc,la)
print(ls,lb)


class DemoClass:
    def __init__(self,name):
        self.name = name
    def lucky (self,salt=0):
        s = 0
        for c in self.name:
            s += (ord(c) + id(salt)%100)
        return s

dc1 = DemoClass("老李")
Lucky = dc1.lucky      #将使用方法 简化
print(DemoClass.lucky(dc1,10))
print(dc1.lucky(10))
print(Lucky(10))     #三个使用方法输出的结果相同
                
#深拷贝
import copy
ls = ["python",[1,2,3]]
lt = copy.deepcopy(ls)     #深拷贝的方法
for i in [ls,lt]:
    for c in i :
        print(c,id(c),"",end="")
    print("",i ,id(i))     #列表内部各可变对象元素都被拷贝 （此时元素的内存空间发生“变化”）
    






























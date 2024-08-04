#类的运算

class NewList(list):             #继承list类型的新类型
    def __add__ (self,other):         #重载其中的加法运算
        result = []
        for i in range (len(self)):
            try:
                result.append (self[i]+other[i])
            except:
                result.append (self[i])
        return result
ls = NewList([1,2,3,4,5,6])
lt = NewList([1,2,3,4])
print(ls + lt)                  #对两的对象进行进行加法运算

#比较运算
class NewList(list):        #继承list类型的新类型
    def __lt__ (self,other):      #重载其中的小于比较运算 
        "以各元素算术和为比较依据"
        s,t = 0,0
        for c in self:
            s += c
        for c in other:
            t += c
        return True if s<t else False
ls = NewList([6,1,2,3])
lt = NewList([1,2,3,99])
print([6,1,2,3]<[1,2,3,99])        #比较第一个元素的Ulike码
print(ls<lt)              #比较每个列表的元素和

#成员运算符的重载
class NewList(list):              #继承list类型的新类型
    def __contains__(self,item):        #重载其中的成员判断运算
        "各元素算术和也作为成员"
        s = 0
        for c in self :
            s += c     #求和
        if super().__contains__(item) or item == s:     # item是参数   使用增量重载
            return True
        else:
            return False

ls = NewList([6,1,2,3])
print(6 in ls , 12 in ls)            #对实际参数进行判断

#其他运算的重载
class NewList(list):                 #继承list类型的新类型
    def __format__(self,format_spec):    #重载其中的格式化运算  
        "格式输出，以逗号分隔"
        t = []
        for c in self:
            if type(c) == type("字符串"):
                t.append(c)           # append() 方法用于在列表末尾添加新的对象。
            else:
                t.append(str(c))      # str 将数据类型转换成字符串类型
        return ", ".join(t)           #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
ls = NewList([1,2,3,4])
print(format([1,2,3,4]))
print(format(ls))                 #格式化输出，并与列表类型比较




















    

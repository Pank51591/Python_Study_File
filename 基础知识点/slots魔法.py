# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:01:55 2020
如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

@author: lenovo
"""

class Person (object):
    
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')   # slots魔法
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name 
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
        
    def play(self):
        if self._age < 16:
            print("%s 在看电视" % self._name)
        else:
            print("%s 在玩游戏" % self._name)
            
def main():
    person = Person('王大锤',20)
    person.play()
    person._gender = "男"
    
if __name__ == "__main__":
    main()
    
    
    
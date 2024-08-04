# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:46:13 2020
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，
所以子类比父类拥有的更多的能力，
在实际开发中，我们经常会用子类对象去替换掉一个父类对象

@author: lenovo
"""

class Person(object):
    """人"""

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
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):    #继承
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)     # 增量重载，派生类扩展定义与基类相同名称的方法。
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):   #继承
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)    
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()
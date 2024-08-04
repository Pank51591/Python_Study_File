# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 07:55:43 2020

类方法采用<类名>.<方法名>(<参数列表>)或<对象名>.<方法名>(<参数列表>)方式使用

@author: lenovo
"""

from time import time, localtime, sleep

class Clock (object):
    """数字时钟的显示"""
    
    def __init__(self, hour= 0, minute= 0, second= 0):
        self._hour = hour
        self._minute = minute
        self._second = second
        
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
                    
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)
             
def main():
    clock = Clock.now()  #实例对象
    while True:
        print(clock.show())  # 对象名.方法名
        sleep(1)
        clock.run()
            
if __name__ == '__main__':
    main()
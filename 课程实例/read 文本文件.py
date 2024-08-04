# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:02:07 2020
除了使用文件对象的`read`方法读取文件之外，
还可以使用`for-in`循环逐行读取
或者用`readlines`方法将文件按行读取到一个列表容器中

@author: lenovo
"""

import time

def main():
    
    try:
        with open("致橡树.txt", 'r', encoding= "utf-8") as f:
            print(f.read())     # 一次性读入
            print()
        
        with open("致橡树.txt", 'r', encoding= "utf-8") as f:
            for line in f :
                print(line, end= '')  # 逐行读入
                time.sleep(0.5)
            print()
        print()
        
        with open("致橡树.txt") as f:
            lines = f.readlines()    # 读取文件按行读取到列表中
            print(lines, end='')
           
        
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
        
if __name__ == "__main__":
    main()
    

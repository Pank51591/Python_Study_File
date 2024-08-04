# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:20:47 2020

@author: lenovo
"""

from math import sqrt

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')   #元组类型
    fs_list = []   # 创建空列表
    try:
        for filename in filenames:
             # Append object to the end of the list
            fs_list.append(open(filename, 'w', encoding='utf-8'))   
        for number in range(1, 10000):
            if is_prime(number):    # 逐个判断是否为素数
                if number < 100:
                    fs_list[0].write(str(number) + '\n')   # str（）转换成字符串
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:  # Base class for I/O related errors.
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')

if __name__ == '__main__':
    main()
#!/usr/bin/env python
#coding:utf-8

# 导入系统库
import os
import sys
import time

# 应用库导入：如果需要引用的库未安装，则自动安装
try:   
    import schedule
    import pyautogui
except  ImportError:
    import pip
    pip.main(["install", "--user", "schedule","pyautogui"])
    import schedule
    import pyautogui

# svn 列表，注意路径使用linux的"/"分割
svn_list = ["E:/1.HET_Project/084-C2201A",
            "E:/1.HET_Project/357-A2142A",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/台湾向/089-C2106A",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/香港向/089-C2106B",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/香港向/089-C2106C",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/香港向/089-C2119D",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/香港向/089-C2119E",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/中国向/089-B2017B",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/中国向/089-B2017C",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/中国向/089-B2125B",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/中国向/089-B19110B",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/中国向/089-B19110C",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/中国向/089-B19110D",
            "E:/1.HET_Project/Panasonic浴霸RF遥控器/SVN文件夹/越南向/089-C2203A",
            "E:/1.HET_Project/P40控制板和显示板/560-C2201A"
            ]

def svn_auto_commit_job():
    for path in svn_list:
        print("auto commit:"+ path)
        os.chdir(path)
        r=os.popen('svn st')
        info = r.readlines()
        for line in info:
            one=line[:1] # 获取第一个字符
            tow=line[1:].lstrip() # 获取文件名
            #print(one)
            #print(tow)
            if one == '?':
                os.system('svn add \"%s\"' % tow )
            elif one == '!':
                os.system('svn delete \"%s\"' % tow)
        os.system('svn commit -m \"auto commit every day by panke\"')

def i_need_work():
    pyautogui.press("scrolllock")

if __name__=="__main__":
    print("svn_auto commit starting...")
    while True:
        try:
            schedule.every().day.at("17:20").do(svn_auto_commit_job)         # 每天在 17:20 时间点运行上传SVN
            #schedule.every(1).minutes.do(i_need_work)                       # 每隔 1分钟运行一次不熄灭屏幕程序

            while True:
                schedule.run_pending()
                time.sleep(1)
        except:
            print("except !!!")


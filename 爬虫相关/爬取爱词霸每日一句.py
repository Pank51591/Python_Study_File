# 小技巧：pycharm中，alt+enter快捷键可快速安装缺失库
import json      #json (JavaScript Object Notation) 是一种轻量级的数据交换格式，它是JavaScript的子集，易于人阅读和编写。
                 #前端和后端进行数据交互，其实就是JS和Python进行数据交互
import requests       #Requests模块是一个用于网络访问的模块

# 爬取爱词霸每日鸡汤
def get_iciba_everyday_chicken_soup():
    url = 'http://open.iciba.com/dsapi/'     # 爱词霸网站地址  (打开源代码)
    r = requests.get(url) 
    all = json.loads(r.text)  # 获取到json格式的字符串解码成Pyhon对象
    # print(all)   # json内容，通过这行代码来确定每日一句的键名
    English = all['content']   # 提取json中的英文鸡汤
    Chinese = all['note']   # 提取json中的中文鸡汤
    everyday_soup = English+'\n'+Chinese   # 合并需要的字符串内容
    return everyday_soup   # 返回结果

print(get_iciba_everyday_chicken_soup())

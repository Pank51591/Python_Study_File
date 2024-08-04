d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
print (d["中国"])

de = {} ; a = type (de)    #检测一个变量的类型
print(a)

de =set() ; a = type (de)
print(a)

de =[]  ; a=type (de)
print(a)

d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
a = "中国" in  d         #判断是否为键值
print(a)     

a=d.keys()              #返回字典d中所有键的信息
print(a)           

a=d.values()            #返回字典中所有值信息
print(a)

a=d.get("中国","伊斯兰堡")       #键存在则返回键，不存在则返回后面的 字符串
print(a)

a=d.get("巴基斯坦","伊斯兰堡")
print(a)

a=d.popitem()           #随机从字典中取出一个键值对以元组形式返回
print(a)

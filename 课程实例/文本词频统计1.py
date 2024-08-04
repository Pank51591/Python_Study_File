#CalHamletv1.py
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%()*=-,./:;<=>?@[\\]^_‘{|}~' :
        txt = txt.replace(ch," ")    #将文本符号替换位空格
    return txt

hamletTxt = getText()       #对文件进行读取
words = hamletTxt.split()   #变成列表类型
counts = {}                 #定义空字典类型
for word in words:
    counts[word] = counts.get(word,0) + 1     #用字典操作
items = list(counts.items())       #变形列表类型
items.sort(key=lambda x:x[1], reverse = True)    #排序  lambda函数
for i in range (10):
    word, count = items[i]
    print ( "{0:<10}{1:>5}" .format(word,count))

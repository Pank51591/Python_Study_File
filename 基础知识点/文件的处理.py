#文本形式打开文件
tf = open("f.txt","rt")
txt = tf.readline() 
print(txt)
tf.close ()

#二进制形式打开文件
bf = open("f.txt","rb")
txt = bf.readline()
print(txt)
bf.close ()


#文件的全文本操作（遍历全文本）

fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
txt = fo.read()
#对全文本txt进行处理(一次读入，统一处理)
fo.close()


fname = input("请输入要打开的文件名：")
fo = open(fname,"r")
txt = fo.read(2)
while txt != "":
#对txt进行处理 （按数量读入，逐步处理）
    txt = fo.read(2)
fo .close()


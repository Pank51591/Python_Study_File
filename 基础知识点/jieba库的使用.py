import jieba

a = jieba.lcut("中国是一个伟大的国家")         #精确模式，返回一个列表类型的分词结果
print (a)

d = jieba.lcut("中国是一个伟大的国家",cut_all = True)   #全模式，返回一个列表类型的分词结果存在冗余
print(d)

s = jieba.lcut_for_search("中华人民共和国是伟大的")     #搜索引擎模式，返回一个列表类型的分词结果，存在冗余
print (s)

jieba.add_word("蟒蛇语言")       #向分词字典中增加新词


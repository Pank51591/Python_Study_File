ls = ["cat","dog","tiger",1024]
print(ls)

lt = ls
print(lt)

ls[1:2] = [1,2,3,4]        #切片操作，将dog替换为1，2，3，4
print(ls)

del ls[::3]                #删除以3为步长的列表子序列
print(ls)

print(ls*2)

lt = ["cat","dog","tiger",1024]       # lt在之前是改变过的，去掉这一行得到的结果不一样
lt.append(1234)
print(lt)

lt.insert(3,"human")
print(lt)

lt.reverse()
print(lt)

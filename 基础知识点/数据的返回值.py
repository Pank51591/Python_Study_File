def fact(n,m):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m,n,m

a , b, c= fact(10,10)
print (a,b,c)

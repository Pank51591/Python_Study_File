def fact (n,*b):
    s = 1
    for i in range(1,n+1):
        s *= i
    for item in b:
        s *= item
    return s
a = fact(10,3,5,8)
print(a)
         

#Calstatisticsv1.py
def getNum():       #获取用户不定长度的输入
    nums = [ ]
    iNumstr = input("请输入数字（回车输出):")
    while iNumstr !="" :           #为空时 表示输入完毕
        nums.append(eval(iNumstr))     #列表
        iNumstr = input("请输入数字（回车输出）:")
    return nums

def mean(numbers):             #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers,mean):          #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)** 2
    return pow(sdev/(len (numbers) - 1) , 0.5)

def median(numbers):           #计算中位数
    sorted(numbers)            #对列表进行排序   （默认是又小到大）
    size = len(numbers)
    if size % 2 == 0 :         #取余 如果为偶数个求平均值
        med = (numbers[size//2-1] + numbers[size//2])/2   
    else:
        med = numbers[size // 2]
    return med

n = getNum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数:{}.".format(m,dev(n,m),median(n)))  #函数调用




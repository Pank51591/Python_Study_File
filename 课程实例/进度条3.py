#TextProBarV3.py （通过cmd在指点文件夹下运行）

import time
scale = 50
print("执行开始". center (scale//2,"-"))      #格式

start = time.perf_counter()            #计时开始
for i in range (scale + 1):   
    a = "*" * i                   #表示重新出现的次数
    b = "." * (scale - i)
    c = (i/scale)*100             #加载进度需要用百分号来表示
    dur = time.perf_counter() - start
    print ("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end=' ')  # “/r”表示光标返回到本行首
    time.sleep(0.1)

print("\n"+"执行结果".center (scale//2,'-'))    

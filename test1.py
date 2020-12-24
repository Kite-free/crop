#找车牌趣味问题:
# 现场有三人目击该事件，但都没有记住车号，只记下了车号的一些特征。
# 甲说：牌照的前两位数字是相同的；乙说：牌照的后两位数字是相同的，但与前两位不同；
# 丙是数学家，他说：4位的车号刚好是一个整数的平方。请根据以上线索求出车号。

import time
start = time.perf_counter()
a = [str(i) for i in range(10)]
b = [str(i) for i in range(10)]
for i in a:
    for j in b:
        if i != j:
            c = i + i + j + j
            # print(c)
            d = int(c)
            # print(d)
            e = d**0.5
            # print(e)
            if  e - int(e) == 0:
                print("车牌号为：" + c)
                break
            else:
                continue
end = time.perf_counter()
print("运行时间为：", end - start)

start2 = time.perf_counter()
for i in range(10):
    for j in range(10):
        if i != j:
            c = i*1000 + i*100 + j*10 + j
            e = c**0.5
            # print(e)
            if  e - int(e) == 0:
                print("车牌号为：", c)
                break
            else:
                continue
end2 = time.perf_counter()
print("运行时间为：", '{:.20f}'.format(end2 - start2))#格式化浮点数
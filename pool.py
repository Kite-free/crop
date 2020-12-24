from multiprocessing import Pool
import time


#杨氏三角形生成器：
def yangshi(n):
    list = []
    for i in range(n):
        list1 =[1]
        if len(list) < 2:
            list.append(1)
            print(list)
        else:
            for i in range(len(list)-1):
                list1.append(list[i]+list[i+1])
            list1.append(1)
            list = list1
            print(list)


def main():
    p = Pool(5)#1111
    start = time.perf_counter()
    p.map(yangshi,range(0,6))#2222
    end = time.perf_counter()
    p.close()#3333
    p.join()#4444
    print('process end and ru time:%0.1d'%(end-start))


if __name__ == "__main__":
    main()
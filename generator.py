
#杨氏三角形生成器：
def yangshi(n):
    list = []
    for i in range(n):
        list1 =[1]
        if len(list) < 2:
            list.append(1)
            yield (list)
        else:
            for i in range(len(list)-1):
                list1.append(list[i]+list[i+1])
            list1.append(1)
            list = list1
            yield (list)

def main():
    for i in yangshi(10):
        print(i)

if __name__ == "__main__":
    main()
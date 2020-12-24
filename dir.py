import os

# print(os.getcwd()) 获取当前目录路径
key = input("请输入要搜寻的关键词：")
def finddir(pathdir):
    path = []
    list1 = [x for x in os.listdir(pathdir)if os.path.isdir(x)]
    for i in list1:
        path.append(pathdir +'/'+ i)
    return path

def findfile(path):
    list = [x for x in os.listdir(path)if os.path.isfile(x)]
    for i in list:
        if key in i:
            print(path + '/' + i)


def main():
    path = ['.']
    while True:
        for i in path:
            findfile(i)
        for i in path:
            p = finddir(i)
            if len(p) == 0:
                break
            path = p


if __name__ == "__main__":
    main()

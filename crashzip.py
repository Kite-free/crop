import zipfile
import itertools

def extract(pword):
    file = zipfile.ZipFile("zip.zip", "r")
    file.extractall(path='.', pwd=pword.encode('utf-8'))


# def find():
#     it = itertools.count(1)
#     for i in it:
#         try:
#             extract(str(i))
#         except Exception:
#             if i == 99999:
#                 print("没有找到")
#                 break
#             continue
#         else:
#             print("密码为：", i)
#             break
# find()


# def find():
#     its = itertools.count(1)
#     it = itertools.takewhile(lambda x: x<=100000,its)
#     for i in it:
#         try:
#             extract(str(i))
#         except Exception:
#             if i == 99999:
#                 print("没有找到")
#                 break
#             continue
#         else:
#             print("密码为：", i)
#             break
# find()



list1 = [str(i) for i in range(10)]#0-9
list2 = [chr(i) for i in range(65, 91)]#A--Z
list3 = [chr(i) for i in range(97, 123)]
print(list1, '\n', list2, '\n', list3)
a =[]
password = itertools.permutations(list1, 5)
for i in password:
    a.append("".join(i))
print(a)
for i in a:
    try:
        extract(i)
        print(i)
    except :
        continue
    else:
        print("密码是：", i)
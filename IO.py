# -*- coding: utf-8 -*-
import os,sys
with open('test.txt','r',encoding='utf-8') as f:
    # print(f.read())#size大小为字节
    # print(f.readline())
    for i in f.readlines():
        print (i.strip())#去掉末尾的\n
 # f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')#errors 可以忽略一些编码报错
print(os.path.abspath('.'))
print(os.environ.get('PATH'))#获得环境变量path的值
print(os.path.split(r'C:\Users\admin\Desktop\crop\test.txt'))#将路径拆分为两部分
print(os.path.splitext(r'C:\Users\admin\Desktop\crop\test.txt'))#获得文件扩展名
list = [x for x in os.listdir('.')if os.path.isdir(x)]#获取当前路径下所有文件目录
list1 = [x for x in os.listdir('.')if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
#获取当前路径下扩展名为.py的文件
print(list)
print(list1)

#输入要查找的文件名  查找当前文件夹下该文件的相对目录：

import os
path = os.path.abspath('.')
target_str = input('请输入要搜索的文件名关键字：')
for root, dirs, files in os.walk(path):
    for file in files:
        if target_str in file:
         print(os.path.join(root.replace(os.getcwd(),'.'), file))
         # print(os.path.join(root, file))
# os.walk
# root 所指的是当前正在遍历的这个文件夹的本身的地址
# dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
# files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
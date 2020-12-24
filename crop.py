import os
import cv2
import numpy as np
n = 0

def crop_img(img_address, img_name): 
    img = cv2.imread(img_address)
 
    if (img.shape[1]) % 4096 == 0:
        x_num = (img.shape[1]) // 4096
    else:
        x_num = (img.shape[1]) // 4096 +1
    if (img.shape[0]) % 4096 == 0:
        y_num = (img.shape[0]) // 4096
    else:
        y_num = (img.shape[0]) // 4096 +1

    x_re=4096 * x_num
    y_re=4096 * y_num
    
    img_r=x_re-img.shape[1]  #第0个维度填充需要的像素点个数
    img_b=y_re-img.shape[0]  #第1个维度填充需要的像素点个数
    img_t = cv2.copyMakeBorder(img,0,img_b,0,img_r, cv2.BORDER_CONSTANT,value=0) 

    
    global n
    n += 1
    os.makedirs(out_address + "\\" + "inbay" + str(n), exist_ok=True)
    for y in range(0, y_num):
        for x in range(0, x_num):
            cropped = img_t[4096*y : 4096*y+4096, 4096*x : 4096*x+4096]
            crop_name = img_name + '_'+ str(y) + '_' + str(x) + '.tif'
            cv2.imwrite(out_address + "\\" + "inbay" + str(n)+"\\" + crop_name, cropped)
    print('successfully cropped' + img_name) 

def crop_imgs(img_folder): 
    img_names = os.listdir(img_folder) 
    for name in img_names:       
        crop_img(address+name, name)

if __name__ == '__main__':
    address = 'G:\\SRC\\'
    out_address = 'G:\\DST\\'
    crop_imgs(address)

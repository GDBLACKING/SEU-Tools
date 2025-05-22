# -*- coding: utf-8 -*-
"""
    Author:Song Wei
    Email:<220225876@seu.edu.cn>

    *以Csv形式存储Pngs，避免多次处理图片
"""

#%%
import numpy as np
import binascii

def pcap2png(filepath, img_size, img_column):
    with open(filepath, 'rb') as f:
        content = f.read()
    ''' 转换为16进制
        data = b"hello world"
        hexstr = binascii.hexlify(data)
        print(hexstr)  # 输出：b'68656c6c6f20776f726c64'
    '''
    hexadecimal = binascii.hexlify(content)
    while len(hexadecimal) < img_size:
        hexadecimal += b'0' # padding
    image_hex = hexadecimal[:img_size]
    fh = np.array([int(image_hex[i:i+2],16) for i in range(0, len(image_hex), 2)])  # 字节转换
    img_row = int(len(fh) / img_column)    # 确保整除
    image = np.reshape(fh[:img_row * img_column],(-1, img_column))
    image = np.uint8(image)
    return image

#%%
import  os
from utils.csv_writer import write_csv

abspath = os.path.abspath('.')
folders_path = "4_Session_Pcaps"

print("Pcap to PNGs Start ...")
folders= os.listdir(folders_path)
for folder in folders:
    folder_path = os.path.join(folders_path,folder)
    print(f"folder {folder} Converting ...")

    files= os.listdir(folder_path)
    for file in files:
        file_path = folder_path+"\\"+file
        if file_path.endswith(".pcap"):
            pngs = pcap2png(file_path, img_size = 784, img_column = 28)

            name1 = file_path.split('\\')
            path = abspath + '\\' + '6_PNGs' + '\\' + name1[-2]
            if not os.path.exists(path):
                os.mkdir(path)
            name2 = name1[-1].split('\\')
            png_name = path+"\\"+name2[0]+".csv"
            for i in range(pngs.shape[0]):
                write_csv(png_name, pngs[i,:])
print("Pcap to PNGs Ends ...")


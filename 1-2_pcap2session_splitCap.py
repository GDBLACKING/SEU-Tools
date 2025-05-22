"""
    Author:Song Wei
    Email:<220225876@seu.edu.cn>

    -2_Raw_Pcaps
        -folder
            -file
"""
import os
from utils.packet_spliter_old import packet_split
abspath = os.path.abspath('.')

path = "2_Raw_Pcaps"
folders= os.listdir(path)
print("Pcap to 4_Session_Pcaps Start ...")
for folder in folders:
    folder_path = os.path.join(path,folder)
    if os.path.isdir(folder_path):
        #print(f"folder {folder} Converting ...")
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path,file)
            if file_path.endswith(".pcap"):
                p = abspath+"\\"+file_path
                print(p)
                packet_split(p)

                # print("\""+file_path+"\"")
                # subprocess.run(f"cd 1_Tool && SplitCap.exe -r \"{abspath}/{file_path}\" -o \"{abspath}/4_Session_Pcaps/{folder}/{file}\" -s flow", shell=True)
                #flowProcess("cd 1_Tool && SplitCap.exe -r \"{abspath}/{file_path}\"","\"{abspath}/4_Session_Pcaps/{folder}/{file}\"")
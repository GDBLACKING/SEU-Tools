"""
    Author:Song Wei
    Email:<230258671@seu.edu.cn>

    -2_Raw_Pcaps
        -folder
            -file
"""
import os
from utils.packet_spliter import packet_split
abspath = os.path.abspath('.')
mode = "session"

path = "2_Raw_Pcaps"
folders= os.listdir(path)
print("Pcap to Sessions Start ...")
for folder in folders:
    folder_path = os.path.join(path,folder)
    if os.path.isdir(folder_path):
        print(f"folder {folder} Converting ...")
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path,file)
            if file_path.endswith(".pcap"):
                p = abspath+"\\"+file_path
                packet_split(p,mode)
print("Pcap to Sessions Ends ...")
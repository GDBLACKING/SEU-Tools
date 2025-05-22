# -*- coding: utf-8 -*-

import  os
from scapy.all import *
from utils.csv_writer import write_csv
from utils.packet_parsing import packet_parse

abspath = os.path.abspath('.')
input_path = "4_Session_Pcaps"
output_path = "5_Session_Csvs"

print("Pcap to Csvs Start ...")
folders= os.listdir(input_path)
for folder in folders:
    folder_path = os.path.join(input_path,folder)
    print(f"folder {folder} Converting ...")
    files= os.listdir(folder_path)
    for file in files:
        file_path = folder_path+"\\"+file
        if file_path.endswith(".pcap"):
            packets = rdpcap(file_path)
            name1 = file_path.split('\\')
            path = abspath + '\\' + output_path + '\\' + name1[-2]
            if not os.path.exists(path):
                os.mkdir(path)
            name2 = name1[-1].split('\\')
            csv_name = path+"\\"+name2[0]+".csv"
            title = "TimeStamp" + "," + "Src" + "," + "Dst" + "," + "sprot" + "," + "dport" + "," + "proto" + "," + "length" + "," + "id" + ","  + "flags" + ","  + "ttl"
            write_csv(csv_name, title)
            for packet in packets:
                five_tuple, complete_tuple = packet_parse(packet)
                if five_tuple=="not IP":
                    continue
                write_csv(csv_name, complete_tuple)
print("Pcap to Csvs Ends ...")


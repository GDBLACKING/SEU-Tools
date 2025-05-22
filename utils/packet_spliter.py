# -*- coding: utf-8 -*-
from scapy.all import *
from packet_parsing import packet_parse
from scapy.utils import PcapWriter

def packet_split(pcap,split_mode):
    abspath = os.path.abspath('.')
    packets = rdpcap(pcap)
    flow_list = []
    wrong_data = 0
    for packet in packets:
        five_tuple,complete_tuple = packet_parse(packet)
        if five_tuple == "not IP":
            print(complete_tuple) #layer.name
            continue

        file_name = pcap.split('\\')
        sub_pcap_path = abspath + '\\' + '4_Session_Pcaps'+ '\\' + file_name[-2]
        if not os.path.exists(sub_pcap_path):
            os.mkdir(sub_pcap_path)
        five_tuple = five_tuple.replace('.', '-')

        if split_mode == "flow":
            if five_tuple not in flow_list:
                flow_list.append(five_tuple)
        elif split_mode == "session":
            tup = five_tuple.split('_')
            five_tuple1 = tup[0]+"_"+tup[3]+"_"+tup[4]+"_"+tup[1]+"_"+tup[2]
            if five_tuple not in flow_list and five_tuple1 not in flow_list:
                flow_list.append(five_tuple)
            if five_tuple1 in flow_list:
                five_tuple = five_tuple1
        sub_pcap_name = './4_Session_Pcaps' + "/" + file_name[-2] + "/" + five_tuple + '.pcap'
        writer = PcapWriter(sub_pcap_name, append=True)
        try:
            writer.write(packet)
            writer.flush()
        except AttributeError:
            wrong_data = wrong_data + 1
            print("AttributeError")
        writer.close()
    return wrong_data

# packet_split("D:\\研究生\\科研\\APT分类\\基于Transformer的APT分类\\SEU-UTool\\2_Raw_Pcaps\\8202_tbd_ 6D2C12085F0018DAEB9C1A53E53FD4D1-pcap\\8202_tbd_ 6D2C12085F0018DAEB9C1A53E53FD4D1.pcap")
    # dicts = {}
    # for item in flow_list:
    #     dicts[item] = flow_list.count(item)
    #
    #
    # abspath = os.path.abspath('.')
    # t_name1 = pcap.split('\\')
    # path = abspath + '\\' + '4_Session_Pcaps'+ '\\' + t_name1[-2]
    # if not os.path.exists(path):
    #     os.mkdir(path)
    #
    # wrong_data = 0
    # count = 0
    # for key in dicts.keys():
    #     k = key.replace('.', '-')
    #     d = './4_Session_Pcaps'+ "/" + t_name1[-2]+ "/" + k + '.pcap'
    #     writer = PcapWriter(d, append=True)
    #     count += 1
    #     print(f"split progress:{100*count/ len(dicts)}%")
    #     for packet in packets:
    #         if packet.payload.name == 'IP':
    #             try:
    #                 five_tuple,five_tuple = packet_parse(packet)
    #                 if five_tuple == key:
    #                     writer.write(packet)
    #                     writer.flush()
    #             except AttributeError:
    #                 wrong_data = wrong_data + 1
    #                 print("AttributeError")
    #     writer.close()
    # return wrong_data
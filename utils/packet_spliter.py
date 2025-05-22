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
            #print(complete_tuple) #layer.name
            continue

        file_name = pcap.split('\\')
        sub_pcap_path = abspath + '\\' + '3_Session_Pcaps'+ '\\' + file_name[-2]
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
        sub_pcap_name = './3_Session_Pcaps' + "/" + file_name[-2] + "/" + five_tuple + '.pcap'
        writer = PcapWriter(sub_pcap_name, append=True)
        try:
            writer.write(packet)
            writer.flush()
        except AttributeError:
            wrong_data = wrong_data + 1
            print("AttributeError")
        writer.close()
    return wrong_data

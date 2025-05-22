# -*- coding: utf-8 -*-
import warnings
from scapy.all import *
from packet_parsing import packet_parse
from scapy.utils import PcapWriter

def packet_split(pcap):
    warnings.warn("some_old_function is deprecated", DeprecationWarning)
    packets = rdpcap(pcap)
    flow_list = []
    for packet in packets:
        five_tuple,complete_tuple = packet_parse(packet)
        if five_tuple == "not IP":
            print(complete_tuple) #layer.name
            continue
        flow_list.append(five_tuple)

    dicts = {}
    for item in flow_list:
        dicts[item] = flow_list.count(item)

    abspath = os.path.abspath('.')
    t_name1 = pcap.split('\\')
    path = abspath + '\\' + '4_Session_Pcaps'+ '\\' + t_name1[-2]
    if not os.path.exists(path):
        os.mkdir(path)

    wrong_data = 0
    count = 0
    for key in dicts.keys():
        k = key.replace('.', '-')
        d = './4_Session_Pcaps'+ "/" + t_name1[-2]+ "/" + k + '.pcap'
        writer = PcapWriter(d, append=True)
        count += 1
        print(f"split progress:{100*count/ len(dicts)}%")
        for packet in packets:
            if packet.payload.name in ["IP","IPv6"]:
                try:
                    five_tuple,five_tuple = packet_parse(packet)
                    if five_tuple == key:
                        writer.write(packet)
                        writer.flush()
                except AttributeError:
                    wrong_data = wrong_data + 1
                    print("AttributeError")
        writer.close()
    return wrong_data
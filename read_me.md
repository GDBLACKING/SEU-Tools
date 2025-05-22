SEU-Tool
Author:Song Wei
Email:<230258671@seu.edu.cn>

Introduction:
    This project is to provide a convenient network traffic batch processing tool.

Env-Needed: python, scapy, binascii
Suported protocol: IPv4-based protocol: DHCP IGMPv3 ICMP DNS TCP SSDP NBNS BROWSER and so on.


The project is suposed to be structured as follow:
    -1_Tools
    -2_Raw_Pcaps         put your raw pcaps here
    -3_Session_Pcaps   
    -4_Session_Csvs      
    -5_Session_PNGs     
    -Utils
    1-1_pcap2session.py
    2-1_session2csv.py
    3-1_session2png.py

Easily Use:
    1\ to convert Pcap files into sessions:
        run 1-1_pcap2session.py
    1\ to convert Pcap files into features:
        run 2-1_session2csv.py
    3\ to convert Pcap files into PNGs:
        run 3-1_session2png.py

Note:
    The Pcap files to be processed must be contained as the folling structure:
    -folders
        -files 
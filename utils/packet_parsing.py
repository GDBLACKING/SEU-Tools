
# -*- coding: utf-8 -*-
# 支持协议：ARP、DHCP、IGMPv3、ICMP、DNS、TCP、SSDP、NBNS、BROWSER
def packet_parse(data):

    flow_list = []
    src = ''
    sport = ''
    dst = ''
    deport = ''
    proto = ''
    timestamp = ''
    length = ''
    identification = ''
    flags = ''
    ttl = ''

    if data.payload.name not in ["IP"]:
        return "not IP",data.payload.name
    p_n = data.payload.name
    try:
        src = data["IP"].src if p_n=="IP" else data["IPv6"].src
    except AttributeError:
        src = -1
    try:
        dst = data["IP"].dst if p_n=="IP" else data["IPv6"].dst
    except AttributeError:
        dst = -1
    try:
        sport = data.sport
    except AttributeError:
        sport = -1
    try:
        deport = data.dport
    except AttributeError:
        deport = -1
    try:
        proto = data.proto if p_n=="IP" else -2
    except AttributeError:
        proto = -10
    try:
        timestamp = data["IP"].time if p_n=="IP" else data["IPv6"].time
    except AttributeError:
        timestamp = -1
    try:
        length = data.len
    except AttributeError:
        length = -1
    try:
        identification = data.id
    except AttributeError:
        identification = -1
    try:
        flags = data.flags
    except AttributeError:
        flags = -1
    try:
        frag = data.frag
    except AttributeError:
        frag = -1


    try:
        ttl = data["IP"].ttl if p_n=="IP" else data["IPv6"].ttl
    except AttributeError:
        ttl = -1
    table = {1:"ICMP",2:"IGMP",6:"TCP",17:"UDP",-2:"unknown"}
    five_tuple = "{}_{}_{}_{}_{}".format(table[proto], src, sport, dst, deport)
    complete_tuple = "{},{},{},{},{},{},{},{},{},{}".format(timestamp, src, dst, sport, deport, proto, length, identification, flags, ttl)
    return five_tuple,complete_tuple

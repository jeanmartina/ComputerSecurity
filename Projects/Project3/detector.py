from dpkt import ethernet, pcap, http

f = open('388-proj3.pcap')
pcap = pcap.Reader(f)

for ts, buf in pcap:
    eth = ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data

    if tcp.dport == 80 and len(tcp.data) > 0:
        http = http.Request(tcp.data)
        print http.uri

f.close()
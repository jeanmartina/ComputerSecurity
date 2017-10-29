from dpkt import pcap,ethernet,UnpackError,tcp,ip
from sys import argv

def parseIP(hexstring):
    attackip = []
    for i in range(0, len(hexstring), 2):
        attackip.append(str(int(hexstring[i:i + 2], 16)))
    print attackip[0] + '.' + attackip[1] + '.' + attackip[2] + '.' + attackip[3]

f=open(argv[1],"rb")
pcap = pcap.Reader(f)
dict = {}

for ts, buf in pcap:
    try:
        eth = ethernet.Ethernet(buf)
    except UnpackError:
        continue

    if eth.type != ethernet.ETH_TYPE_IP: continue
    ip = eth.data

    if ip.p == 6:
        packet = ip.data
        if packet.flags & tcp.TH_SYN != 0:
            if ip.src not in dict: dict[ip.src] = {'SYN': 0, 'SYN+ACK': 0}
            if ip.dst not in dict: dict[ip.dst] = {'SYN': 0, 'SYN+ACK': 0}

            if packet.flags & tcp.TH_ACK != 0:
                dict[ip.dst]['SYN+ACK'] += 1
            else:
                dict[ip.src]['SYN'] += 1

for item in dict.items():
    if item[1]['SYN'] > item[1]['SYN+ACK'] * 3:
        parseIP(str(item[0].encode('hex')))

f.close()
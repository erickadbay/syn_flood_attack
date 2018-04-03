from scapy.all import *
from time import sleep
from random import randint

import sys

if len(sys.argv) < 3:
    print("Please provide a target ip and interval and try again.")
    sys.exit()

target_ip = sys.argv[1]
interval = float(sys.argv[2])

for x in range(1,10):
    network_layer = IP(dst = target_ip)
    transport_layer = TCP(sport = randint(1025, 65535), dport=[80, 22], flags = "S")

    packet = network_layer/transport_layer

    print("Sending SYN segment to " + target_ip)
    send(packet, verbose = False)

    print("Done sending")
    sleep(interval)

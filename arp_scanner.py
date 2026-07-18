from scapy.all import *
from ipaddress import IPv4Network
import sys

if len(sys.argv) != 1:
	print(f"usage: python3 {sys.argv[0]}")
	sys.exit()

subnet_or_ip = input("enter the ip(192.168.0.8) OR subnet->include the '/' (10.0.0.0/24) :")

print("   IP                 MAC   ")
print("=========================================")

#amount of host found
total = 0

#all ip from the subnet
for ip in IPv4Network(subnet_or_ip):

	#create packet to send
	eth = Ether()
	arp = ARP(pdst=str(ip))
	packet = eth/arp

	#send packet
	result,unanswered = srp(packet,verbose=False,timeout=0.3)

	#report
	for sent,received in result:
		total +=1
		print(f"{total}. {received.psrc}   ---->   {received.hwsrc}")

print("finished")

# A MORE SIMPLE APPROACH
# INSTEAD OF MANUALLY SCANNING EACH IP, I CAN SCAN THE WHOLE SUBNET

#eth=Ether()
#arp=ARP(pdst="10.0.2.0/24")
#packet=eth/arp
#
#result,unanswered = srp(packet,verbose=False,timeout=3)
#
#for sent,received in result:
#	print(f"{received.psrc} -----> {received.hwsrc}")


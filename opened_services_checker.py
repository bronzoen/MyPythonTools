import sys
import socket
import subprocess

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <ip>")
    exit()

ip = sys.argv[1]

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}


for port, service in services.items():

	result = subprocess.run(
		["nc", "-z", ip, str(port)])

	if result.returncode == 0:
        	print(f"{service} ({port}) OPEN")
	else:
		print(f"{service} ({port}) CLOSED")

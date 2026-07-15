import sys
import subprocess
import time
from datetime import datetime

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

services_copy = services.copy()

for port, service in services_copy.items():
	answer = input(f"Scan {service}? (y/n):").lower()
	if answer == "n":
		services.pop(port)
	elif answer == "y":
		pass
	else:
		print("INPUT (y / n)!")
		sys.exit()
try:
	while True:
		warning = 0
		current = datetime.now()
		print("="*25,"\n",current.strftime("%Y-%m-%d,%H:%M:%S"),"\n")
		for port, service in services.items():
			result = subprocess.run(
				["nc", "-z", ip, str(port)])
			if result.returncode == 0:
        			pass
			else:
				print(f" *WARNING* {service} ({port}) CLOSED!")
				warning +=1
		if warning > 0:
			print(f"\nWARNINGS : {warning}x")
		else:
			print("Everything looks fine..")
		time.sleep(5)
except KeyboardInterrupt:
	sys.exit()

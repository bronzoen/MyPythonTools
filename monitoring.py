import sys
import subprocess
import time
from datetime import datetime

if len(sys.argv) >2 or len(sys.argv) <2:
	print("usage: python3 monitoring.py <ip>")
	sys.exit()

ip = sys.argv[1]
services = {"SSH":"22","FTP":"21","HTTP":"80","HTTPS":"443"}

for service in list(services.keys()):
	answer = input(f"MONITOR {service}? (y/n):").lower()
	if answer == 'n':
		services.pop(service)
	elif answer == 'y':
		pass
	else:
		print("(ENTER y/n)!")
		sys.exit()

try:
	while True:
		current = datetime.now()
		print("======================")
		print(current.strftime("%Y-%m-%d %H:%M:%S"))
		if subprocess.run(["ping","-c","1","-W","1",ip],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode == 0 :
			print(f"{ip} UP")
			for service,port in services.items():
				if subprocess.run(["nc","-z",ip,port],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode == 0:
					print(f"{service} UP")
				else:
					print(f"{service} DOWN")
		else:
			print(f"{ip} DOWN")
		time.sleep(5)
except KeyboardInterrupt:
	sys.exit()

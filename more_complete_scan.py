#This is for outputting ip status,services opened within a single file into a specified directory

import sys
import subprocess

if len(sys.argv) <3 or len(sys.argv) >3:
	print("usage: python3 more_complete_scan.py <ip> <directory>")
	sys.exit()

ip = sys.argv[1]
directory = sys.argv[2]

pinging = subprocess.run(["python3","/home/kali/PythonTools/python_ping.py",ip],capture_output=True,text=True)

ping_result = pinging.stdout

services = subprocess.run(["python3","/home/kali/PythonTools/opened_services_checker.py",ip],capture_output=True,text=True)

services_result = services.stdout

with open (f"/home/kali/ips_status/{ip}.txt","w") as file:
	file.write(f"HOST STATUS :\n {ping_result}\n")
with open (f"/home/kali/ips_status/{ip}.txt","a") as file:
	file.write(f"SERVICE STATUS :\n {services_result}\n")

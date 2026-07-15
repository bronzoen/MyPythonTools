import json
import subprocess
import sys

if len(sys.argv) != 2:
	print(f"usage: python3 {sys.argv[0]} <ip>")
	sys.exit()

ip = sys.argv[1]

result = subprocess.run(["nmap","-sV",ip],capture_output=True,text=True)

lines = result.stdout.splitlines()

services = {}

for line in lines:
	if "/tcp" in line:
		parts = line.split()
		port_location = parts[0].split("/")
		port = port_location[0]
		service = parts[2]
		services[port] = service
try:
	with open("ports.json","r") as file:
		previous = json.load(file)
except FileNotFoundError:
	previous = {}

with open("ports.json","w") as file:
	json.dump(services,file)

with open("ports.json","r") as file:
	now = json.load(file)

#NEW PORTS?
print("NEW PORTS\n==============")
for port in now:
	if port not in previous:
		print(f"Added : {port} {now[port]}")

print("==============\nREMOVED PORTS\n===============")
#REMOVED PORTS?
for port in previous:
	if port not in now:
		print(f"Removed : {port} {previous[port]}")


print("===============\nACTIVE PORTS\n--------------")
for port,service in now.items():
	print(f"{port} {service}")

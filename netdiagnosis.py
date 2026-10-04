import subprocess

#collect information

interface = None
state = None
gateway = "n/a"
ip_address = "n/a"
dns = "n/a"
gateway_status = "x"
dns_status = "x"
internet_status = "x"
latency = "n/a"
possible_problems = 0

#find the interface, state, ip, gateway
info1 = subprocess.run(["ip","route","get","8.8.8.8"],capture_output=True,text=True).stdout
parts1 = info1.split()

if "dev" in parts1:
	interface = parts1[parts1.index("dev")+1]

stateinfo = subprocess.run(["ip","link","show",interface],capture_output=True,text=True).stdout
stateparts = stateinfo.split()

if "state" in stateparts:
	if stateparts[stateparts.index("state")+1] == "DOWN":
		state = "down"
		possible_problems = 6
	elif stateparts[stateparts.index("state")+1] == "UP":
		state = "up"

		if "via" in parts1:
			gateway = parts1[parts1.index("via")+1]
		else:
			possible_problems += 1

		if "src" in parts1:
			ip_address = parts1[parts1.index("src")+1]
		else:
			possible_problems += 1

		#find dns
		info2 = subprocess.run(["nmcli","device","show"],capture_output=True,text=True).stdout
		parts2 = info2.splitlines()

		for line in parts2:
			if "IP4.DNS[1]" in line:
				line_parts = line.split()
				dns = line_parts[1]
		if dns == "n/a":
			possible_problems += 1

		#check gateway state
		gateway_state = subprocess.run(["ping", "-c", "4", gateway],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

		if gateway_state.returncode == 0:
			gateway_status = "✓"

		else:
			possible_problems += 1

		#test dns
		domain = "google.com" #the domain to test dns
		dns_state = subprocess.run(["dig","@"+dns,domain],capture_output=True,text=True).stdout
		dns_lines = dns_state.splitlines()

		for line in dns_lines:
			if "status" in line:
				dnsline_parts= line.split()
				if dnsline_parts[dnsline_parts.index("status:")+1] == "NOERROR,":
					dns_status = "✓"
		if dns_status == "x":
			possible_problems += 1

		#internet status
		internet_test = subprocess.run(["ping","-c","4","8.8.8.8"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		if internet_test.returncode == 0:
			internet_status = "✓"
		else:
			possible_problems += 1

		#check latency
		internet_test = subprocess.run(["ping","-c","4","8.8.8.8"],capture_output=True,text=True).stdout
		internet_lines = internet_test.splitlines()
		latency = internet_lines[1].split("time=")[1].split(" ")[0]



# THE OUTPUT

print("\n   NETWORK DIAGNOSTIC\n\n-------------------------")
print(f"\nInterface = {interface}")
print(f"Status = {state.upper()}")
print(f"Gateway = {gateway}")
print(f"IP = {ip_address}")
print(f"DNS = {dns}\n")
print(f"Gateway Test = {gateway_status}")
print(f"Internet Test = {internet_status}")
print(f"DNS Test = {dns_status}")
print(f"Latency = {latency} ms\n")
print(f"possible_problems : {possible_problems}")
if possible_problems == 0:
	print("None Detected")

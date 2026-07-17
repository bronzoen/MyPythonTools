import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#i could also add a dict variable from json file and make it loop through the dict to scan more servers/machines but i dont wanna post my ssh logins on github :) (even tho i could make
#it in .gitignore or make ssh keys im too lazy)

ip ="192.168.1.2"

#for this project im only making it work neat for 1 minute to i gues 23:59 hours, anything after that will result in 1 day uptime outputted as 1 M (just not in the mood to fix)

try:
	client.connect(ip,port=22,username="xubuntu",password="xubuntu")
	stdin, stdout, stderr = client.exec_command('uptime')
	output = stdout.read().decode().split()
	if ":" in output[2]:
		timee = output[2].split(",")
		print(f"{ip} --> UPTIME : {timee[0]} H")
	else:
		print(f"{ip} --> UPTIME : {output[2]} M")
except Exception as e:
	print(f"{ip} --> ERROR : {e}")
finally:
	client.close()

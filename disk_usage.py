import subprocess
import sys

if len(sys.argv) != 1:
	print(f"usage: python3 {sys.argv[0]}")
	sys.exit()

result = subprocess.run(["df","-h","-B1"],capture_output=True,text=True)

lines = result.stdout.splitlines()

#only check what
check = ["/","/dev","/dev/shm","/tmp","/run"]

#ask in what size it should display
sizetype = ""
size = 0

while True:
	userinput = input("Display in size (GB/MB)? :").upper()
	if userinput == "GB":
		sizetype = "GB"
		size = 1024*1024*1024
		break
	elif userinput == "MB":
		sizetype = "MB"
		size = 1024*1024
		break
	else:
		print("Input Only 'GB' or 'MB'!")

#REPORT

totalusage = 0

print("="*20)
print(" DISK SPACE REPORT ")
print("="*20)

for line in lines:
	parts = line.split()
	for partition in check:
		if parts[5] == partition:
			total = float(parts[1]) / size
			used = float(parts[2]) / size
			available = float(parts[3]) / size
			try:
				usage = (used / total) * 100
				totalusage += usage
			except ZeroDivisionError:
				usage = 0

			print(f"*** Partition : {partition} ***")
			print(f"Total Size : {total:.2f}{sizetype}")
			print(f"Used : {used:.2f}{sizetype}")
			print(f"Available : {available:.2f}{sizetype}")
			print(f"Usage : {usage:.2f}%")
			if usage <50:
				print("Status : OK\n")
			elif usage >=50 and usage <=70:
				print("Status : WARNING\n")
			elif usage >70:
				print("Status : CRITICAL\n")

print(f"TOTAL USAGE : {totalusage:.2f}%")

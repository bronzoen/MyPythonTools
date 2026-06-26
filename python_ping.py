import subprocess
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <ip>")
    exit()

ip = sys.argv[1]

result = subprocess.run(["ping", "-c", "4", ip])

if result.returncode == 0:
    print(f"{ip} is UP")
else:
    print(f"{ip} is DOWN")

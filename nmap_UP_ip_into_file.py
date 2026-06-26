import os
import sys

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} <subnet> <output_file>")
    exit()

subnet = sys.argv[1]
output_file = sys.argv[2]

command = f"nmap -sn {subnet} | grep 'Nmap scan report' | awk '{{print $5}}' > {output_file}"

os.system(command)

print(f"Live IPs saved to {output_file}")

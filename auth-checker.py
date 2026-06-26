import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <file>")
    exit()

filename = sys.argv[1]

with open(filename, "r") as file:
    lines = file.readlines()

print("Checking Authentication Methods\n")

for line in lines:
    line = line.strip()

    if line == "":
        continue

    if "password" in line.lower():
        print(f"[PASSWORD] {line}")

    elif "publickey" in line.lower():
        print(f"[PUBLIC KEY] {line}")

    elif "anonymous" in line.lower():
        print(f"[ANONYMOUS] {line}")

    else:
        print(f"[UNKNOWN] {line}")

import subprocess

ip = input("INPUT THE IP ADDRESS OR SUBNET: ")

filters = []

questions = [
    ("sV", "Version Detection"),
    ("O", "OS Detection"),
    ("Pn", "Skip Host Discovery"),
    ("T4", "Faster Scan")
]

for flag, description in questions:
    answer = input(f"Use -{flag} ({description})? (y/n): ").lower()

    if answer == "y":
        filters.append(f"-{flag}")

command = ["nmap"] + filters + [ip]

print("\nRunning:")
print(" ".join(command))
print()

subprocess.run(command)

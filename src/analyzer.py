import re

# Load suspicious IP list
with open("data/suspicious_ips.txt", "r") as f:
    suspicious_ips = set(line.strip() for line in f)

failed_logins = {}
alerts = []

with open("logs/auth.log", "r") as log:
    for line in log:
        # Extract IP
        match = re.search(r"from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)
        ip = match.group(1) if match else None

        # 1. Failed login detection
        if "Failed password" in line:
            failed_logins[ip] = failed_logins.get(ip, 0) + 1
            
            if failed_logins[ip] >= 3:
                alerts.append(f"[ALERT] Possible brute force from {ip} ({failed_logins[ip]} failures)")

        # 2. Suspicious IP match
        if ip in suspicious_ips:
            alerts.append(f"[ALERT] Suspicious IP detected: {ip}")

        # 3. Root login detection
        if "root" in line and ("Accepted password" in line or "sudo:" in line):
            alerts.append("[ALERT] Root access detected in log")

# Print results
print("\n--- ALERTS GENERATED ---")
if alerts:
    for a in set(alerts):
        print(a)
else:
    print("No alerts detected.")


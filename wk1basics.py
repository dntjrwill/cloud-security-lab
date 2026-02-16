#week 1 - Baisc Log Parser 
# 
# This is:

#Log parsing

##Pattern matching

#Data extraction

log_file="sample.log"
error_ips = []
with open(log_file, "r") as file:
    lines = file.readlines()

error_count = 0

for line in lines: 
    if "ERROR" in line:
        error_count += 1
    if "from" in line:
        ip_address = line.split("from")[-1].strip()
        error_ips.append(ip_address)

print(f"Total number of errors: {error_count}")
print(f"IP addresses found: {error_ips}")
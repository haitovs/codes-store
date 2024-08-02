import json
import ipaddress

# Define the path to the input and output files
input_file = 'subnets.txt'
output_file = 'ip_addresses.json'

# Read the content of the input file
with open(input_file, 'r') as file:
    subnets = file.read().splitlines()

# Generate the dictionary of IP addresses
ip_dict = {}
for subnet in subnets:
    try:
        network = ipaddress.ip_network(subnet.strip())
        ip_list = [str(ip) for ip in network.hosts()]  # .hosts() method skips network and broadcast addresses
        ip_dict[subnet] = ip_list
    except ValueError:
        print(f"Invalid subnet: {subnet}")

# Create the JSON structure
data = {
    "ips": ip_dict
}

# Write the JSON structure to the output file
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"IP addresses have been written to {output_file}")

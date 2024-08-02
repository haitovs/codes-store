import re
import ipaddress

# Define the path to the input and output files
input_file = 'raw_text.txt'
output_file = 'raw_text_output.txt'

def divide_subnet(subnet):
    network = ipaddress.ip_network(subnet)
    if network.prefixlen < 20:
        subnets = list(network.subnets(new_prefix=20))
        return subnets
    else:
        return [network]

# Read the content of the input file
with open(input_file, 'r') as file:
    text = file.read()

# Use a regular expression to find all IP addresses with subnets
subnets = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b', text)

# Convert and write the extracted subnets to the output file
with open(output_file, 'w') as file:
    for subnet in subnets:
        divided_subnets = divide_subnet(subnet)
        for ds in divided_subnets:
            file.write(str(ds) + '\n')

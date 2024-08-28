import subprocess
import re
import argparse
from concurrent.futures import ThreadPoolExecutor
import ipaddress

# Function to divide subnets if necessary
def divide_subnet(subnet):
    network = ipaddress.ip_network(subnet)
    if network.prefixlen < 20:
        subnets = list(network.subnets(new_prefix=20))
        return subnets
    else:
        return [network]

# Function to run nmap based on intensity
def run_nmap(target, intensity):
    command = [
        "nmap",
        "-PN",
        intensity,
        "-p",
        "443",
        "--min-parallelism",
        "100",
        "--min-hostgroup",
        "64",
        "-n",
        "--max-retries",
        "1",
        "--max-rate",
        "800",
        target,
    ]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap for {target}: {e}")
        return ""

def extract_open_ports(nmap_output):
    open_ports_info = []
    combined_pattern = re.compile(r"Nmap scan report for (\S+)|(\d+/tcp)\s+open")

    current_ip = None
    for line in nmap_output.splitlines():
        match = combined_pattern.search(line)
        if match:
            if match.group(1):
                current_ip = match.group(1)
            elif current_ip and match.group(2):
                port = match.group(2).split("/")[0]
                open_ports_info.append(f"{current_ip}: {port}")

    return open_ports_info

def scan_and_extract(target, intensity):
    target = target.strip()
    if target:
        print(f"Running nmap for target: {target} with intensity {intensity}")
        nmap_output = run_nmap(target, intensity)
        return extract_open_ports(nmap_output), target
    return [], target

def main():
    intensity_map = {"T3": "-T3", "T4": "-T4", "T5": "-T5"}

    parser = argparse.ArgumentParser(description="Nmap scanning with different intensities")
    parser.add_argument("--T3", action="store_true", help="Use slowest scan intensity")
    parser.add_argument("--T4", action="store_true", help="Use medium scan intensity")
    parser.add_argument("--T5", action="store_true", help="Use fastest scan intensity")
    args = parser.parse_args()

    intensity = intensity_map.get("T3" if args.T3 else "T4" if args.T4 else "T5", "-T5")

    # Read the content of the input file and filter IPs/subnets
    with open("target.txt", "r") as file:
        text = file.read()

    # Find all IP addresses with subnets
    subnets = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b', text)

    # Prepare targets list
    targets = []
    for subnet in subnets:
        divided_subnets = divide_subnet(subnet)
        for ds in divided_subnets:
            targets.append(str(ds))

    # Clear the results file before starting the scan
    with open("output.txt", "w"):
        pass

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda target: scan_and_extract(target, intensity), targets)

        with open("output.txt", "a") as results_file:
            for open_ports_info, target in results:
                if open_ports_info:
                    results_file.write("\n".join(open_ports_info) + "\n")
                else:
                    results_file.write(f"Results for {target} - No open ports found.\n")
                print(f"Finished nmap for target: {target}")

if __name__ == "__main__":
    main()

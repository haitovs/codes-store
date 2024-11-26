import subprocess
import re
import argparse
from concurrent.futures import ThreadPoolExecutor
import ipaddress
import os
import multiprocessing


# Function to divide subnets if necessary
def divide_subnet(subnet):
    network = ipaddress.ip_network(subnet)
    if network.prefixlen < 30:
        subnets = list(network.subnets(new_prefix=20))
        return subnets
    else:
        return [network]


# Function to run Nmap based on intensity
def run_nmap(target, ports, verbose):
    command = [
        "nmap",
        "-PN",
        "-T5",  # Fastest scan intensity
        "-p",
        ports,
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
    if verbose:
        print(f"Executing: {' '.join(command)}")
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


def scan_and_extract(target, ports, verbose):
    target = target.strip()
    if target:
        print(f"Running Nmap for target: {target}")
        nmap_output = run_nmap(target, ports, verbose)
        return extract_open_ports(nmap_output), target
    return [], target


def main():
    parser = argparse.ArgumentParser(description="Nmap scanning with T5 intensity")
    parser.add_argument(
        "--input",
        type=str,
        default="target.txt",
        help="Input file containing target IPs or subnets",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.txt",
        help="Output file to save results",
    )
    parser.add_argument(
        "--ports",
        type=str,
        default="443",
        help="Comma-separated ports to scan (default: 443)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging for debugging",
    )
    args = parser.parse_args()

    # Read the content of the input file and filter IPs/subnets
    if not os.path.exists(args.input):
        print(f"Input file '{args.input}' not found.")
        return

    with open(args.input, "r") as file:
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
    with open(args.output, "w"):
        pass

    # Use dynamic worker count based on CPU cores
    max_workers = min(32, multiprocessing.cpu_count() * 2)

    print(f"Starting scans with {max_workers} threads. Results will be saved in '{args.output}'.")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(lambda target: scan_and_extract(target, args.ports, args.verbose), targets)

        with open(args.output, "a") as results_file:
            for open_ports_info, target in results:
                if open_ports_info:
                    results_file.write("\n".join(open_ports_info) + "\n")
                print(f"Finished Nmap for target: {target}")


if __name__ == "__main__":
    main()

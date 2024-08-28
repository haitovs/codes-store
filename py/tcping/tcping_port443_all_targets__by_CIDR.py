import subprocess
import re
import argparse
from concurrent.futures import ThreadPoolExecutor

# Function to run nmap based on intensity
def run_nmap(target, intensity):
    # Add "sudo" before "nmap" if needed for scanning
    command = [
        # "sudo", 
        "nmap", "-PN", intensity, "-p", "443", 
        "--min-parallelism", "100", "--min-hostgroup", "64", 
        "-n", "--max-retries", "1", "--max-rate", "800", target
    ]
    with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
        return process.communicate()[0]

def extract_open_ports(nmap_output):
    open_ports_info = []
    # Combined regex pattern to find IPs and open ports in a single pass
    combined_pattern = re.compile(r"Nmap scan report for (\S+)|(\d+/tcp)\s+open")
    
    current_ip = None
    for line in nmap_output.splitlines():
        match = combined_pattern.search(line)
        if match:
            if match.group(1):  # IP address found
                current_ip = match.group(1)
            elif current_ip and match.group(2):  # Open port found
                port = match.group(2).split('/')[0]
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
    # Define available intensities
    intensity_map = {
        'T3': '-T3',  # Slowest
        'T4': '-T4',  # Medium
        'T5': '-T5'   # Fastest
    }
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Nmap scanning with different intensities")
    parser.add_argument("--T3", action="store_true", help="Use slowest scan intensity")
    parser.add_argument("--T4", action="store_true", help="Use medium scan intensity")
    parser.add_argument("--T5", action="store_true", help="Use fastest scan intensity")
    args = parser.parse_args()

    # Determine scan intensity
    if args.T3:
        intensity = intensity_map['T3']
    elif args.T4:
        intensity = intensity_map['T4']
    else:
        intensity = intensity_map['T5']  # Default to fastest if none specified

    with open("targets.txt", "r") as targets_file, open("results.txt", "a") as results_file:
        targets = targets_file.readlines()
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(lambda target: scan_and_extract(target, intensity), targets)
            
            for open_ports_info, target in results:
                if open_ports_info:
                    for info in open_ports_info:
                        results_file.write(f"{info}\n")
                else:
                    results_file.write(f"Results for {target} - No open ports found.\n")
                print(f"Finished nmap for target: {target}")

if __name__ == "__main__":
    main()

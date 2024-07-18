import subprocess
import re

def run_nmap(target):
    # Add "sudo" before "nmap" to scan on linux
    command = [
        # "sudo"
        "nmap", "-PN", "-T5", "-p", "443", 
        "--min-parallelism", "100", "--min-hostgroup", "32", 
        "-n", "--max-retries", "1", "--max-rate", "400", target
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def extract_open_ports(nmap_output):
    open_ports_info = []
    # Regex pattern to find IPs and corresponding open ports
    ip_pattern = re.compile(r"Nmap scan report for (\S+)")
    open_port_pattern = re.compile(r"(\d+/tcp)\s+open")
    
    lines = nmap_output.split("\n")
    current_ip = None

    for line in lines:
        ip_match = ip_pattern.search(line)
        if ip_match:
            current_ip = ip_match.group(1)
        if current_ip:
            port_match = open_port_pattern.search(line)
            if port_match:
                port = port_match.group(1).split('/')[0]
                open_ports_info.append(f"{current_ip}: {port}")

    return open_ports_info

def main():
    with open("targets.txt", "r") as targets_file:
        targets = targets_file.readlines()
    
    for target in targets:
        target = target.strip()
        if target:
            print(f"Running nmap for target: {target}")
            nmap_output = run_nmap(target)
            open_ports_info = extract_open_ports(nmap_output)
            with open("results.txt", "a") as results_file:
                if open_ports_info:
                    for info in open_ports_info:
                        results_file.write(f"{info}\n")
                else:
                    results_file.write(f"Results for {target} - No open ports found.\n")
            print(f"Finished nmap for target: {target}")

if __name__ == "__main__":
    main()

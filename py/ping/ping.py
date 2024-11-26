# File: connectivity_checker.py
import ipaddress
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from ping3 import ping

# File paths
REACHABLE_IPS_FILE = "reachable_ips.txt"


def fast_ping(ip, timeout=0.5):
    """
    Perform an ICMP ping to test if an IP is reachable.
    Returns the latency in milliseconds or -1 if unreachable.
    """
    try:
        latency = ping(ip, timeout=timeout, unit='ms')
        if latency is not None:
            return round(latency, 2)
    except Exception as e:
        print(f"Ping error for {ip}: {e}")
    return -1


def process_cidr(cidr):
    """
    Generate a list of all IPs from a given CIDR range.
    """
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        print(f"Invalid CIDR range: {e}")
        return []


def load_file(file_path):
    """
    Load a list of IPs or other data from a file.
    """
    if Path(file_path).is_file():
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def write_to_file(lines, file_path):
    """
    Write a list of strings to a file, one per line.
    """
    with open(file_path, "w") as file:
        file.writelines(line + "\n" for line in lines)


def run_fast_ping(input_data, timeout=0.5, max_workers=50):
    """
    Perform ICMP ping for a CIDR range or a list of IPs from a file using concurrent workers.
    """
    if Path(input_data).is_file():
        ips = load_file(input_data)
    else:
        ips = process_cidr(input_data)

    reachable_ips = []
    total_ips = len(ips)

    print(f"Starting ping test for {total_ips} IPs with {max_workers} workers...")

    # Use ThreadPoolExecutor for concurrency
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_ip = {executor.submit(fast_ping, ip, timeout): ip for ip in ips}
        for idx, future in enumerate(as_completed(future_to_ip), start=1):
            ip = future_to_ip[future]
            try:
                latency = future.result()
                if latency != -1:
                    reachable_ips.append(ip)
            except Exception as e:
                print(f"Error pinging {ip}: {e}")

            # Log progress every 50 IPs or at the end
            if idx % 50 == 0 or idx == total_ips:
                print(f"Processed {idx}/{total_ips} IPs... Reachable so far: {len(reachable_ips)}")

    write_to_file(reachable_ips, REACHABLE_IPS_FILE)
    print(f"Ping test completed. Reachable IPs stored in {REACHABLE_IPS_FILE}")


def main():
    data_source = input("Enter CIDR range or file path for IPs: ")
    ping_timeout = float(input("Enter ICMP ping timeout in seconds (e.g., 0.5): "))
    max_workers = int(input("Enter number of workers (e.g., 50): "))
    run_fast_ping(data_source, timeout=ping_timeout, max_workers=max_workers)


if __name__ == "__main__":
    main()

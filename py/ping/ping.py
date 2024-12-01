import ipaddress
import asyncio
import argparse
import time
from multiprocessing import Process, Queue, cpu_count
from ping3 import ping as icmp_ping_lib
from functools import partial

# Function to parse IP ranges and CIDR blocks
def parse_ip_range(ip_range_str):
    ip_list = []
    if '/' in ip_range_str:
        # CIDR notation
        network = ipaddress.ip_network(ip_range_str, strict=False)
        ip_list.extend([str(ip) for ip in network.hosts()])
    elif '-' in ip_range_str:
        # IP range notation
        start_ip_str, end_ip_str = ip_range_str.split('-')
        start_ip = ipaddress.IPv4Address(start_ip_str.strip())
        end_ip = ipaddress.IPv4Address(end_ip_str.strip())
        ip_list.extend([str(ipaddress.IPv4Address(ip)) for ip in range(int(start_ip), int(end_ip) + 1)])
    else:
        # Single IP
        ip_list.append(ip_range_str.strip())
    return ip_list

# Function to parse multiple IP ranges or CIDRs
def parse_multiple_ip_ranges(ip_ranges_list):
    ip_set = set()
    for ip_range_str in ip_ranges_list:
        ip_list = parse_ip_range(ip_range_str)
        ip_set.update(ip_list)
    return ip_set

# Asynchronous ICMP ping function
async def icmp_ping(ip, timeout, count):
    loop = asyncio.get_event_loop()
    latencies = []
    tasks = []

    # Run pings concurrently for the same IP to speed up
    for _ in range(count):
        tasks.append(loop.run_in_executor(None, partial(icmp_ping_lib, ip, timeout=timeout, unit='ms')))

    results = await asyncio.gather(*tasks)

    for latency in results:
        if latency is not None:
            latencies.append(latency)

    if latencies:
        average_latency = sum(latencies) / len(latencies)
        return ip, average_latency
    else:
        return ip, None

# Worker function for each process
def worker(ip_list, timeout, result_queue, concurrency_limit, count):
    async def run():
        sem = asyncio.Semaphore(concurrency_limit)  # Limit concurrency per process
        tasks = []

        async def sem_icmp_ping(ip):
            async with sem:
                return await icmp_ping(ip, timeout, count)

        for ip in ip_list:
            tasks.append(sem_icmp_ping(ip))

        results = await asyncio.gather(*tasks)
        for result in results:
            result_queue.put(result)

    asyncio.run(run())

# Main function
def main():
    parser = argparse.ArgumentParser(description="Optimized ICMP Pinger")
    parser.add_argument('ip_range', help='IP range in CIDR (e.g., 192.168.1.0/24) or range (e.g., 192.168.1.1-192.168.1.254)')
    parser.add_argument('-t', '--timeout', type=float, default=0.5, help='Timeout in seconds (default: 1.0)')
    parser.add_argument('-o', '--output', type=str, default='results.txt', help='Output file name (default: results.txt)')
    parser.add_argument('-c', '--concurrency', type=int, default=300, help='Concurrency limit per process (default: 200)')
    parser.add_argument('-r', '--retries', type=int, default=2, help='Number of ping attempts per host (default: 2)')
    parser.add_argument('-e', '--exclude', action='append', help='IP ranges or CIDRs to exclude (can be used multiple times)')
    args = parser.parse_args()

    # Parse the main IP range
    ip_set = set(parse_ip_range(args.ip_range))

    # Parse exclusions if any
    if args.exclude:
        exclude_set = parse_multiple_ip_ranges(args.exclude)
        # Exclude the IPs
        ip_set -= exclude_set

    ip_list = list(ip_set)
    total_ips = len(ip_list)
    print(f"Total IPs to ping after exclusions: {total_ips}")

    if total_ips == 0:
        print("No IPs to ping after applying exclusions.")
        return

    num_processes = min(cpu_count(), len(ip_list))  # Avoid creating unnecessary processes
    chunk_size = (total_ips + num_processes - 1) // num_processes
    processes = []
    result_queue = Queue()

    # Split IP list among processes
    for i in range(num_processes):
        chunk = ip_list[i * chunk_size:(i + 1) * chunk_size]
        if not chunk:
            continue
        p = Process(target=worker, args=(chunk, args.timeout, result_queue, args.concurrency, args.retries))
        processes.append(p)
        p.start()

    # Collect results
    results = {}
    finished_processes = 0
    while finished_processes < len(processes):
        try:
            ip, latency = result_queue.get(timeout=1)
            results[ip] = latency
        except Exception:
            pass  # Timeout waiting for results
        # Check if processes are still alive
        finished_processes = sum(1 for p in processes if not p.is_alive())

    for p in processes:
        p.join()

    # Prepare lists of reachable IPs with latencies
    reachable_ips = [(ip, latency) for ip, latency in results.items() if latency is not None]

    # Write results to file
    with open(args.output, 'w') as f:
        # Write unordered list
        for ip, latency in reachable_ips:
            f.write(f"{ip}  {latency:.2f}ms\n")

        # Write two blank lines
        f.write("\n\n")

        # Write ordered list sorted by latency
        for ip, latency in sorted(reachable_ips, key=lambda x: x[1]):
            f.write(f"{ip}  {latency:.2f}ms\n")

    print(f"Results saved to {args.output}")

if __name__ == '__main__':
    main()

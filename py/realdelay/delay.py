import os
import json
import subprocess
import time
import threading
import requests

# Path to the V2Ray core executable
V2RAY_PATH = 'v2ray'  # or 'v2ray.exe' / 'xray' / 'xray.exe'

# Base configuration file
BASE_CONFIG_FILE = 'base_config.json'

# Temporary configuration file
TEMP_CONFIG_FILE = 'temp_config.json'

# List of IPs to test
IPS_TO_TEST = [
    '151.101.210.1',
    '151.101.210.2',
    # Add more IPs as needed
]

# Target URL to test latency (you can choose any reliable site)
TEST_URL = 'https://www.google.com/'

# Proxy settings
PROXY = {
    'http': 'socks5h://127.0.0.1:1080',
    'https': 'socks5h://127.0.0.1:1080',
}

def start_v2ray(config_path):
    """Start V2Ray with the specified configuration."""
    process = subprocess.Popen([V2RAY_PATH, '-config', config_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def stop_v2ray(process):
    """Stop the V2Ray process."""
    process.terminate()
    process.wait()

def measure_latency():
    """Measure latency by sending a request through the proxy."""
    start_time = time.time()
    try:
        response = requests.get(TEST_URL, proxies=PROXY, timeout=5)
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        return latency
    except requests.exceptions.RequestException:
        return None

def test_ip(ip_address, base_config):
    """Test latency for a single IP address."""
    # Update the configuration with the new IP
    base_config['outbounds'][0]['settings']['vnext'][0]['address'] = ip_address

    # Write the temporary configuration
    with open(TEMP_CONFIG_FILE, 'w') as f:
        json.dump(base_config, f)

    # Start V2Ray
    process = start_v2ray(TEMP_CONFIG_FILE)

    # Allow time for V2Ray to start
    time.sleep(2)

    # Measure latency
    latency = measure_latency()

    # Stop V2Ray
    stop_v2ray(process)

    # Clean up
    os.remove(TEMP_CONFIG_FILE)

    return latency

def main():
    # Load the base configuration
    with open(BASE_CONFIG_FILE, 'r') as f:
        base_config = json.load(f)

    # Iterate over the IPs
    for ip in IPS_TO_TEST:
        latency = test_ip(ip, base_config.copy())
        if latency is not None:
            print(f"IP: {ip} - Latency: {latency:.2f} ms")
        else:
            print(f"IP: {ip} - Connection failed or timed out")

if __name__ == '__main__':
    main()

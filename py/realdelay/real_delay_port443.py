from turtle import delay
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import socket
import ssl
import time


class VlessConfig:
    def __init__(
        self,
        user_id,
        address,
        port,
        type="ws",
        security="tls",
        encryption="none",
        host="",
        alpn="http/1.1",
        path="/",
        sni="",
        fp="chrome",
        tag="VLESS Server",
    ):
        self.user_id = user_id
        self.address = address
        self.port = port
        self.type = type
        self.security = security
        self.encryption = encryption
        self.host = host
        self.alpn = alpn
        self.path = path
        self.sni = sni
        self.fp = fp
        self.tag = tag

    @classmethod
    def from_uri(cls, vless_uri):
        """
        Create a VlessConfig object from a VLESS URI.
        """
        parsed_uri = urlparse(vless_uri)
        user_id = parsed_uri.username
        address = parsed_uri.hostname
        port = parsed_uri.port

        # Extract query parameters
        query_params = parse_qs(parsed_uri.query)

        return cls(
            user_id=user_id,
            address=address,
            port=port,
            type=query_params.get("type", ["ws"])[0],
            security=query_params.get("security", ["tls"])[0],
            encryption=query_params.get("encryption", ["none"])[0],
            host=query_params.get("host", [""])[0],
            alpn=query_params.get("alpn", ["http/1.1"])[0],
            path=query_params.get("path", ["/"])[0],
            sni=query_params.get("sni", [""])[0],
            fp=query_params.get("fp", ["chrome"])[0],
            tag=parsed_uri.fragment,
        )

    def to_uri(self):
        """
        Convert a VlessConfig object back to a VLESS URI.
        """
        query_params = {
            "type": self.type,
            "security": self.security,
            "encryption": self.encryption,
            "host": self.host,
            "alpn": self.alpn,
            "path": self.path,
            "sni": self.sni,
            "fp": self.fp,
        }

        query_string = urlencode(query_params)
        vless_uri = f"vless://{self.user_id}@{self.address}:{self.port}?{query_string}#{self.tag}"
        return vless_uri

    def real_delay(self, retries=2):
        """
        Measure the real delay (round-trip time) to the VLESS server with retry logic.
        Disables SSL certificate verification.
        """
        attempt = 0
        while attempt < retries:
            try:
                # Create an SSL context without certificate verification
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE

                # Measure connection delay
                start_time = time.time()

                # Connect to the VLESS server
                try:
                    # Debugging the connection process
                    print(f"Attempting to connect to {self.address}:{self.port}")
                    with socket.create_connection(
                        (self.address, self.port), timeout=10
                    ) as sock:
                        print("Socket connection established.")
                        with context.wrap_socket(
                            sock, server_hostname=self.address
                        ) as ssl_sock:
                            print("SSL connection established.")
                except Exception as e:
                    print(f"Connection error: {str(e)}")

                # Calculate round-trip time
                round_trip_time = time.time() - start_time
                print(f"Real delay: {round_trip_time:.3f} seconds")

                return round_trip_time

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                attempt += 1
                time.sleep(2)  # Wait 2 seconds before retrying

        # If all retries fail, return None
        print("All retry attempts failed.")
        return None


vless_uri = "vless://9ce79333-df40-4f1e-9bc6-b7525089b54b@151.101.163.2:443?path=%2F%3Fed%3D2048&security=tls&encryption=none&alpn=http/1.1&host=dom.spikeservice.top&fp=chrome&type=ws&sni=google.com#Server+%234+DE+3G%2F4G"

# Create a VlessConfig object from the URI
vless_config = VlessConfig.from_uri(vless_uri)

# Print the URI
print("JSON VLESS URI:")
print(vless_config)
print("Original VLESS URI:")
print(vless_config.to_uri())

# Measure the real delay
delay = vless_config.real_delay()

# Check if delay is a valid number
if isinstance(delay, (float, int)):
    print(f"Measured delay: {delay:.3f} seconds")
else:
    print("Failed to measure delay or delay is not a valid number.")

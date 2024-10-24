import socket
import threading
import time
import queue

# Define target host and port range
target_host = "example.com"
start_port = 1
end_port = 1024

# Create a queue to store discovered ports
port_queue = queue.Queue()

# Define a function to scan for open ports
def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            port_queue.put(port)
        sock.close()

# Define a function to perform port scanning in a separate thread
def scan_thread():
    scan_ports(target_host, start_port, end_port)

# Define a function to perform vulnerability scanning on discovered ports
def scan_vulnerabilities(port):
    # Perform vulnerability scanning logic based on the port
    # For example, check for known vulnerabilities related to the service running on the port
    print(f"Scanning vulnerabilities on port {port}")
    # Add your vulnerability scanning logic here

# Create a thread to perform port scanning
scan_thread = threading.Thread(target=scan_thread)
scan_thread.start()

# Wait for the scanning thread to complete
while scan_thread.is_alive():
    time.sleep(1)

# Process the discovered ports and perform vulnerability scanning
while not port_queue.empty():
    port = port_queue.get()
    scan_vulnerabilities(port)

print("Pentesting completed.")
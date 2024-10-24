Here's a Python script that demonstrates a basic penetration testing project for educational purposes.
This script defines a target host and port range. It uses a separate thread to perform port scanning using the scan_thread function. 
The scan_ports function iterates over the specified range of ports and stores the discovered open ports in a queue.
After the scanning thread completes, the script processes the discovered ports from the queue and performs vulnerability scanning on each port using the scan_vulnerabilities function. 
You can add your own vulnerability scanning logic based on the discovered ports.
Please note that this script is for educational purposes and should only be used with permission and on systems you own or have explicit authorization to test. 
Performing penetration testing without proper authorization is illegal and unethical.



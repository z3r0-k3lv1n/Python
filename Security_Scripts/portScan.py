# This is a port scanner written and explained by the Infosec YouTube Channel https://youtu.be/t9EX2RAUoTU

import socket
import subprocess
import sys
from datetime import datetime

# Blank out your screen.
subprocess.call('clear', shell=True)

# Ask for input.
remoteServer = input("Enter the address of a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan.
print("_" * 60)
print("Please wait, we are scanning remote host ", remoteServerIP)
print("_" * 60)

# Check the date and time the scan was started.
t1 = datetime.now()

# Using the range function specify the port range to scan.
# We will also add error handling

try:
    for port in range(1, 5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:     Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting...")
    sys.exit()

except socket.error:
    print("Couldn't connect to server. Exiting...")
    sys.exit()

# Check the time again.
t2 = datetime.now()

# Calculate the difference in time to know how long the scan took
total = t2 - t1

# Printing the information on the screen
print("Scanning completed in: ", total)

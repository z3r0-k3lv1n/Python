#!/bin/bash
# A port scanner based on ITPro TVs Python for Security course with a few adjustments

import socket
import threading
import os

from tqdm import tqdm
from utils import timefunc
from datetime import datetime


class Scanner:
    def __init__(self, ip):
        """
        Initialise the Scanner object with the specified IP address and an empty list
        to store the open ports discovered during scanning
        :param ip: This is the target IP address to scan for open ports.
        """
        self.ip = ip
        self.open_ports = []; # Creates a list called open ports. This will have the port numbers that are open
        # added to this list.
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


    def __repr__(self):
        """
        Return a string representaiton of the scanner object.

        :return: String representation in the format "Scanner: <ip">
        """
        return f'Scanner: {self.ip}'

    def add_port(self, port):
        """
        Add an open port to the list of open ports.

        :param port: The open port number to be added to the list.
        """
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        """
        Scan a range of ports on the target IP address to check for open ports.
        :param lowerport: The lower bound of the port range to scan.
        :param upperport: The upper bound of the port range to scan.
        """
        # Initialise the progress bar

        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    def threaded_scan(self, num_threads, total_ports):
        """
        Perform threaded scanning by splitting the port range among threads.

        :param num_threads: Number of threads to use for scanning.
        :param total_ports: Total number of ports to scan.
        """
        progress = tqdm(total=total_ports, desc="Scanning Ports")  # Shared progress bar

        lock = threading.Lock()  # Create a lock to synchronize progress bar updates

        def scan_range(lowerport, upperport):
            nonlocal progress
            for port in range(lowerport, upperport + 1):
                if self.is_open(port):
                    with lock:
                        self.add_port(port)
                with lock:
                    progress.update(1)

        ports_per_thread = total_ports // num_threads
        open_ports_list = []

        for i in range(num_threads):
            lowerport = i * ports_per_thread
            upperport = (i + 1) * ports_per_thread - 1

            if i == num_threads - 1:  # Last thread handles the remaining ports
                upperport = total_ports

            thread = threading.Thread(target=scan_range, args=(lowerport, upperport))
            open_ports_list.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in open_ports_list:
            thread.join()

        # Close the progress bar
        progress.close()

    def is_open(self, port):
        """
        Check if a specific port is open on the target IP address.

        :param port: The port number to check for openness.
        :return: Scan returns True if the port is open, otherwise it returns False.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        # print('Port {}:         {}'.format(port, result)) // Optionally you can print the port and result here
        # for debugging purposes.
        s.close()
        return result == 0

    def write(self, filepath):
        """
        Write the list of open ports to a file.

        :param filepath: The path of the file to write the open ports to.
        """
        openport = str(self.open_ports)

        output_dir = "scans/"

        filename = f'{self.ip}_{self.timestamp}_open_ports.txt'
        filepath = os.path.join(output_dir, filename)

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        else:
            with open(filepath, 'w') as f:
                f.write(openport)

        print(openport)

@timefunc
def main(filepath=None):
    # Define the target IP address to scan for open ports.
    ip = str(input("Please input the target address you wish to scan: "))

    # Create a Scanner object with the specified IP address.
    scanner = Scanner(ip)

    # Define the number of threads to use for scanning
    num_threads = 8 # Adjustable based on system capabilities

    # Scan ports in the given range and store the open ports in the Scanner object.
    lowerport = input('What is the starting port within the scanning range: ')
    upperport = input('What is the highest port within the scanning range: ')

    lowerport = int(lowerport)
    upperport = int(upperport)

    scanner.threaded_scan(num_threads, upperport - lowerport + 1)


    # Write the list of open ports to a file name open_ports in the scans subdirectory
    scanner.write(filepath)


if __name__ == "__main__":
       main()

#!/usr/bin/env python
# Written for Python3

import subprocess
import optparse


def main():
    # ================================================================================================================
    # Allow arguments to be passed in the command line when initiating the program
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface to have its MAC address changed.")
    parser.parse_args()
    # ================================================================================================================

    # ================================================================================================================
    # Set a banner and allow the user to enter their inputs for the interface name to be changed and the new MAC
    # address
    interface = input("Interface > ")
    new_mac = input("New MAC > ")
    print("=" * 80)
    print(f"[+]    Changing MAC address for {interface} to {new_mac}")
    print("=" * 80)

    # ================================================================================================================
    subprocess.call(["ifconfig", interface, "down"])  # Calls the "ifconfig" and adds the "interface" user
    # input and the "down" command as a single command string
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])  # Calls the "ifconfig" and adds the "interface"
    # user input and the "hw" and "ether" commands and passes in the user input for the new mac address as a
    # single command string
    subprocess.call(["ifconfig", interface, "up"])  # Calls the "ifconfig" and adds the "interface" user
    # input and the "up" command as a single command string


if __name__ == '__main__':
    main()

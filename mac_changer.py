#!/usr/bin/env python
# Written for Python3

import subprocess
import optparse


def change_mac(interface, new_mac):
    # ================================================================================================================
    # Set a banner and allow the user to enter their inputs for the interface name to be changed and the new MAC
    # address
    # ================================================================================================================
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


def main():
    # ================================================================================================================
    # Allow arguments to be passed in the command line when initiating the program
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface to have its MAC address changed.")
    parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address for the chosen interface.")
    options, arguments = parser.parse_args()  # Sets two new variables and passes the values of the arguments that
    # the user passes in the command line into them. Options will contain the values while arguments contain
    # the -i or -m as an example
    # ===============================================================================================================

    change_mac(options.interface, options.new_mac)  # Calls the change_mac() function and passes in the valies of
    # the arguments entered on the command line by the user that are parsed in the options and arguments variables


if __name__ == '__main__':
    main()

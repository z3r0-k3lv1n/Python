#!/usr/bin/env python
# Written for Python3

import subprocess
import optparse


def get_arguments():
    # Allow arguments to be passed in the command line when initiating the program
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface to have its MAC address changed.")
    parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address for the chosen interface.")
    options, arguments = parser.parse_args()
    if not options.interface:
        # Code to handle error if options.interface does not hold a value
        parser.error("[-]   Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        # Code to handle error if options.new_mac does not hold a value
        parser.error("[-]   Please specify a new mac address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    # ================================================================================================================
    # Print a banner and allow the user to enter their inputs for the interface name to be changed and the new MAC
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
    options = get_arguments()  # Sets the options and arguments variables as the returned value of
    # the get_arguments() function
    change_mac(options.interface, options.new_mac)  # Calls the change_mac() function and passes in the values of
    # the arguments entered on the command line by the user that are parsed in the options and arguments variables


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# Written for Python3

import subprocess


def main():

    interface = input("Interface > ")
    new_mac = input("New MAC > ")
    print("=" * 80)
    print(f"[+]    Changing MAC address for {interface} to {new_mac}")
    print("=" * 80)

    subprocess.call(["ifconfig", interface, "down"]) 
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


if __name__ == '__main__':
    main()

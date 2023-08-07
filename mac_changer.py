#!/usr/bin/env python
# Written in Python3

import subprocess


def main():

    interface = "Interface Name > "
    new_mac = input("MAC Address > ")
    print("=" * 80)
    print(f"[+]    Changing MAC address for {interface} to {new_mac}...")
    print("=" * 80)
    
    subprocess.call('ifconfig {interface} down', shell=True)
    subprocess.call('ifconfig {interface} hw ether {new_mac}', shell=True)
    subprocess.call('ifconfig {interface} up', shell=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# Written in Python3

import subprocess


def main():

    interface = "wlan0"
    new_mac = "00:11:22::33::44:55"
    print("[+]" * 60)
    print(f"[+]    Changing MAC address for {interface} to {new_mac}...")
    print("[+]" * 60)
    
    subprocess.call('ifconfig', shell=True)
    subprocess.call('ifconfig {interface} down', shell=True)
    subprocess.call('ifconfig {interface} hw ether {new_mac}', shell=True)
    subprocess.call('ifconfig {interface} up', shell=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import subprocess


def main():
    subprocess.call('clear', shell=True)
    subprocess.call('ifconfig', shell=True)
    subprocess.call('ifconfig wlan0 down', shell=True)
    subprocess.call('ifconfig wlan0 hw ether 00:11:22:33:44:55', shell=True)
    subprocess.call('ifconfig wlan0 up', shell=True)
    subprocess.call('clear', shell=True)
    subprocess.call('ifconfig', shell=True)


if __name__ == '__main__':
    main()

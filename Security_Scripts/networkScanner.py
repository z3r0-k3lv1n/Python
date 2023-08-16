#!/usr/bin/env python3

# A network scanner
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="The legen, wait for it, dairy network scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="The target host to scan")
    args = parser.parse_args()
    return args


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether)  # List the elements that are available in the Ether element.
    arp_request_broadcast = broadcast/arp_request  # Sends out an arp request on the network being scanned.
    # Will return responses as two lists. The Positive responses, meaning there was a response from a device.
    # A negative response. Meaning no response was received, indicating no connection.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # Using the [0] means that it will only
    # capture the positive responses in the variable.

    clients_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}  # Creates a dictionary entry with 2
        # keys and 2 values , the first key:value pair will be the ip address (.psrc), and the second will be the mac
        # address (.hwsrc) for the corresponding ip.
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    # Format a header banner for the output
    print(f"{'=' * 100}\nIP\t\t\tMAC Address\n{'=' * 100}")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")


def main():
    args = get_arguments()
    ip = args.target

    scan_result = scan(ip)
    print_result(scan_result)


if __name__ == '__main__':
    main()

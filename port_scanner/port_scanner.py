#!/usr/bin/env python3
# Yannis Folias
# Multithreaded python port scanner
# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

import socket
import requests
import threading
import time
import os

ports= [
    {"port": 21, "description": "FTP Server", "hints": "- run nmap -V \r\n- Try to connect anonymously"},
    {"port": 22, "description": "SSH Server", "hints": ""},
    {"port": 23, "description": "Telnet", "hints": ""},
    {"port": 25, "description": "SMTP", "hints": ""},
    {"port": 53, "description": "DNS Server", "hints": ""},
    {"port": 69, "description": "TFTP", "hints": ""},
    {"port": 80, "description": "Web Server", "hints": "- run nikto \r\n- run gobuster"},
    {"port": 88, "description": "Kerberos Auth System", "hints": ""},
    {"port": 110, "description": "POP3 Protocol", "hints": ""},
    {"port": 111, "description": "RPC", "hints": ""},
    {"port": 135, "description": "RPC Locator", "hints": ""},
    {"port": 137, "description": "Netbios Name Service", "hints": ""},
    {"port": 139, "description": "Netbios Session Service", "hints": ""},
    {"port": 143, "description": "IMAP Protocol", "hints": ""},
    {"port": 161, "description": "SNMP Protocol", "hints": ""},
    {"port": 162, "description": "SNMP Protocol", "hints": ""},
    {"port": 389, "description": "LDAP Authentication", "hints": ""},
    {"port": 443, "description": "Web server using https", "hints": "- run nmap -V \r\n- Try to connect anonymously"},
    {"port": 445, "description": "SMB Service", "hints": ""},
    {"port": 464, "description": "kerberos Auth", "hints": ""},
    {"port": 631, "description": "IPPl Internet Printing Protocol", "hints": ""},
    {"port": 636, "description": "LDAP Over SSL", "hints": ""},
    {"port": 993, "description": "IMAP Over SSL", "hints": ""},
    {"port": 995, "description": "POP3 Over SSL", "hints": ""},
    {"port": 1099, "description": "Java RMI Registry", "hints": ""},
    {"port": 1521, "description": "Oracle Server", "hints": ""},
    {"port": 2030, "description": "Centos Web Panel", "hints": ""},
    {"port": 2100, "description": "Oracle FTP", "hints": ""},
    {"port": 3268, "description": "LDAP Port", "hints": ""},
    {"port": 3269, "description": "LDAP over SSL", "hints": ""},
    {"port": 3306, "description": "Mysql Server", "hints": ""},
    {"port": 3389, "description": "RDP", "hints": ""},
    {"port": 5000, "description": "Flask default port", "hints": ""},
    {"port": 7778, "description": "Oracle App Server", "hints": ""},
    {"port": 8080, "description": "Tomcat Web Server", "hints": ""},
    {"port": 8443, "description": "Tomcat running over SSL", "hints": ""},
    {"port": 9050, "description": "TOR Socks", "hints": ""},
    {"port": 10000, "description": "Webmin", "hints": ""},
    {"port": 27017, "description": "Default MongoDB", "hints": ""},
    {"port": 27018, "description": "Default MongoDB", "hints": ""}
]

target_ip=input("Provide target ip: ")

def get_header(url):
    res = requests.get(url)
    print(res.headers['Server'])

def portScan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target_ip, port['port']))
    #print("Scanning %s" % port['port'])
    if conn == 0:
        print("Port %s is open" % port['port'])
        if port['hints']!="":
            print(port['hints'])
        if port['port']==80:
            try:
                url=("http://"+target_ip)
                get_header(url)
            except:
                pass
        elif port['port']==443:
            try:
                url=("https://"+target_ip)
                get_header(url)
            except:
                pass
        elif port['port']==8080:
            try:
                url=("http://"+target_ip+":8080")
                get_header(url)
            except:
                pass
        elif port['port']==8443:
            try:
                url = ("https://" + target_ip + ":8443")
                get_header(url)
            except:
                pass
    s.close()

for port in ports:
    t = threading.Thread(target=portScan, args=(port, ))
    t.start()

time.sleep(5)
print("\r\nIf the outcome is not satisfactory enough, please follow steps below:"
      "\r\n- Run a full port scan"
      "\r\n- Run a udp scan"
      "\r\n- Run a network scan (tcpdump/wireshark)"
      "\r\n- Stay calm, it's there")
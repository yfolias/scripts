#!/usr/bin/env python3
# Yannis Folias
# Python fuzzer

import socket

target_ip=input("Provide target ip: ")
target_port=input("Provide target port: ")

for i in range(100):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, int(target_port)))
        payload=int(i)*("A"*100)
        print("Sending %s of As" % len(payload))
    except:
        print("Fuzzer failed")
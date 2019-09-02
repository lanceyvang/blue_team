#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()
    # just for ip.src
    # all_ips_li = re.findall(r"EST;[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", content)

    # for ip.src + ip.dst
    # all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", content)

    # for ftp requests
    # all_ips_li = re.findall(r"EST;[0-9]+\.[0-9]+\.[0-9]+.[0-9]+.+;FTP;Request", content)
    # print(all_ips_li)
    pattern = r"(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)"
    all_ips_li = re.findall(pattern, content)

    ip_dict = {}

    for ip in all_ips_li: 
        if ip in ip_dict: ip_dict[ip] += 1
        else: ip_dict[ip] = 1

    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)

    for ip in sorted_dict:
        print(ip, ip_dict[ip])

if __name__ == '__main__':
    main()
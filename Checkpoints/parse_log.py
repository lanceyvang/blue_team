#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()
    regular_expression = r"(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)"
    all_matches_li = re.findall(regular_expression, content)

    # print(all_matches_li)

    ip_dictionary = {}

    for ip in all_matches_li:
        if ip in ip_dictionary: ip_dictionary[ip] += 1
        else: ip_dictionary[ip] = 1
    
    # print(ip_dictionary)

    def compare_value(ip):
        return ip_dictionary[ip]

    sorted_dictionary = sorted(ip_dictionary, key=compare_value, reverse=True)

    # print(sorted_dictionary)

    for ip in sorted_dictionary[0:5]:
        print(ip, ip_dictionary[ip])

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import sys
import re

def create_dict(content):
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", content)
    ip_dict = {}
    for ip in all_ips_li:
        if ip in ip_dict: ip_dict[ip] += 1
        else: ip_dict[ip] = 1
    return ip_dict

def sort_ip_des(dict):
    
    def compare_ip(ip):
        return int(ip.split('.')[0])

    def compare_amount(ip):
        return dict[ip]
    
    sorted_ips = sorted(dict, key=compare_ip, reverse=True)
    return sorted(sorted_ips, key=compare_amount, reverse=True)

def pad_ip(ip):
    return ' ' * (15 - len(str(ip))) + str(ip)

def print_histogram(dict):
    final_sort = sort_ip_des(dict)
    for ip in final_sort: 
        print(pad_ip(ip) + ' ' + ('*' * dict[ip]) + ' (' + str(dict[ip])+')')

def main():
    content = open(sys.argv[1], 'r').read()
    ip_dict = create_dict(content)
    print_histogram(ip_dict)
    

# It allows the code in the module to be importable by other modules, without executing the code block beneath on import.
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()

'''
OUTPUT
$ python apache_log_parser.py apache_log_parser_data1.txt clear
        1.2.3.4 ***** (5)
        6.6.6.6 **** (4) 
        5.6.7.8 **** (4) 
        9.1.2.3 *** (3)  
244.244.244.244 ** (2)   
        7.6.6.6 ** (2)   
        6.6.7.6 ** (2)   
        6.6.6.7 ** (2)   
        6.7.6.6 ** (2)   
        1.2.3.0 ** (2)   
      261.2.3.4 * (1)    
255.255.254.255 * (1)    
255.255.255.255 * (1)    
       11.5.6.7 * (1)    
       10.3.4.5 * (1)    
       10.0.0.1 * (1)
     10.0.0.256 * (1)
     10.0.0.255 * (1)
        9.1.2.1 * (1)
        9.1.2.4 * (1)
        1.2.3.5 * (1)
        1.2.3.6 * (1)
        1.2.3.1 * (1)
'''
#!/usr/bin/env python
import sys
import re

def create_content():
    file = open(sys.argv[1], 'r')
    content = file.read()
    file.close()
    return content
​
def create_dict(li):
    ip_dict = {}
    for ip_address in li:
        if ip_address in ip_dict: ip_dict[ip_address] += 1
        else: ip_dict[ip_address] = 1
    return ip_dict
​
def sort_ip_li(dict):
    def compare_ip(ip):
        return int(ip.split('.')[0])
    def compare_amount(key):
        return dict[key]
    first_sort = sorted(dict, key = compare_ip)
    return sorted(first_sort, key = compare_amount)
​
def format_amount(n):
    n_str = str(n)
    if len(n_str) == 1: n_str = '00' + n_str
    elif len(n_str) == 2: n_str = '0' + n_str 
    return '('+ n_str + ')'
​
def print_ip_lines(li, dict):
    for ip in li:
        validate = re.search(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)
        print(format_amount(dict[ip]) + ' ' + str(bool(validate)) + ': ' + ip + ' *' )
​
def main():
    content = create_content()
    all_ips = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", content)
    ip_dict = create_dict(all_ips)
    sorted_ips = sort_ip_li(ip_dict)
    print_ip_lines(sorted_ips, ip_dict)
​
main()
​
# OUTPUT
# (001) False: 1.1234.1.1 *
# (001) False: 7.888.8.8 *       
# (001) True: 11.11.11.105 *     
# (001) True: 11.11.11.95 *      
# (001) True: 24.17.237.70 *     
# (001) True: 141.101.98.63 *    
# (001) True: 141.101.98.43 *    
# (001) True: 141.101.97.63 *    
# (001) True: 141.101.198.63 *   
# (001) True: 141.101.98.53 *    
# (001) False: 444.2.2.2 *       
# (001) False: 555.1.1.1 *       
# (001) False: 777.777.7777.777 *
# (001) False: 888.8888.888.888 *
# (001) False: 999.999.999 *     
# (002) True: 2.2.2.2 *
# (002) False: 09.01.02.03 *     
# (002) True: 141.102.98.63 *    
# (003) True: 11.11.11.89 *      
# (003) True: 141.101.98.61 *    
# (004) True: 11.11.11.70 *      
# (004) True: 192.150.249.87 *   
# (004) True: 211.168.230.94 *
# (045) True: 127.0.0.1 *
# (049) True: 211.190.205.93 *
# (050) True: 61.73.94.162 *
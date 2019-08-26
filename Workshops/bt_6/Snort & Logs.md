# 2.Snort
## Install and Setup
### Warm-up Exercise
1. The attacker is doing a ping sweep of the machines on the network.
2. The attacker (192.168.56.104) is scanning the ports of 192.168.56.106
3. The attacker is now browsing the website of the apache server on port 80 of 192.168.56.106.

## Alerting on scans
### Writing Rules
3. Create an alert for any ping traffic incoming to your machine; add this rule into your fullstack.rules file.
```sh
alert icmp any any <> any any (msg:"We're getting scanned!"; sid:1000001)
```
4. Capture packets that contain Metasploitable pinging your Kali machine, then replay that capture through Snort. Observe the alerts from #3 in the snort output.
```sh
root@kali:/media/sf_Downloads/blue_team/Workshops/bt_6# snort -l ./logs -c fullstack.rules -r captured.pcap 
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "fullstack.rules"
Tagged Packet Limit: 256
Log directory = ./logs

+++++++++++++++++++++++++++++++++++++++++++++++++++
Initializing rule chains...
1 Snort rules read
    1 detection rules
    0 decoder rules
    0 preprocessor rules
1 Option Chains linked into 1 Chain Headers
0 Dynamic rules
+++++++++++++++++++++++++++++++++++++++++++++++++++

+-------------------[Rule Port Counts]---------------------------------------
|             tcp     udp    icmp      ip
|     src       0       0       0       0
|     dst       0       0       0       0
|     any       0       0       1       0
|      nc       0       0       1       0
|     s+d       0       0       0       0
+----------------------------------------------------------------------------

+-----------------------[detection-filter-config]------------------------------
| memory-cap : 1048576 bytes
+-----------------------[detection-filter-rules]-------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[rate-filter-config]-----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[rate-filter-rules]------------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[event-filter-config]----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[event-filter-global]----------------------------------
+-----------------------[event-filter-local]-----------------------------------
| none
+-----------------------[suppression]------------------------------------------
| none
-------------------------------------------------------------------------------
Rule application order: activation->dynamic->pass->drop->sdrop->reject->alert->log
Verifying Preprocessor Configurations!

[ Port Based Pattern Matching Memory ]
pcap DAQ configured to read-file.
Acquiring network traffic from "captured.pcap".
Reload thread starting...
Reload thread started, thread 0x7fc2fdee4700 (2103)

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.8.1
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=2098)
WARNING: No preprocessors configured for policy 0.
...
===============================================================================
Run time for packet processing was 1.5917 seconds
Snort processed 72 packets.
Snort ran for 0 days 0 hours 0 minutes 1 seconds
   Pkts/sec:           72
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       2260992
  Bytes in mapped regions (hblkhd):      17117184
  Total allocated space (uordblks):      2067840
  Total free space (fordblks):           193152
  Topmost releasable block (keepcost):   39184
===============================================================================
Packet I/O Totals:
   Received:           72
   Analyzed:           72 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           72 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           51 ( 70.833%)
       Frag:            0 (  0.000%)
       ICMP:           12 ( 16.667%)
        UDP:           34 ( 47.222%)
        TCP:            0 (  0.000%)
        IP6:           16 ( 22.222%)
    IP6 Ext:           21 ( 29.167%)
   IP6 Opts:            5 (  6.944%)
      Frag6:            0 (  0.000%)
      ICMP6:            5 (  6.944%)
       UDP6:           11 ( 15.278%)
       TCP6:            0 (  0.000%)
     Teredo:            0 (  0.000%)
    ICMP-IP:            0 (  0.000%)
    IP4/IP4:            0 (  0.000%)
    IP4/IP6:            0 (  0.000%)
    IP6/IP4:            0 (  0.000%)
    IP6/IP6:            0 (  0.000%)
        GRE:            0 (  0.000%)
    GRE Eth:            0 (  0.000%)
   GRE VLAN:            0 (  0.000%)
    GRE IP4:            0 (  0.000%)
    GRE IP6:            0 (  0.000%)
GRE IP6 Ext:            0 (  0.000%)
   GRE PPTP:            0 (  0.000%)
    GRE ARP:            0 (  0.000%)
    GRE IPX:            0 (  0.000%)
   GRE Loop:            0 (  0.000%)
       MPLS:            0 (  0.000%)
        ARP:            5 (  6.944%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:            0 (  0.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            0 (  0.000%)
      Other:            5 (  6.944%)
Bad Chk Sum:            1 (  1.389%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           72
===============================================================================
Action Stats:
     Alerts:           17 ( 23.611%)
     Logged:           17 ( 23.611%)
     Passed:            0 (  0.000%)
Limits:
      Match:            0
      Queue:            0
        Log:            0
      Event:            0
      Alert:            0
Verdicts:
      Allow:           72 (100.000%)
      Block:            0 (  0.000%)
    Replace:            0 (  0.000%)
  Whitelist:            0 (  0.000%)
  Blacklist:            0 (  0.000%)
     Ignore:            0 (  0.000%)
      Retry:            0 (  0.000%)
===============================================================================
Snort exiting
```
## Scan Behavior
1. Research how to create rules for nmap scans in snort (one resource)
```sh
alert tcp any any -> 192.168.1.105 any (msg: "NMAP TCP Scan";sid:10000005;) 
```
https://github.com/lanceyvang/blue_team/blob/master/Workshops/bt_6/logs/nmap_alert.txt

# Python
```python
#!/usr/bin/env python
import sys
import re
​
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
```
### Find Letter in String
```python
#!/usr/bin/env python3
import sys

def but_really_parse(s, c):
    index = s.find(c)
    # print(s, c, index)
    print(s[:index+1])

def process(line):
    # this should take in a line and print to the screen the result
    # pass
    line = line.strip().split(' )
    # string, character = line
    string = line[0]
    character = line[1]
    # print(line, string, character)
    but_really_parse(string, character)

def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    lines = f.readlines()

    for line in lines:
        process(line)

if __name__ == '__main__':
    main()
```

## Back to Python!
Given a log file, grab as many IP addresses (4 octet numbers) as you can and push those numbers through an IP address validator to verify their correctness. Print out if they are valid or not. Keep track of how many times you see each IP address. Pay close attention to the example output for the formatting and ordering details. 
Example input: ip_finder_and_validator_data1.txt
```python
#!/usr/bin/env python
import sys
import re
​
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
```
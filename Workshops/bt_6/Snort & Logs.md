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

Alert Output
```
[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:02.744089 192.168.56.106 -> 192.168.56.105
ICMP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:37906   Seq:1  ECHO

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:02.744138 192.168.56.105 -> 192.168.56.106
ICMP TTL:64 TOS:0x0 ID:25901 IpLen:20 DgmLen:84
Type:0  Code:0  ID:37906  Seq:1  ECHO REPLY

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:03.743039 192.168.56.106 -> 192.168.56.105
ICMP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:37906   Seq:2  ECHO

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:03.743085 192.168.56.105 -> 192.168.56.106
ICMP TTL:64 TOS:0x0 ID:26117 IpLen:20 DgmLen:84
Type:0  Code:0  ID:37906  Seq:2  ECHO REPLY

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:04.742076 192.168.56.106 -> 192.168.56.105
ICMP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:37906   Seq:3  ECHO

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:04.742123 192.168.56.105 -> 192.168.56.106
ICMP TTL:64 TOS:0x0 ID:26237 IpLen:20 DgmLen:84
Type:0  Code:0  ID:37906  Seq:3  ECHO REPLY

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:05.741382 192.168.56.106 -> 192.168.56.105
ICMP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:37906   Seq:4  ECHO

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:05.741428 192.168.56.105 -> 192.168.56.106
ICMP TTL:64 TOS:0x0 ID:26385 IpLen:20 DgmLen:84
Type:0  Code:0  ID:37906  Seq:4  ECHO REPLY

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:06.740364 192.168.56.106 -> 192.168.56.105
ICMP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:37906   Seq:5  ECHO

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:06.740412 192.168.56.105 -> 192.168.56.106
ICMP TTL:64 TOS:0x0 ID:26573 IpLen:20 DgmLen:84
Type:0  Code:0  ID:37906  Seq:5  ECHO REPLY

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:07.739588 192.168.56.106 -> 192.168.56.105
ICMP TTL:64 TOS:0x0 ID:0 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:37906   Seq:6  ECHO

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:14:07.739635 192.168.56.105 -> 192.168.56.106
ICMP TTL:64 TOS:0x0 ID:26615 IpLen:20 DgmLen:84
Type:0  Code:0  ID:37906  Seq:6  ECHO REPLY

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:16:35.391755 fe80::4df1:e0bd:b460:aff -> ff02::16
IPV6-ICMP TTL:1 TOS:0x0 ID:256 IpLen:40 DgmLen:76

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:16:35.446602 fe80::4df1:e0bd:b460:aff -> ff02::16
IPV6-ICMP TTL:1 TOS:0x0 ID:256 IpLen:40 DgmLen:76

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:16:35.446999 fe80::4df1:e0bd:b460:aff -> ff02::16
IPV6-ICMP TTL:1 TOS:0x0 ID:256 IpLen:40 DgmLen:76

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:16:35.447167 fe80::4df1:e0bd:b460:aff -> ff02::16
IPV6-ICMP TTL:1 TOS:0x0 ID:256 IpLen:40 DgmLen:76

[**] [1:1000001:0] We're getting scanned! [**]
[Priority: 0] 
08/26-11:16:35.813641 fe80::4df1:e0bd:b460:aff -> ff02::16
IPV6-ICMP TTL:1 TOS:0x0 ID:256 IpLen:40 DgmLen:76
```

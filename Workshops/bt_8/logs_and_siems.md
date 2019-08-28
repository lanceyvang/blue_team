# Logs
## Windows logs
What application, service, or type of defense might have generated these logs?  
* These are Windows Firewall logs. There is a rule that blocks ICMP.
```
#Software: Microsoft Windows Firewall
#Time Format: Local
#Fields: date time action protocol src-ip dst-ip src-port dst-port size tcpflags tcpsyn tcpack tcpwin icmptype icmpcode info path
2019-08-05 16:42:33 ALLOW UDP 192.168.56.7 224.0.0.251 5353 5353 0 - - - - - - - SEND
2019-08-05 16:42:33 ALLOW UDP 192.168.56.7 192.168.56.255 137 137 0 - - - - - - - SEND
2019-08-05 16:42:39 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:40 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:41 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:42 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:47 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:48 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:49 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:50 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:51 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:52 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:43:01 ALLOW ICMP ::1 ff02::16 - - 0 - - - - 143 0 - SEND
2019-08-05 16:43:01 ALLOW 2 127.0.0.1 224.0.0.22 - - 0 - - - - - - - SEND
2019-08-05 16:43:01 ALLOW UDP 127.0.0.1 239.255.255.250 63778 1900 0 - - - - - - - SEND
2019-08-05 16:43:01 ALLOW UDP 127.0.0.1 239.255.255.250 63778 1900 0 - - - - - - - RECEIVE
2019-08-05 16:43:16 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:17 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:18 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:19 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
```
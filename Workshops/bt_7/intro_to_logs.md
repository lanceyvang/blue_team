# Reading network logs
![](https://media.amazonwebservices.com/blog/2015/flow_see_a_stream_2.png)

How to Read
![](http://40cloud.com/fcnew/wp-content/uploads/2015/06/flowlogs.jpg)


<details>
    <summary>Show AWS Flow Log</summary>

```
2 123456789010 eni-abc123de 172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK
2 123456789010 eni-abc123de 172.31.9.69 172.31.9.12 49761 3389 6 20 4249 1418530010 1418530070 REJECT OK
2 123456789010 eni-1a2b3c4d - - - - - - - 1431280876 1431280934 - NODATA
2 123456789010 eni-4b118871 - - - - - - - 1431280876 1431280934 - SKIPDATA
2 123456789010 eni-1235b8ca 203.0.113.12 172.31.16.139 0 0 1 4 336 1432917027 1432917142 ACCEPT OK
2 123456789010 eni-1235b8ca 172.31.16.139 203.0.113.12 0 0 1 4 336 1432917094 1432917142 REJECT OK
2 123456789010 eni-f41c42bf 2001:db8:1234:a100:8d6e:3477:df66:f105 2001:db8:1234:a102:3304:8879:34cf:4071 34892 22 6 54 8855 1477913708 1477913820 ACCEPT OK
root@kali:/media/sf_Downloads/blue_team/Workshops/bt_6# date -d @1477913820
Mon 31 Oct 2016 07:37:00 AM EDT
```
</details>


## Pcap
https://web.archive.org/web/20190102062652/http://laredo-13.mit.edu/~brendan/regin/pcap/

We had a user that' surfing the internet on IE8 and reading news online. He's possibly updating his Windows computer too.

# Web Proxies
* What kind of HTTP request(s) are being made?
    * We have 200 and 304 request  
* What do the different HTTP status codes mean for each request?
    * 
* What story are these logs telling us? (big picture)
    * We have a user using web proxies to visit travelocity to view vacations in Twin Peaks, California.
```
## bluecoat proxy logs
## http://log-sharing.dreamhosters.com/bluecoat_proxy_big.zip
## tail -n300 Demo_log_001.log
## dont `cat` these logs; millions of lines

2005-05-04 17:16:08 1 45.14.4.61 304 TCP_HIT 207 431 GET http hg.travelocity.com.edgesuite.net /graphics/tvly_mc_125x25.gif - - DIRECT 80.67.66.62 image/gif "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)" PROXIED Travel - 192.16.170.42 SG-HTTP-Service - none -
2005-05-04 17:16:08 154 45.14.4.127 200 TCP_NC_MISS 2973 720 GET http images.google.com /images ?q=tbn:-dEjG3JAHxgJ:www.kevcom.com/images/linux/linux.logo.2yp.jpg - DIRECT images.google.com image/jpeg "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312" PROXIED Hacking/Proxy%20Avoidance - 192.16.170.42 SG-HTTP-Service - none -
2005-05-04 17:16:08 18 45.23.4.216 304 TCP_RESCAN_HIT 422 405 GET http twinpeaksweather.com /java-sys/Dgclock.class - - DIRECT 66.235.216.135 application/octet-stream "Mozilla/4.0 (Windows 2000 5.0) Java/1.5.0_02" PROXIED News/Media - 192.16.170.42 SG-HTTP-Service - none -
```

## Firewalls

Which protocol is being allowed by UFW?
* TCP
Which port is allowed through the firewall?
* 80
How many different IP addresses are found in the log?
* 3
Which service was MOST likely blocked on UDP/67?
* DHCP

## Netflow

* In Kali, install ntopng: apt install ntopng
* Download this pcap
* Run a redis server: redis-server &
* Run ntopng with that pcap as the interface: ntopng --disable-autologout --disable-login=1 -i ./pcap-file.pcap
* Open a browser and visit localhost:3000; replace localhost with your Kali ip address to use a browser on your host machine
* Explore the flows and answer the questions below:

Questions:
Which sites are users visiting?
* Google, Facebook, Other, Unknown
How many unique clients are in the log?
    * 10.0.3.15
    * 172.217.164.164
    * 31.13.66.19
    * 172.217.164.131
    * Other
Is any client performing any suspicious activity? If so, which client performed the suspicious activity, and what was the target?
* 10.0.3.15 : digicert.com, lots of UDP activity
Which DNS server are clients using?
    * 1.1.1.1: Cloudflare

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

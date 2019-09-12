# VM-Ware

## Basic Configuration for VMs
![](https://technology.amis.nl/wp-content/uploads/2018/07/virtualbox-networking-overview-768x155.png)

By default, things on the internet cannot talk to your devices for safety reasons. However, you can set up port forwarding on your router and when traffic comes in for a ip at the right port, the traffic will go to that device.
https://technology.amis.nl/2018/07/27/virtualbox-networking-explained/

### Host-only
![](https://technology.amis.nl/wp-content/uploads/2018/07/virtualbox-host-only-768x298.png)

### Internal
![](https://technology.amis.nl/wp-content/uploads/2018/07/virtualbox-internal-network-768x303.png)

### Bridged
![](https://technology.amis.nl/wp-content/uploads/2018/07/virtualbox-bridged-768x300.png)

### NAT
![](https://technology.amis.nl/wp-content/uploads/2018/07/virtualbox-nat-768x295.png)

## NAT Network
![](https://technology.amis.nl/wp-content/uploads/2018/07/virtualbox-nat-network-768x298.png)

## Passive Recon: Using publicly available information
* Open Web Information Gathering
* Email Harvesting
<details><summary>theHarvester Example</summary>

```
root@kali:~# theharvester -d fullstackacademy.com -b google

Warning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.


*******************************************************************
*                                                                 *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __| '_ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester Ver. 3.0.6                                         *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*******************************************************************


found supported engines
[-] Starting harvesting process for domain: fullstackacademy.com

[-] Searching in Google:
	Searching 0 results...
	Searching 100 results...
	Searching 200 results...
	Searching 300 results...
	Searching 400 results...
	Searching 500 results...

Harvesting results
No IP addresses found


[+] Emails found:
------------------
hello@fullstackacademy.com
first@fullstackacademy.com
it@fullstackacademy.com
press@fullstackacademy.com
johns@fullstackacademy.com
slo@fullstackacademy.com
admissions@fullstackacademy.com
 
[+] Hosts found in search engines:
------------------------------------

Total hosts: 3

[-] Resolving hostnames IPs... 
 
cloud.fullstackacademy.com:99.84.106.63
cyber.fullstackacademy.com:54.83.25.24
www.fullstackacademy.com:54.83.25.24
```
</details>

* Netcraft.com
* Whois
```
root@kali:~# whois fullstackacademy.com
   Domain Name: FULLSTACKACADEMY.COM
   Registry Domain ID: 1809991644_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.godaddy.com
   Registrar URL: http://www.godaddy.com
   Updated Date: 2019-06-22T15:18:16Z
   Creation Date: 2013-06-21T18:37:40Z
   Registry Expiry Date: 2020-06-21T18:37:40Z
   Registrar: GoDaddy.com, LLC
   Registrar IANA ID: 146
   Registrar Abuse Contact Email: abuse@godaddy.com
   Registrar Abuse Contact Phone: 480-624-2505
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientRenewProhibited https://icann.org/epp#clientRenewProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Name Server: NS51.DOMAINCONTROL.COM
   Name Server: NS52.DOMAINCONTROL.COM
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2019-09-03T01:00:49Z <<<
```
* recon-ng
    * Similar in use to metasploit but for recon

## Active Recon: Touching the Target
* DNS Enumeration
    * `host -t ns fullstackacademy.com`
    * `host -t axfr domain.name dns-server`
    * `dig axfr @dns-server domain.name`

<details><summary>dnsenum example</summary>

* Port Scanning
    * -sS (steaktg SYN scan), 
    * -sT (TCP connect scan), 
    * -Pn (skip host discovery and port scan all target hosts), 
    * -p- (scan ports from 1 through 65535), 
    * -A (agressive scan, -O -sV -sC --traceroute), 
    * -O (OS detection), 
    * -sV /-a(service detection), 
    * -oA (output into three formats), 
    * -v (enable verbose mode)
    * -sU (UDP Scan)
* SMB Enumeration
* SMTP Enumeration

## Zone Transfer
```
host -t ns wikipedia.com

host -l wikipedia.com ns1.wikipedia.com

dig -axfr @<DNS you are querying> <target>

dnsrecon.py -d <domain> -a

dnsrecon.py -d <domain> -t axfr

dnsenum zonetransfer.me
```
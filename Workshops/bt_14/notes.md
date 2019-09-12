Lance Vang, Rita Law
# Blue Team Incident Handling Lab
## Specific Commands/Filters Used
* ip.addr==10.10.4.251 and ip.addr==172.16.2.0/24  // displays only packets with these ip addresses
* ip.addr==172.16.2.0/24 && DNS
* ip.addr==172.16.2.58 && ip.addr==10.10.4/0/24
* host -t ANY inserturl  // grabs all the IPv6, MX, IPv4 information
* host -a inserturl // same content as using ANY but formatted differently
* FTP commands: LIST, CWD, SYST
* SYN, SYN ACK -connection established
* FIN or RST means the conversation is over

## Lab Questions
What tools will you use to analyze the network traffic and log files?
* Wireshark
* Kali VM

What is the IP address of the host that accessed our DNS server?  
* 172.16.2.58

What are the first 3 requests made from that host to our DNS? 
* First request was a forward lookup for AAAA records.
* Second request was a forward lookup for A records. 
* Third request was a lookup for CNAME records.

What information has the external host determined about our network that he/she might use during subsequent penetration attempts? 
* He has the name servers so he may be able to do a zone transfer. 
* He can also do a ping sweep of the network. 

What is unusual about this interaction between an (external) Internet host and our DNS server?
* The DNS server is sending information via TCP later rather than UDP to communicate, which means this DNS server can be used for zone transfers.

Which hosts were scanned? 
* 10.10.4.1, 10.10.4.12, 10.10.4.16, 10.10.4.251

The attacker scanned the same group of ports on each server. Which ports did the attacker include in his/her scan of these hosts?
Hosts		|	Ports Scanned	|	Open Ports
--- | --- | ---
10.10.4.1 	| 	20,21,25,80,443	| 	22, 80, 443
10.10.4.12 	| 	20,21,25,80,443	|	21, 80, 443	
10.10.4.16 	| 	20,21,25,80,443	|	21, 22
10.10.4.251 	| 	20,21,25,80,443	|	53

Which ports did the attacker ﬁnd open (which ports accepted connection attempts)? Hint: look for evidence of a complete TCP 3-way handshake. 
* Refer to chart on question 7

What is wrong with our ﬁrewall rules that allowed these scans to get to our DMZ network? Hint: The ﬁrewall rules are provided in ﬁrewall rules.txt.
* The firewall rules for DNS are too permissive and allow both TCP and UDP for all IPs. 

 What did the attacker do during his/her anonymous login? What information was the attacker able to get from the FTP server during the anonymous login? Hint: look at both the ftp and ftp-data trafﬁc (tcp ports 20 and 21).
* The FTP server responds with 220 indicating that it is ready for the new client. During the anonymous login, the attacker was able to get the directory listing to get usernames. He was later able to log in as lazyjoe using information from the listing. The attacker also used the SYST command to look for information about the server’s operating system. 

What approach did the attacker take with the internal web server (what was he/she doing that could be considered malicious)? Give examples of malicious behavior. Hint: Don’t forget the log ﬁles!
* The attacker was attempting a SQL injection to get login information and a password file.

What information was the attacker able to gain from the internal web server that he/she could use in his/her continued attempts to compromise your network?
* The attacker was able to gain logins and usernames as well as a server file.

Which account does the attacker use to log in to the FTP server?
* He uses lazyjoe to log in.

What password does the attacker use to log on to the FTP server? 
* The attacker logs in with the password L3tM3InN0w!!

Where did the attacker get that password? 
* We believe he might have received it via the anonymous FTP login where he acquired the directory listing, or he was able to find it when he changed to lazyjoe’s user directory.

What ﬁles did the attacker attempt to GET from the FTP server?
* The attacker was able to gain passwd and shadow files.

Which ﬁles did they successfully GET?
* He was able to get the passwd file.

The attacker placed some ﬁles on the FTP server. What are the names of the ﬁles the attacker tried to upload to the server?
* The attacker was uploading netcat.exe and crontab over to the server.

Which ﬁles did he/she successfully upload? 
The attacker successfully loaded both netcat.exe and crontab. 
Should any rules be immediately applied to prevent further malicious activity from the suspected attacker? If so, what should the new rule(s) be?
A firewall rule should deny all traffic from 172.16.2.58.
Are there any other actions that you would recommend to system administrators to contain the current event? (Your answer should be speciﬁc to the incident you are investigating.)
They should reconfigure the DNS to only allow zone transfers from only specified hosts.
Is there evidence that the attacker put something on your system that will allow him or her to easily regain access? Hint: What ﬁles did the attacker UPLOAD to your network and what might he/she be able to do with them?
The attacker put netcat.exe and crontab on the system and can easily schedule netcat.exe to send a reverse shell back to his system using crontab.
What server would you check immediately to determine whether any unusual ports are open? Why? 
We would check the FTP server for strange open ports.
Assuming that you ﬁnd evidence that one of your systems remains compromised after the attack, what actions do you recommend that system administrators take to remedy the compromise?
We would recommend checking the crontab file to see if it’s starting up services.
What conﬁguration changes must be made on our current DNS server to limit outsiders’ access to detailed information about our network?
In Windows, the DNS server manager can only allow access to specific IP addresses, and then enable the Only Allow Access From Secondaries Included on the Notify List. In Linux, the DNS configuration file must be configured to enter specific IP addresses that are allowed for zone transfers.
The company is currently using a single DNS server to service both internal and external DNS requests. Assuming the company has sufﬁcient resources to deploy a second DNS server, in what conﬁguration should we deploy those servers to improve security? How is security improved by your recommendation?
Zone transfers should only be allowed from master to slave DNS server, but the slave DNS server should not be configured to allow any zone transfers besides the master DNS server. 
What ﬁrewall rule changes do you recommend to provide better security to our DMZ? (You need not provide a speciﬁc set of rules, but you should recommend a better approach for our ﬁrewall conﬁguration and provide enough guidance so your recommendations can be implemented).
DNS requests via TCP should be blocked because they are generally used for zone transfers.
The only security-speciﬁc device in our network is a ﬁrewall. Are there any additional network devices that we could have placed in our network to alert systems administrators of potentially malicious activity on our network? How would such devices improve security?
We recommend installing host-based anti-virus software and a network and host-based IDP/IPS on the system. The anti-virus would immediately malicious files with known signatures, and IDS/IPS would detect the malicious attacker due to its frequent requests.
Are there any services on the network that should be turned off to better protect data in transit? What can those potentially insecure services be replaced with to provide better security?
FTP should not enabled because everything is sent in cleartext. Instead, they should enable SFTP so that things can be sent securely and no anonymous login can be used.
There seems to be a problem with the password policy on the network since you should have seen at least some passwords in the network trafﬁc. What is wrong with the current password and what recommendations would you make with regard to password policy to ﬁx this issue?
Data that is sent over the network should be sent using secure protocols such as SSH. They should also only use HTTPS because web traffic is unencrypted.


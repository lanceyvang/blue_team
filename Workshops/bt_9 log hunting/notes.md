# Log Hunting
## Hunting
### Network/Host Logs
* Log 1
    * AUDIT very verbose logging mode
* Log 2  
    * 1337 port used
* Log 3
### Host Logs
<details><summary>Show Log 1</summary>

```
Aug  5 14:09:20 debian sudo:   debian : TTY=pts/0 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  5 14:09:20 debian sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Aug  5 14:09:20 debian su: (to root) debian on pts/0
Aug  5 14:09:20 debian su: pam_unix(su:session): session opened for user root by (uid=0)
Aug  5 14:09:22 debian su: pam_unix(su:session): session closed for user root
Aug  5 14:09:22 debian sudo: pam_unix(sudo:session): session closed for user root
Aug  5 14:09:23 debian sudo:   debian : TTY=pts/0 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  5 14:09:23 debian sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Aug  5 14:09:23 debian su: (to root) debian on pts/0
Aug  5 14:09:23 debian su: pam_unix(su:session): session opened for user root by (uid=0)
Aug  5 14:09:41 debian su: pam_unix(su:session): session closed for user root
Aug  5 14:09:41 debian sudo: pam_unix(sudo:session): session closed for user root
Aug  5 14:09:43 debian sudo:   debian : TTY=pts/0 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  5 14:09:43 debian sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
``` 
</details>

1. Linux (debian) | inside /var/log/auth.log
2. Root user typing su three times.
3. Normal?
4. root | root | no IP

<details><summary>Show Log 2</summary>

```
Aug  6 02:52:28 debian sudo:   debian : 3 incorrect password attempts ; TTY=pts/2 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  6 02:52:31 debian sudo: pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/2 ruser=debian rhost=  user=debian
Aug  6 02:52:42 debian sudo:   debian : 3 incorrect password attempts ; TTY=pts/2 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  6 03:14:30 debian sudo: pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/6 ruser=debian rhost=  user=debian
Aug  6 03:14:50 debian sudo:   debian : 3 incorrect password attempts ; TTY=pts/6 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
```
</details>

* Linux | Trying to access sudo but don't have the priv
* Couldn't authenicate to SUDO
* SSH Logs

<details><summary>Log 4</summary>

```
Aug  6 02:54:16 debian sshd[1278]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  6 02:54:18 debian sshd[1278]: Failed password for root from 192.168.56.3 port 53312 ssh2
Aug  6 02:54:23 debian sshd[1278]: Failed password for root from 192.168.56.3 port 53312 ssh2
Aug  6 02:54:29 debian sshd[1278]: Failed password for root from 192.168.56.3 port 53312 ssh2
Aug  6 02:54:31 debian sshd[1278]: Connection closed by authenticating user root 192.168.56.3 port 53312 [preauth]
Aug  6 02:54:31 debian sshd[1278]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  6 02:54:37 debian sshd[1280]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  6 02:54:39 debian sshd[1280]: Failed password for root from 192.168.56.3 port 53314 ssh2
Aug  6 02:54:42 debian sshd[1280]: Failed password for root from 192.168.56.3 port 53314 ssh2
Aug  6 02:54:47 debian sshd[1280]: Failed password for root from 192.168.56.3 port 53314 ssh2
Aug  6 02:54:47 debian sshd[1280]: Connection closed by authenticating user root 192.168.56.3 port 53314 [preauth]
Aug  6 02:54:47 debian sshd[1280]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
```
</details>

* Trying to SSH in and failing.

<details><summary>Log 5</summary>

```
Aug  5 14:30:19 debian sshd[2251]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2252]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2259]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2257]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2255]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2254]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2258]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2261]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2256]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2260]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:20 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:20 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:20 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:20 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:20 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:20 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:20 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:20 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:20 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:20 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:22 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:23 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:23 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:23 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:23 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:23 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:23 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:23 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:23 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:23 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:25 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:25 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:25 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:26 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:26 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:26 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:26 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:26 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:26 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:26 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:28 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:28 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:28 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:28 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:28 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:28 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:28 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:28 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:28 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:28 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:31 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:31 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:31 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:31 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:31 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:31 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:31 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:32 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:32 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
```
</details>

## 5. Detection Alerts
### Scenario 1: DNS
1. Evaluate the below screenshots.
    * Image is from pi-hole, an ad-blocking solution.
2. Which domains were blocked by the firewall?
    * v10.events.data.microsoft.com blocked is Microsoft diagnostic data.
    * settings-win.data.microsoft.com Blocked dynamic configuration updates.
3. Are the domains potentially malicious?
    * The domains are probably not malicious.
4. What is the likely reason the domains were blocked?
    * The user probably didn't want to send extra data to Microsoft.

Image 1
![](https://github.com/lanceyvang/blue_team/blob/master/Workshops/bt_9%20log%20hunting/files/bt8.5.2-1.png?raw=true)

Image 2
![image 2](https://github.com/lanceyvang/blue_team/blob/master/Workshops/bt_9%20log%20hunting/files/bt8.5.2-3.png?raw=true)

### Scenario 2: Antivirus
1. Which application generated the below detection alerts?
    * AVG AntiVirus 
2. Are the detected actions benign or malicious?
    * Malicous
3. Are all of the quarantined items in image 2 malicious?
    * These files are probably malicious.
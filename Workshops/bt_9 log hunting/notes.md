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

Log 3
* SSH Logs

Log 4
* Trying to SSH in and failing.

Log 5

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

![](https://learndotresources.s3.amazonaws.com/workshop/5d4458a5cf11e4000483a2a7/bt8.5.2-1.png)
![image 2](https://learndotresources.s3.amazonaws.com/workshop/5d4458a5cf11e4000483a2a7/bt8.5.2-3.png)
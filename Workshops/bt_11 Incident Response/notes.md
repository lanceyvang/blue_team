# Incident Response 
![](https://pronto-core-cdn.prontomarketing.com/2/wp-content/uploads/sites/334/2017/05/incident-response-lifecycle.png)
## Service Issue Plan

## Incident Response Phases
* Preparation
    * Upgrading the organization's firewall to block a new type of attack.
    * Assembling the hardware and software required to conduct an incident investigation. 
* Detection & Analysis
    * Receiving a report from a staff member about a malware infection.
    * Indentifying the attackers and attacking systems.
    * Interpreting log entries using a SIEM to identify a potential incident.
* Containment Eradication & Recovery
    * Recoverying normal operations after eradicating an incident.
* Post-Incident Activity
    * Conducting a lessons-learned review session.

## Service Issue Plan
Write a Service Issue Response Plan

Write an identification and response plan for services that an organization you are familiar with relies on. Your response plan should presume that a service issue or outage has been reported, but the cause is not known. Ensure that you cover key elements discussed in this chapter, including

How you would identify potential issues using the application and system logs
* How you would monitor the service for problems
* What types of issues you would look for
* What the organization’s response should be

Once you have completed your plan, walk through it using an example issue. Ensure that your plan would address the issue and that you would be able to provide a complete report to your organization's management about the issue.


# BT 11: Incident Response > Malicious or Not?
## Passwords
Alert

Suspected password(s) sent via plaintext!
Task

Review the following pcap. Our systems have alerted that it may contain user credentials sent in the clear. Document what steps you take to find any evidence, such that your teammates might be able to verify your conclusions. Include references to specific packets/streams, and/or screenshots as evidence. Complete the following tasks:

1. Find all instances of user passwords, or note that this is a false positive if none exist.
2. Make recommendations for follow-up actions
    * Dismiss as false positive
    * More information required, what questions do you need to ask/answer?
    * User action required, who do you contact and what do you say?
    * Analyst/IT action, what action can remediate this incident?
    * Escalate to incident management, why does this require a larger response? Who might you need to include?

In display filter:

`http.request.method == "POST" and http contains "password"`

Right-click, follow TCP stream
Look for password in red.
Try searching for "pw" in Find: field:

![pw-proof1](https://raw.githubusercontent.com/fredhtan/blueteam/master/workshops/blueteam11/files/bt11passwords1.PNG)

![pw-proof2](https://raw.githubusercontent.com/fredhtan/blueteam/master/workshops/blueteam11/files/bt11passwords2.PNG)
This is was an incorrect password.  401 error
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
IP Address + MAC Address - look up DHCP

`http.request.method == "POST" and http contains "pw"`

![pw-proof3](https://raw.githubusercontent.com/fredhtan/blueteam/master/workshops/blueteam11/files/bt11passwords3.PNG)

`http.request.method == "POST"`
![pw-proof4](https://raw.githubusercontent.com/fredhtan/blueteam/master/workshops/blueteam11/files/bt11passwords2a.PNG)

## Email
Alert
User reports suspicious email, and sends you this screenshot.
![](https://pepipost.com/wp-content/uploads/2017/01/email-header-gmail.png)

## Task
We love getting user reports! They are an important part of the defensive layers in our organization. Users frequently flag suspicious emails, but don't always send enough information to make a clear recommendation.

1. Craft an email response to this user, thanking them for their report (you want more!), and asking for more information. What specific information do you need? Include steps any user could follow to get that information to you.
    * Thank the user
    * Ask if this was the only email from this address
    * Did the user search for this (nitric oxide) online at any point in time?
    * Did they visit any suspicious website or links in the last few weeks.
    * Maybe ask for their name and contact information?
2. Send that email to your partner! Create a help ticket if you asked for information from the user.
3. Make recommendations for follow-up actions
    - Dismiss as false positive
    - More information required, what questions do you need to ask/answer?
    - User action required, who do you contact and what do you say?
    - Analyst/IT action, what action can remediate this incident?
    - Escalate to incident management, why does this require a larger response? Who might you need to include?
# How to Parse a Log with Python
Writing Python code to parse a log is easier than you think. This is because even when searching for different things, most of the Python code is reused. The only thing you need to change is the search term you're interested in.

## Boiler Plate
This is the boiler plate (starting code) you will almost always use when parsing a log file. The only thing you need to change is the code inside `main`.
```py
#!/usr/bin/env python3
import sys # needed to read files
import re # needed to use regular expression

def main():
    # opens the content of the file into one very long string
    content = open(sys.argv[1], 'r').read()

# Written this way to make exporting easier. The if-statement makes it so main will only run if the python file is ran directly. If you want more details, you can read here: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ '__main__':
    main()
```

## Regular Expression
The next step is deciding what pattern in the log you want to search for and creating a regular expression for it. Do not be scared of regular expression, you just need to know it at a very, very basic level. You can use https://regex101.com/ to make sure your regular expression matches. Here are some examples and you can find more in Google.

### Find IP Address
* `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}`  
    * `[0-9]{1,3}` means any number between 0 and 9, at least 1 digit and max 3 digit.
    * `\.` the backslash is used to escape a get the literal value.
    * Use only if you're sure all the IPs in the log are valid, matches 0.0.0.0 to 999.999.999.999

### Validate IP
* `(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)`

### FTP requests:
```
5;Jan 10, 2003 04:34:13.455582000 EST;65.240.185.205;2335;131.243.2.12;21;6;56;FTP;Request: USER anonymous
6;Jan 10, 2003 04:34:13.455754000 EST;131.243.2.12;21;65.240.185.205;2335;6;40;TCP;21 â†’ 2335 [ACK] Seq=84 Ack=17 Win=64240 Len=0
```
* `(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)`
    * Look for an IP that starts with `EST;` goes on for some length, `.+`, and ends with `FTP;Request`
```py
#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()

if __name__ '__main__':
    main()
```
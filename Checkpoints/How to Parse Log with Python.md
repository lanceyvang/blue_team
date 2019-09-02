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

# Written this way to make exporting easier. 
# The if-statement makes it so main will only run if the python file is ran directly. 
# If you want more details, you can read here: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
```

## Creating Regular Expression Patterns
The next step is deciding what pattern in the log you want to search for and creating a regular expression for it. Do not be scared of regular expression, you just need to know it at a very, very basic level. You can use https://regex101.com/ to make sure your regular expression matches. Here are some examples and you can find almost any other pattern on Google or http://regexlib.com.

### Find IP Address
* `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}`  
    * `[0-9]{1,3}` means any number between 0 and 9, at least 1 digit and max 3 digit.
    * `\.` the backslash is used to escape a get the literal value.
    * Use only if all the IPs in the log are valid, matches 0.0.0.0 to 999.999.999.999

### Validate IP
* `(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)`

### IP with FTP requests
* `(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)`
    * Look for an IP that starts with `EST;` goes on for some length, `.+`, and ends with `FTP;Request`
```
5;Jan 10, 2003 04:34:13.455582000 EST;65.240.185.205;2335;131.243.2.12;21;6;56;FTP;Request: USER anonymous
6;Jan 10, 2003 04:34:13.455754000 EST;131.243.2.12;21;65.240.185.205;2335;6;40;TCP;21 â†’ 2335 [ACK] Seq=84 Ack=17 Win=64240 Len=0
```

## Using Regular Expression Patterns
```py
#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()

    # To create a regular expression, start with r and use quotations around the regular expression pattern.
    regular_expression = r"(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)"

    # To find all the matches we use re.findall, this will return the result in a list.
    all_matches_li = re.findall(pattern, content)
    
    # print(all_matches_li)
    # ['65.240.185.205', '65.240.185.205', '65.240.185.205', ...]


if __name__ == '__main__':
    main()
```

## Counting the Matches
One of best way to keep track of duplicates is by creating a dictionary.
```py
#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()
    regular_expression = r"(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)"
    all_matches_li = re.findall(regular_expression, content)

    ip_dictionary = {}

    # Go through all_matches_li and if the ip is in ip_dictionary then increase the current value by 1, 
    # if the ip isn't in the ip_dictionary then add that ip to ip_dictionary set its value to 1.
    for ip in all_matches_li:
        if ip in ip_dictionary: ip_dictionary[ip] += 1
        else: ip_dictionary[ip] = 1

    # print(ip_dictionary) 
    # => {'84.68.192.198': 36, '9.141.237.194': 40, ...}

if __name__ == '__main__':
    main()
```
## Sorting the Matches
```py 
#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()
    regular_expression = r"(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)"
    all_matches_li = re.findall(regular_expression, content)

    ip_dictionary = {}

    for ip in all_matches_li:
        if ip in ip_dictionary: ip_dictionary[ip] += 1
        else: ip_dictionary[ip] = 1

    # This function takes in an ip and returns its value from the ip_dictionary.
    def compare_value(ip):
        reurn ip_dictionary[ip]

    # Sorted takes in something that's iterable (list, dictionary, etc.)
    # and sorts it based on the key which is a function that decides the sorting order.
    # Set reverse to True for greatest-to-least sorting and False for least-to-greatest sorting
    sorted_dictionary = sorted(ip_dictionary, key=compare_value; reverse=True)

    # print(sorted_dictionary)
    # => ['157.231.148.18', '70.68.140.137', '83.1.240.233',...]

if __name__ == '__main__':
    main()
```
## Display the Results 
```py 
#!/usr/bin/env python3
import sys
import re

def main():
    content = open(sys.argv[1], 'r').read()
    regular_expression = r"(?<=EST;)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?=;.+FTP;Request)"
    all_matches_li = re.findall(regular_expression, content)

    ip_dictionary = {}

    for ip in all_matches_li:
        if ip in ip_dictionary: ip_dictionary[ip] += 1
        else: ip_dictionary[ip] = 1

    def compare_value(ip):
        reurn ip_dictionary[ip]

    sorted_dictionary = sorted(ip_dictionary, key=compare_value; reverse=True)

    # Loops through the top 5 items in the dictionary and print their key and value.
    for ip in sorted_dictionary[0:5]:
        print(ip, ip_dictionary[ip])

if __name__ == '__main__':
    main()
```

## Running the Python Script
```
python parse_log.py log.txt =>

('157.231.148.18', 3861)
('70.68.140.137', 1574)
('83.1.240.233', 1271)
('38.93.253.216', 1084)
('143.156.1.2', 908)
```

## Tips
* Test your code as you write it to catch errors.
* Copy a few lines from the log into a new log and use that log to help you write your code.
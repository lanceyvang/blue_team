#!/usr/bin/env python3

def add_li(li):
    sum = 0

    for i in li:
        sum += i

    return sum

confuse_students = add_li([1,2,3])

print(confuse_students) # => 6



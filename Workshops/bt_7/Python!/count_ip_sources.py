#!/usr/bin/env python
import sys

def main():
    file = open(sys.argv[1], 'r')
    content = file.read().split('\n')
    file.close()

    counter = 0
    dictionary = {}
    
    for line in content:
        line_split = line.split(' ')
   
        try:
            src_dst = line_split[11] + line_split[12]
            if src_dst in dictionary: dictionary[src_dst] += 1
            else: 
                dictionary[src_dst] = 1
                counter += 1
        except:
            # try-except will make sure code doesn't break when it sees a line that doesn't have an ip src + dst
            # print(line) 
            pass
    # print(dictionary)
    print('There are ' + str(counter) + ' unique IP sources and destinations')

if __name__ == '__main__' :
    main()
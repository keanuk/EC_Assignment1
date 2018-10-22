#!/usr/bin/env python2
import sys
 
prev_key = None 
total = 0 
 
for line in sys.stdin: 
    key, value = line.strip().split('\t')
    value = int(value)

    if prev_key == key:
        total += value
    else:
        if prev_key != None:
            print prev_key + '\t', total
            
        total = value
        prev_key = key

if prev_key == key: 
    print prev_key + '\t', total

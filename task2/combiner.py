#!/usr/bin/env python2
import sys
 
prev_key = None 
values = [] 
 
for line in sys.stdin: 
    key, value = line.strip().split('\t')                                   
    if key != prev_key and prev_key is not None:
        result_key, result_value = prev_key, sum(values)
        if result_value >= 5:
            print(result_key + "\t" + str(result_value)) 
        values = [] 

    prev_key = key 
    values.append(int(value)) 

if prev_key is not None: 
    result_key, result_value = prev_key, sum(values)
    if result_value >= 5:
        print(result_key + "\t" + str(result_value))

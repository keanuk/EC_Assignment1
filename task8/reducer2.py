#!/usr/bin/env python2
import sys

total = 0
count = 0
currDec = 0

for line in sys.stdin:
    year, rating = line.strip().split('\t')
    if int(year[2]) == currDec:
        count += 1
        total += float(rating)
    else:
        if count != 0:
            print '19' + str(currDec) + '0', '\t', round(total / (count), 1)    
        total = float(rating)
        currDec = int(year[2])
        count = 1
print '19' + str(currDec) + '0', '\t', round(total / (count), 1)    
 
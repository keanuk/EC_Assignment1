#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line) > 3:
        if line[5] != '\N' and int(line[5]) >= 1900 and int(line[5]) <= 1999: 
            print line[0], '\t', line[5]
    else:
        print line[0], '\t', line[1]
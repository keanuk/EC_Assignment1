#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    for word in line[5]:
        if line[5] != '\N':
            print line[1] + '\t', line[5]

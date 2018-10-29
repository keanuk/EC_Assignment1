#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[5] != '\N' and line[8] != '\N' and int(line[5]) >= 2000 and int(line[5]) <= 2014:
        for genre in line[8].split(','):
            print genre, '\t', 1
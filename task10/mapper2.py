#!/usr/bin/env python2
import sys

for line in sys.stdin:
    title, value = line.strip().split('\t')
    if line[5] != '\N' and int(line[5]) >= 2010 and int(line[5]) <= 2018:
        print line[0], '\t', line[5]

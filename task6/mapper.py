#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[1] != '\N':
        print line[0], '\t', line[2]
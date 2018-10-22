#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    for word in line[8].split(','):
        if word != '\N':
            print word + '\t', 1
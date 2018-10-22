#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    for word in line[4].split(','):
        if word[:3] == 'act':
            print 'act\t', 1
            break
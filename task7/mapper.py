#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[2] != '\N':
        writerCount = 0
        for writer in line[2].split(','):
            writerCount += 1
        print line[0], '\t', writerCount
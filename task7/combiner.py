#!/usr/bin/env python2
import sys

total = 0
count = 0

for line in sys.stdin:
    key, value = line.split('\t')
    total += float(value)
    count += 1

print 'combined', '\t', total / count
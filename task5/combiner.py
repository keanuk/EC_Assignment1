#!/usr/bin/env python2
import sys

earliest = None
latest = None

for line in sys.stdin:
    key, value = line.split('\t')
    if value > latest or latest == None:
        latest = '{}\t{}'.format(key, value)
    elif value < earliest or earliest == None:
        earliest = '{}\t{}'.format(key, value)

print earliest, latest.strip('\n')
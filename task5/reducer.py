#!/usr/bin/env python2
import sys

earliest = None
latest = None

for line in sys.stdin:
    key, value = line.split('\t')
    if value > latest or latest == None:
        latest = value
    elif value < earliest or earliest == None:
        earliest = value

print earliest.strip('\n'), '\t',latest.strip('\n')
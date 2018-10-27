#!/usr/bin/env python2
import sys

prevKey = None
prevVal = None

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key == prevKey:
        if '.' in value:
            print prevVal, '\t', value
        else:
            print value, '\t', prevVal
    prevKey = key
    prevVal = value
#!/usr/bin/env python2
import sys

prevKey = None
prevVal = None

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key == prevKey:
        print prevVal, '\t', value
    prevKey = key
    prevVal = value
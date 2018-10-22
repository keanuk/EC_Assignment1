#!/usr/bin/env python2
import sys

actCount = 0

for line in sys.stdin:
    key, value = line.split('\t')
    actCount += int(value)

print actCount
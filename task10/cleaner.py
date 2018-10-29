#!/usr/bin/env python2
import sys

prevLine = None
count = 0

for line in sys.stdin:
    if line == prevLine:
        prevLine = line
        count += 1
    prevLine = line

print "There were ", count, " duplicates"

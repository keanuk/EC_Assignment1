#!/usr/bin/python2.7
import sys

prev_key = None 
lc = 0
wc = 0

for line in sys.stdin:

    line = line.strip()

    if line == 'word':
        wc += 1

    elif line == 'line':
        lc += 1
    
    else:
        print "How did that get in there?"

print wc, lc
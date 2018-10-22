#!/usr/bin/python2.7
import sys

lc = 0
wc = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key == 'word':
        wc += int(value)
    elif key == 'line':
        lc += int(value)

print wc, lc
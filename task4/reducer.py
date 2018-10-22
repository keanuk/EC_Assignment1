#!/usr/bin/env python2
import sys

prev_key = None

for line in sys.stdin:
    key, value = line.split('\t')
    if key != prev_key:
        print key
    prev_key = key

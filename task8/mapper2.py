#!/usr/bin/env python2
import sys

for line in sys.stdin:
    year, rating = line.strip().split('\t')
    print year, '\t', rating
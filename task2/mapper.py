#!/usr/bin/env python2
import sys

for i in range(len(sys.stdin.read().split()) - 1):
    print words[i] + "_" + words[i + 1], "\t", 1
    i += 1
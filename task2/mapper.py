#!/usr/bin/env python2
import sys

words = sys.stdin.read().strip().split()
for i in range(len(words) - 1):
    print words[i] + "_" + words[i + 1] + "\t", 1
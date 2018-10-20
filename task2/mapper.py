import sys

words = sys.stdin.read().split()

for i in range(len(words) - 1):
    print words[i] + "_" + words[i + 1], "\t", 1
    i += 1
#!/usr/bin/python3

for c in range(ord('a'), ord('z') + 1):
    if chr(c) != 'e' and chr(c) != 'q':
        print(chr(c), end='')

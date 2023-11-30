#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args=len(argv)-1
    sum = 0
    if num_args == 0:
        print(sum)
    else:
        i=1
        while i <= num_args:
            sum += int(argv[i])
            i += 1
        print(sum)
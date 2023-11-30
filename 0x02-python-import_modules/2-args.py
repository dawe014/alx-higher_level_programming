#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from sys import argv
num_args = len(argv) - 1
if len(argv)-1 == 0:
    print("{} arguments.".format(num_args))
elif len(argv)-1 == 1:
        print("{} argument: \n{}: {}".format(num_args,num_args,argv[1]))
else:
    print("{} arguments:".format(num_args))
    i=1
    while i <= num_args:
        print("{}: {}".format(i,argv[i]))
        i+=1
    
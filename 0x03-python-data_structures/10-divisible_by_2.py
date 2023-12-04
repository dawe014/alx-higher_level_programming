#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    num = len(my_list)
    lis = []
    for i in range(num):
        if my_list[i]%2==0:
            lis.append(True)
        else:
            lis.append(False)
    return lis
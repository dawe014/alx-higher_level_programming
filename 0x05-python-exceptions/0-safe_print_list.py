#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except:
        print()
        return count

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# result = safe_print_list(my_list, 3)
# print("Total elements printed:", result)

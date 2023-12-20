#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for a in range(list_length):
        r = None  # Initialize to None before the try block
        try:
            r = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(r if r is not None else 0)
    return result

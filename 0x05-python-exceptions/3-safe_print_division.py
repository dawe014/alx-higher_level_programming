#!/usr/bin/python3

def safe_print_division(a, b):
    result=None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        pass
        # return "none"
    finally:
        if result:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: {}".format("none"))
        
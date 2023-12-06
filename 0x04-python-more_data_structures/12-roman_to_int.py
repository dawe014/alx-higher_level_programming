#!/usr/bin/python3
def r_value(prmChar):
    r_list = [('I', 1), ('V', 5), ('X', 10),
                  ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
    for item in r_list:
        ch, value = item
        if (prmChar is ch):
            return value
    return None


def n_value(prmStr, prmI):
    if prmI + 1 < len(prmStr):
        return r_value(prmStr[prmI + 1])
    else:
        return None


def roman_to_int(roman_string):
    result = 0

    if (roman_string is None or isinstance(roman_string, str) is False):
        return result

    enum = enumerate(roman_string)
    for idx, ch in enum:
        cValue = r_value(ch)
        nValue = n_value(roman_string, idx)
        if nValue is None or cValue >= nValue:
            result += cValue
        else:
            result += (nValue - cValue)
            next(enum)
    return result
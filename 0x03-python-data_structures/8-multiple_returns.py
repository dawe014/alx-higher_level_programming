#!/usr/bin/python3
def multiple_returns(sentence):
    str_len=len(sentence)
    fchar=''
    lis=list(sentence)
    fchar=lis[0]
    tup=str_len,fchar
    return tup
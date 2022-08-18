# 6 kyu
# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python


def count(string):
    # out = {}
    # for c in string:
    #     if c in out:
    #         out[c] += 1
    #     else:
    #         out[c] = 1
    # return out
    return {c:string.count(c) for c in string}

count('aba')

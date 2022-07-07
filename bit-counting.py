# 6 kyu
# https://www.codewars.com/kata/526571aae218b8ee490006f4/solutions/python

n = 4
def count_bits(n):
    return bin(n).count('1')
    # return sum([int(i) for i in bin(n)[2:]])
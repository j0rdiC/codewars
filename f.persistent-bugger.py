# 6 kyu
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

from numpy import prod


def persistence(n):
    count = 0
    while len(str(n)) != 1:
        n = prod([int(i) for i in str(n)])
        count += 1
    return count
    

persistence(39)
persistence(999)
persistence(4)
persistence(25)

n = 39

x = prod([int(i) for i in str(n)])
y = prod([int(i) for i in str(x)])
# 6 kyu
# https://www.codewars.com/kata/541c8630095125aba6000c00/python


def digital_root(n):
    while len(str(n)) > 1:
        n = sum(int(i) for i in list(str(n)))
        # = sum(map(int, str(n)))
    return n

digital_root(16)
digital_root(942)
digital_root(132189)


def recursive(n):
    return n if n < 10 else recursive(sum(map(int,str(n))))

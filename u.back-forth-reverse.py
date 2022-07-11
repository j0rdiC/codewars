# 6 kyu 
# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python


def arrange(s):
    pass


a = [1,2]#, [1,2]),
b = [4, 3, 2]#, [4, 2, 3]),
c = [9, 7, -2, 8, 5, -3, 6, 5, 1]#, [9, 1, 5, 7, -2, 6, -3, 8, 5]),
d = [1]#,# [1]),
e = []#, []),
f = [2, 4, 3, 4]#,[2, 4, 3, 4]),


t = []

while len(c) > 1:
    t.append(c.pop(0))
    t.append(c.pop(-1))
    c.reverse()

for i, n in enumerate(c):
    i = i + 1
    t.append(c[i - 1])
    t.append(c[-i])
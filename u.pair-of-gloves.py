# PAIR OF GLOVES - 6 kyu
# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/python

from turtle import numinput


a = ["red","red"]#,1)
b = ["red","green","blue"]#,0)
c = ["gray","black","purple","purple","gray","black"]#,3)
d = []#,0)
e = ["red","green","blue","blue","red","green","red","red","red"]#,4)

def number_of_pairs(gloves):

    count = {key:0 for key in set(gloves)}
    for color in set(gloves):
        if color in count:
            count[color] += int(gloves.count(color))

    count = {}
    for color in gloves:
        if color in count:
            count[color] += 1
        else:
            count[color] = 0

    return sum([int(n/2) for n in count.values() if n >= 2])

number_of_pairs(c)

number_of_pairs(b)

number_of_pairs(a)
number_of_pairs(e)
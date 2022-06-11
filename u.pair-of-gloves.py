# PAIR OF GLOVES - 6 kyu
# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/python

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
    out = 0
    for i in count.values():
        if (i %2 != 0) and i > 1:
            out

    return count
    #return sum(count.values())

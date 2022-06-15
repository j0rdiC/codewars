# YOUR ORDER PLEASE - 6 kyu
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    n = sorted([int(x) for x in sentence if x.isdigit()], reverse=True)
    out = ''
    for c in sentence:
        if c.isdigit():
            out += str(n.pop())
        else:
            out += c
    return out

order("is2 Thi1s T4est 3a")#, "Thi1s is2 3a T4est")
order("4of Fo1r pe6ople g3ood th5e the2")#, "Fo1r the2 g3ood 4of th5e pe6ople")
order("")#, "")

sentence = "is2 Thi1s T4est 3a"
ls = sentence.split()
out = ''

for c in sentence:
    if c.isdigit():
        for w in ls:
            if c in w:
                out += w

dic = {}
for i, w in enumerate(ls):
    dic[str(i+1)] = w

for c in sentence:
    if c.isdigit():
        for i in dic.keys():
            if i == c:
                dic[i] =


index = [x for x in sentence if x.isdigit()]
n = sorted([int(x) for x in sentence if x.isdigit()], reverse=True)


if c == 
for c in sentence:
    if c.isdigit():
        out += str(n.pop())
    else:
        out += c


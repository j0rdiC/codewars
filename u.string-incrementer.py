# 5 kyu
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python



def increment_string(strng):
    w = ''
    n = ''
    for c in strng:
        if c.isdigit():
            n += c
        else:
            w += c
    return f"{w}{'0'*n.count('0') if int(n) > 0 else '0'*(n.count('0')-1)}{int(n) + 1}" if n else f"{strng}1"


increment_string("foo")# , "foo1")
increment_string("foobar001")# , "foobar002")
increment_string("foobar1")# , "foobar2")
increment_string("foobar00")# , "foobar01")
increment_string("foobar99")# , "foobar100")
increment_string("foobar099")# , "foobar100")
increment_string("")#, " 1")


test = 'foobar001'

w = ''
n = ''
for c in test:
    if c.isdigit():
        n += c
    else:
        w += c

if n.startswith('0'):

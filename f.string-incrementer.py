# 5 kyu 
#  https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python


from curses.ascii import isdigit


def increment_string(strng):
    w = ''
    n = ''
    for c in strng:
        if c.isdigit():
            n += c
        else:
            w += c
    if len(n) > 1
    return f"{w}{int(n) + 1}" if n else f"{strng}1"


increment_string("foobar001")#, "foobar002")
increment_string("foobar1")#, "foobar2")
increment_string("foobar00")#, "foobar01")
increment_string("foobar99")#, "foobar100")
increment_string("foobar099")#, "foobar100")
increment_string("")#, "1")


test = 'foobar001'

n = ''
w = ''
for c in test:
    if c.isdigit():
        n += c
    else:
        w += c

print(f"{w}{int(n) +1}") if n else print(f"{test}1")
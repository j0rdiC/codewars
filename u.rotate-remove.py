# ROTATE, REMOVE, RETURN - 5 kyu
# https://www.codewars.com/kata/57dab71714e53f4bc9000310/train/python

test = [[3,5,8,4,2],
        [1,9,2,3,8],
        [4,6,7,2,2],
        [7,5,5,5,5],
        [6,5,3,8,1]]# 4)


out = []
new = []

for i in range(len(test[0])):
    out.append([ls.pop() for ls in test])

for ls in out:
    ls.remove(min(ls))
    ls.remove(max(ls))

for i in range(len(out[0])):
    new.append([ls.pop() for ls in out])

out = []
for ls in new:
    ls.remove(min(ls))
    ls.remove(max(ls))

for i in range(len(new[0])):
    out.append([ls.pop() for ls in new])

for ls in out:
    ls.remove(min(ls))
    ls.remove(max(ls))

new = []
for i in range(len(out[0])):
    new.append([ls.pop() for ls in out])

for ls in new:
    ls.remove(min(ls))
    ls.remove(max(ls))
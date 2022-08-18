# PAIR OF GLOVES - 6 kyu
# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/python



a = ["red","red"]#,1)
b = ["red","green","blue"]#,0)
c = ["gray","black","purple","purple","gray","black"]#,3)
d = []#,0)
e = ["red","green","blue","blue","red","green","red","red","red"]#,4)

def short(gloves):
    return sum(gloves.count(color)//2 for color in set(gloves))

short(e)

def number_of_pairs(gloves):
    count = {}
    for color in gloves:
        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    return sum([int(n/2) if n%2==0 else int(((n-(n%2)))/2)for n in count.values() if n >= 2])

number_of_pairs(c)

number_of_pairs(b)

number_of_pairs(a)
number_of_pairs(e)


test = ["red","green","blue","blue","red","green","red","red","red"]#,4)

count = {}
for color in test:
    if color in count:
        count[color] += 1
    else:
        count[color] = 1

for key, value in count.items():
    if value%2 != 0:
        count[key] -= value % 2

sum([int(n/2) if n %2 == 0 else int((n - (n % 2))/2) for n in count.values() if n >= 2])

[int(n/2) if n %2 == 0 else int((n - (n % 2))/2) for n in count.values() if n >= 2]

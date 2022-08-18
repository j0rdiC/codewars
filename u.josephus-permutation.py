# 5 kyu
# https://www.codewars.com/kata/5550d638a99ddb113e0000a2


from itertools import cycle


def josephus(items, k):
    out = []
    while items:
        for i, n in enumerate(items):
            if i+k > len(items):
                out.append(items.pop((i+(k-1)-len(items))))
            else:
                out.append(items.pop(i+(k-1)))
    return out


josephus([1,2,3,4,5,6,7,8,9,10],1)#,[1,2,3,4,5,6,7,8,9,10])
josephus([1,2,3,4,5,6,7,8,9,10],2)#,[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
josephus(["C","o","d","e","W","a","r","s"],4)#,['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
josephus([1,2,3,4,5,6,7],3)#,[3, 6, 2, 7, 5, 1, 4])
josephus([],3)#,[])


test = [1,2,3,4,5,6,7,8,9,10]
k = 2
circle = cycle(test)

out = []
while test:
    for i, n in enumerate(test):
        if i+k > len(test):
            out.append(test.pop((i+(k-1))-len(test)))
        else:
            out.append(test.pop(i+(k-1)))
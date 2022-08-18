# 5 kyu
# https://www.codewars.com/kata/57591ef494aba64d14000526/train/python


def john(n):
    katas = n - ann(john(n-1))
    return [n - ann(john(n-1)) for n in range(n)]
    
def ann(n):
    katas = n - john(ann(n-1))
    return []
    
def sum_john(n):
    return 0
    
def sum_ann(n):
    return 0


john(11)# [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6)#, [1, 1, 2, 2, 3, 3]
sum_john(75)#, 1720
sum_ann(115)#, 4070
#  5 kyu
# https://www.codewars.com/kata/5314b3c6bb244a48ab00076c/train/python


def luck_check(string):
    if len(string) % 2 != 0:
        string = [c for c in string]
        string.pop(len(string)//2)
        string = ''.join(string)
    return sum([int(n) for n in string[:len(string)//2]]) == sum([int(n) for n in string[len(string)//2:]])


luck_check('683179') # True
luck_check('683000') # False
luck_check('6835179')


re = '6835179'
if len(re) % 2 != 0:
    a = [c for c in re]
    a.pop(len(a)//2)
    x = ''.join(a)
    x
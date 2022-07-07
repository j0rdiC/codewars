# 6 kyu
# https://www.codewars.com/kata/525f50e3b73515a6db000b83/solutions/python

def create_phone_number(n):
    l = ''.join(str(i) for i in n)
    return f"({l[:3]}) {l[3:6]}-{l[6:]}"
    
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n) # UNPACK



n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
l = ''.join(str(i) for i in n)

print(f"({l[:3]}) {l[3:6]}-{l[6:]}")

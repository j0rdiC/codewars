# FIND THE PARITY OUTLIER
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    out = {
        'even': [],
        'odd': []
    }
    for n in integers:
        if n % 2 == 0:
            out['even'].append(n)
        else:
            out['odd'].append(n)
    return (out['even'][0]) if len(out['even']) == 1 else out['odd'][0]


find_outlier([2, 4, 6, 8, 10, 3])#, 3)
find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])#, 11)
find_outlier([160, 3, 1719, 19, 11, 13, -21])#, 160)


def  find_cleaner(integers):
    odd = [n for n in integers if n %2 != 0]
    even = [n for n in integers if n %2 == 0]
    return odd[0] if len(odd) < len(even) else even[0]
 
find_cleaner([2, 4, 6, 8, 10, 3])#, 3)
find_cleaner([2, 4, 0, 100, 4, 11, 2602, 36])#, 11)
find_cleaner([160, 3, 1719, 19, 11, 13, -21])#, 160)
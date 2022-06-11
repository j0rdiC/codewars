# UNIQUE IN ORDER - 6 kyu
# https://www.codewars.com/kata/54e6533c92449cc251001667

iter = 'AAAABBBCCDAABBB' # , ['A','B','C','D','A','B'])

def unique_in_order(iterable):
    out = []
    for i in iterable:
        if out and (out[-1] == i):
            out.pop()
        out.append(i)
    return out                

print(unique_in_order(iter))

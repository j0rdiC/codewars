# SUMS OF PARTS - 6 kyu
# https://www.codewars.com/kata/5ce399e0047a45001c853c2b

def parts_sums(ls):
    out = []
    for i in range(len(ls)):
        out.append(sum(ls))
        ls.pop(0)
    out.append(0)
    return out



parts_sums([])#, [0])
parts_sums([0, 1, 3, 6, 10])#, [20, 20, 19, 16, 10, 0])
parts_sums([1, 2, 3, 4, 5, 6])#, [21, 20, 18, 15, 11, 6, 0])
parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358])#, [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0])

# OPTIMIZE CODE
ls = [1, 2, 3, 4, 5, 6]
out = []
for i in range(len(ls)):
    out.append(sum(ls))
    ls.pop(i)




# Max & min dont work properly with strings, always use integers for these purposes
def high_and_low(numbers):
    ls = [int(n) for n in numbers.split()]
    return f"{max(ls)} {min(ls)}"

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")#, "42 -9"


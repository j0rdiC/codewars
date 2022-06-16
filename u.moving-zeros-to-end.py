# MOVING ZEROS TO THE END - 5 kyu
# https://www.codewars.com/kata/52597aa56021e91c93000cb0


def move_zeros(array):
    for n in array:
        if n == 0:
            array.remove(n)
            array.append(n)
    return array
    # arr = array
    # for i, n in enumerate(array):
    #     if n == 0:
    #         print(i)
    #         arr.pop(i)
    #         arr.append(0)
    # return arr
    count = 0
    out = []
    for n in array:
        if n == 0:
            count += 1
        else:
            out.append(n)
    for i in range(count):
        out.append(0)
    return out


    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
isinstance(1, bool)

move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])#,[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])#,[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


test = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

count = 0
out  = []
for i, n in enumerate(test):
    if n == 0:
        count += 1
    else:
        out.append(n)
for i in range(count):
    out.append(0 * count)

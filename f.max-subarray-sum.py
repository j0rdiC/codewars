# 5 kyu
# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python


def max_sequence(arr):
    ls = [0 for i in range(len(arr))]
    ls[0] = arr[0]

    for i in range(1, len(arr)):
        ls[i] = max(ls[i-1] + arr[i], arr[i])
    print(ls)
    return max(ls)



max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) #, 6)

test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ls = [0 for i in range(len(test))]
ls[0] = test[0]

for i in range(1, len(test)):
    ls[i] = max(ls[i-1] + test[i], test[i])
print(ls)
print(max(ls))



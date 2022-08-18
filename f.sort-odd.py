# 6 kyu
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python



def sort_array(source_array):
    odd = sorted([n for n in source_array if n%2 != 0], reverse=True)
    return [n if n%2 == 0 else odd.pop() for n in source_array]


sort_array([5, 3, 2, 8, 1, 4])#, [1, 3, 2, 8, 5, 4]) f



test = [5, 3, 2, 8, 1, 4]


odd = sorted([n for n in test if n%2 !=0], reverse=True)
out = [n if n%2 == 0 else odd.pop() for n in test]


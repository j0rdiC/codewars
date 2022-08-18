# 6 kyu
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    l = 0
    r = 0
    for i in range(len(arr)):
        l = sum(arr[i:])
        r =  sum(arr[])




find_even_index([1,2,3,4,3,2,1])#,3)
find_even_index([1,100,50,-51,1,1])#,1,)
find_even_index([1,2,3,4,5,6])#,-1)
find_even_index([20,10,30,10,10,15,35])#,3)
find_even_index([20,10,-80,10,10,15,35])#,0)
find_even_index([10,-80,10,10,15,35,20])#,6)
find_even_index(list(range(1,100)))#,-1)
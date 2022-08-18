# YOUR ORDER PLEASE - 6 kyu
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    def find(w):
        return [int(n) for n in w if n.isdigit()]
    return ' '.join(sorted(sentence.split(), key=find))


order("is2 Thi1s T4est 3a")#, "Thi1s is2 3a T4est")
order("4of Fo1r pe6ople g3ood th5e the2")#, "Fo1r the2 g3ood 4of th5e pe6ople")
order("")#, "")


sentence = "is2 Thi1s T4est 3a"

def find(w):
    return [int(n) for n in w if n.isdigit()]
a = sentence.split()
out = a.sort(key=find)

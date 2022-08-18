# 5 kyu
# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python


def anagrams(word, words):
    out = []
    for w in words:
        if len(w) == len(word):
            match = ''
            for c in w:
                if w.count(c) == word.count(c):
                    match += c
            out.append(match)
    return [x for x in out if len(x) == len(word)]
    
            
#! sorted()
def better(word, words):
    return [x for x in words if sorted(x) == sorted(word)]



anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) # , ['aabb', 'bbaa'])
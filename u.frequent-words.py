# 4 kyu
# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python


from string import whitespace
from re import findall

def top_3_words(text):
    punctuation = """!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    count = {}
    for word in text.split():
        word = word.lower().strip(punctuation)
        if word:
            if word in count:
                count[word] += 1
            else:
                count[word.lower()] = 1
    top = sorted(count.values(), reverse=True)[:3]
    return [list(count.keys())[list(count.values()).index(n)] for n in top]
    #return [key for key, value in count.items() if value in sorted(count.values(), reverse=True)[:3]]
        

top_3_words("a a a  b  c c  d d d d  e e e e e")#, ["e", "d", "a"])
top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")#, ["e", "ddd", "aa"])
top_3_words("  //wont won't won't ")#, ["won't", "wont"])
top_3_words("  , e   .. ")#, ["e"])
top_3_words("  ...  ")#, [])
top_3_words("  '  ")#,# [])
top_3_words("  '''  ")#, [])
top_3_words("""In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.""")#, ["a", "of", "on"])



punctuation = """!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ """
test = "a a a  b  c c  d d d d  e e e e e"

test1 = "  , e   .. "
test2 = "  //wont won't won't "

test3 = "  ...  "


def clean(word):
    return word.strip(punctuation)
count = {}
for word in test3.split():
    w = clean(word)
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

top = sorted(count.values(), reverse=True)[:3]
out = [key for key, value in count.items() if value in sorted(count.values(), reverse=True)[:3]]

[list(count.keys())[list(count.values()).index(n)] for n in top]



# COUNT THE SMILEY FACES - 6 kyu
# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python


def count_smileys(arr):
    opt = ':) :D :-) :~) :-D :~D'
    valid = {key:0 for key in f"{opt} {opt.replace(':', ';')}".split()}

    for i in arr:
        if i in valid:
            valid[i] += 1

    return sum(valid.values())

count_smileys([])#, 0)
count_smileys([':D',':~)',';~D',':)'])#, 4)
count_smileys([':)',':(',':D',':o',':;'])#, 2)
count_smileys([';]', ':[', ';*', ':$', ';-D'])#, 1)


from re import findall

def count_regex(arr):
    return len(findall(r"[:;][-~]?[)D]", " ".join(arr)))

count_regex([])#, 0)
count_regex([':D',':~)',';~D',':)'])#, 4)
count_regex([':)',':(',':D',':o',':;'])#, 2)
count_regex([';]', ':[', ';*', ':$', ';-D'])#, 1)


test = [':D',':~)',';~D',':)']#, 4)
x = findall(r"[:;][-~]?[)D]", " ".join(test))
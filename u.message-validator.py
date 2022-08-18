# 6 kyu

from re import findall

def is_a_valid_message(message):
    if message[-1].isdigit():
        return False
    else:
        num = findall(r"\d{1,3}", message)
        words = findall(r"[a-z]+", message)

        count = 0
        for i, w in enumerate(words):
            if len(w) == int(num[i]):
                count += 1
        return count == len(words)


    


is_a_valid_message("3hey5hello2hi")#, True)


test = "3hey5hello2hi13puta5"
num = findall(r"\d{1,3}[a-z]+", test)
words = findall(r"[a-z]+", test)

count = 0
for i, w in enumerate(words):
    if len(w) == int(num[i]):
        count += 1


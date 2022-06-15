# ROT 13 - 6 kyu
# 

from string import ascii_lowercase, ascii_uppercase, punctuation, whitespace, digits 

def rot13(message):
    alph_low = ascii_lowercase
    alph_up = ascii_uppercase
    other = punctuation + whitespace + digits
    out = ""
    for c in message:
        if c not in other:
            if c in alph_low:
                i = alph_low.find(c)
                out += alph_low[(i - 13) % len(alph_low)]
            else:
                i = alph_up.find(c)
                out += alph_up[(i - 13) % len(alph_low)]
        else:
            out += c
    return out

rot13('test')
rot13('Test')
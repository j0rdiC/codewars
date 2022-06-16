# SIMPLE PIG LATIN - 5 kyu
# https://www.codewars.com/kata/520b9d2ad5c005041100000f

from string import punctuation

def pig_it(text):
    # out = []
    # for w in text.split():
    #     if w in other:
    #         out.append(w)
    #     else:
    #         out.append(w[1:] + w[0] + 'ay')
    # return ' '.join(out)

                                        #! Poner el 'if' antes del 'for' si queremos usar un 'else'
    return ' '.join([w[1:] + w[0] + 'ay' if w not in punctuation else w for w in text.split()])



pig_it('Pig latin is cool')#,'igPay atinlay siay oolcay')
pig_it('This is my string')#,'hisTay siay ymay tringsay'"Quis custodiet ipsos custodes ?"
pig_it("Quis custodiet ipsos custodes ?")# 'uisQay ustodietcay psosiay ustodescay ?')
a = 'Pig latin is cool'

other = punctuation

' '.join([w[1:] + w[0] + 'ay' if w not in other else w for w in a.split()])
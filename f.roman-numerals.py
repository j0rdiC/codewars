# 4 kyu
# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python


ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

class RomanNumerals:

    # SOLUTION 1. CLEAN BUT SPECIFIC TO PYTHON LANGUAGE
    def to_roman(val):
        s = ''
        while val != 0:
            for key, value in ROMANS.items():
                while val % value != val:
                    val -= value
                    s += key
            return s

    def from_roman(roman_num):
        s = 0
        for key, value in ROMANS.items():
            while roman_num.startswith(key):
                roman_num = roman_num[len(key):]
                s += value
        return s
        

    # SOLUTION 2
    def to_roman(val):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        s = ''
        while val:
            div = val // num[i]
            val %= num[i]
            while div:
                s += sym[i]
                div -= 1
            i -= 1
        return s

    def from_roman(roman_num):
        parser = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }

        i = 0
        n = 0
        while i < len(roman_num):
            if i+1 < len(roman_num) and roman_num[i:i+2] in parser:
                n += parser[roman_num[i:i+2]]
                i += 2
            else:
                n += parser[roman_num[i]]
                i += 1
        return n       



RomanNumerals.to_roman(1000)#, 'M', '1000 should == "M"')
RomanNumerals.to_roman(4)#, 'IV', '4 should == "IV"')
RomanNumerals.to_roman(1)#, 'I', '1 should == "I"')
RomanNumerals.to_roman(1990)#, 'MCMXC', '1990 should == "MCMXC"')
RomanNumerals.to_roman(2008)#, 'MMVIII', '2008 should == "MMVIII"')


RomanNumerals.from_roman('XXI')#, 21, 'XXI should == 21')
RomanNumerals.from_roman('I')#, 1, 'I should == 1')
RomanNumerals.from_roman('IV')#, 4, 'IV should == 4')
RomanNumerals.from_roman('MMVIII')#, 2008, 'MMVIII should == 2008')
RomanNumerals.from_roman('MDCLXVI')#, 1666, 'MDCLXVI should == 1666')





# TESTING
num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

# FROM NUM
i = 12
val = 465

out = ''
while val:
    div = val // num[i]
    val %= num[i]

    while div:
        out += sym[i]
        div -= 1
    i -= 1


# FROM SYM
a = 'XXI'

ROMAN = {
    'I':1,
    'IV':4,
    'V':5,
    'IX':9,
    'X':10,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'CD':400,
    'D':500,
    'CM':900,
    'M':1000
}

i = 0
n = 0
while i < len(a):
    if i+1<len(a) and a[i:i+2] in ROMAN:
        n+=ROMAN[a[i:i+2]]
        i+=2
    else:
        #print(i)
        n+=ROMAN[a[i]]
        i+=1




# CLEAN

def to_roman(n):
    s = ''
    while n != 0:
        for key, value in ROMANS.items():
            while n % value != n:
                n -= value
                s += key
        return s

def from_roman(r):
    s = 0
    for key, value in ROMANS.items():
        while r.startswith(key):
            r = r[len(key):]
            s += value
    return s
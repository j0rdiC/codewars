#!/bin/python3

def disemvowel(string_):
    vowels = 'aAeEiIoOuU'
    return "".join([l for l in string_ if not l in vowels])

print(disemvowel("This website is for losers LOL!"))

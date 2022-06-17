# VALID PARENTHESIS - 5 kyu
# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    l, r = '(', ')'
    return True if string.count(l) == string.count(r) else False
    


test = "(())((()())())"
test_1 = ")(()))"

test.count('(')
test.count(')')

test_1.count('(')
test_1.count(')')


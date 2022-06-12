# FIRST NON REPEATING CHARACTER - 6 kyu
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    out = [string[i] for i, c in enumerate(string.lower()) if string.lower().count(c) == 1]
    return out[0] if string and out else ''

#test.it('should handle simple tests')
first_non_repeating_letter('a')#, 'a')
first_non_repeating_letter('stress')#, 't')
first_non_repeating_letter('moonmen')#, 'e')

#test.it('should handle empty strings')
first_non_repeating_letter('')#, '')

#test.it('should handle all repeating strings') 
first_non_repeating_letter('abba')#, '')
first_non_repeating_letter('aa')#, '')

#test.it('should handle odd characters')
first_non_repeating_letter('~><#~><')#, '#')
first_non_repeating_letter('hello world, eh?')#, 'w')

#test.it('should handle letter cases')
first_non_repeating_letter('sTreSS')#, 'T')
first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog')# ','

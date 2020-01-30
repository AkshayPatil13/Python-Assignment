# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

import re

def count_digits_and_letters():
    """
        This function counts the number of letters and digits in given sentence or string.
        
        INPUT : a sentence or string.
        
        OUTPUT : count of letters and digits in given sentence.
    """
    
    letters = 0
    digits = 0
    sentence = raw_input('Enter a sentence : ')
    for character in re.sub('[^A-Za-z0-9]+', '',sentence):
        if character.isdigit():
           digits += 1
        else:
            letters += 1
            
    print 'no. of letters : ',letters   
    print 'no. of digits : ',digits
        
count_digits_and_letters()

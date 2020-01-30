# Question 6:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

import re

def count_upper_and_lower_case_letters():
     """
        This function counts the number of upper and lower case letters in given sentence or string.
        
        INPUT : a sentence or string.
        
        OUTPUT : count of upper and lower case letters in given sentence.
    """
    
    upper_count = 0
    lower_count = 0
    sentence = raw_input('Enter a sentence : ')
    for character in re.sub('[^A-Za-z0-9]+', '',sentence):
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1
        else:
            pass
            
    print 'no. of upper case letters : ',upper
    print 'no. of lower case letters : ',lower
    
count_upper_and_lower_case_letters()

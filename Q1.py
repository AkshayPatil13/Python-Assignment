# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


import math

def calculate_square_root():
    """
        This function calculates the square root using the formula [(2 * C * D)/H].
        
        INPUT : list of values of D in a comma-separated sequence.
        
        OUTPUT : list of calculated square root values
    """
    
    C = 50
    H = 30
    result = []
    user_input = map(int,raw_input('Enter values of D comma seperated : ').split(','))

    for value in user_input:
     result.append(int(round(math.sqrt((2 * C * value)/H))))

    print 'OUTPUT - ',str(result)[1:-1]

calculate_square_root()

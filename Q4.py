# Question 4:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010


def check_divisibility():
    """
        This function checks whether the given binary number is divisible by 5.
        
        INPUT : list of 4 digit binary numbers in a comma separated sequence.
        
        OUTPUT : list of binary numbers divisible by 5.
    """
    
    result = []
    binary_numbers = raw_input('Enter 4 digit binary numbers comma seperated :').split(',')
    for number in binary_numbers:
        if int(int(number,2)) % 5 == 0:
            result.append(number)
            
    print result
           
check_divisibility()

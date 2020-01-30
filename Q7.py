# Question 7:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re

def validate_password():
    """
        This function checks whether the individual password value of the given list matches the password criteria.
        
        INPUT : list of password values in a comma seperated sequence.
        
        OUTPUT : list of password values that matches the password criteria.
    """
    
    result = []
    count = 0
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,12}$"
    passwords = raw_input('Enter passwords in comma seperated sequence : ').split(',')
    for password in passwords:
        if re.match(pattern,password):
            result.append(password)
            count += 1
    
    if(count > 0):
        print 'list of valid password : ',result
    else:
        print 'none of the input password matches the password criteria.'

validate_password()


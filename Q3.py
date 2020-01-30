# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


def sort_words_alphabetically():
    """
        This function sorts the list of words alphabetically.
        
        INPUT : list of words in a comma separated sequence.
        
        OUTPUT : alphabetically sorted list of words.
    """
    
    input_strings = raw_input('Enter list of words to be sorted comma seperated : ').split(',')
    print sorted(input_strings)
    
sort_words_alphabetically()

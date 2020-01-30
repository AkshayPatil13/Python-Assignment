# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


def generate_matrix():
    """
        This function generates an array of dimension rows * columns where value of each cell is 
        product of its corresponding row and column.
        
        INPUT : number of rows and columns in a comma-separated sequence.
        
        OUTPUT : list containing the generated array.
    """
    
    rows,columns = map(int, raw_input('Enter no. of rows and columns of matrix comma seperated : ').split(','))
    matrix = []
    for i in xrange(rows):
        row = []
        for j in xrange(columns):
            row.append(i*j)
        
        matrix.append(row)
        
    print 'OUTPUT : ',matrix
    
generate_matrix()

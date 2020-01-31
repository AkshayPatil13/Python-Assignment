# Question 8:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class Check_numbers_divisible_by_7:
    """
        This class contains a generator which iterates the numbers which are divisible by 7 between a given range 0 and n.
    """
    
    def __init__(self,num_range):
        """
            This function acts as a constructor of class and creates an object for us.
        """
        
        self.num_range = num_range
        
        
    def generator_to_check_divisibility(self):
        """
            This is a generator function that generates a range between 0 to given number_range.
            
            INPUT : number range.
            
            OUTPUT : numbers divisible by 7
        """
        
        for number in range(self.num_range):
            if number % 7 == 0:
                yield number
            else:
                continue
                
                
def main():
    """
        This is the main function from where the execution of program starts.
        It  is responsible for taking user inputs and calling different methods of class.
    """
    
    number_range = raw_input('Enter range : ')
    obj  = Check_numbers_divisible_by_7(int(number_range))
    numbers_divisible = obj.generator_to_check_divisibility()
    for number in numbers_divisible:
        print number
       
        
if __name__ == "__main__":
    main()

#importing math library
import math

class calculator:
     
    #function for addition
    def add(self, number_1, number_2):
        Sum = number_1+number_2
        return Sum
      
    #function for subtraction
    def subtract(self, number_1, number_2):
        Diff = number_1-number_2
        return Diff
    
    #function for multiplication
    def multiply(self, number_1, number_2):
        Prod = number_1*number_2
        return Prod
    
    #function for division
    def division(self, number_1, number_2):
        Quot = number_1/number_2
        return Quot
    
    #function for exponent
    def exponent(self, number_1, number_2):
        exponent_val = math.pow(number_1, number_2)
        return exponent_val
    
    #function for Nth root
    def nth_root(self, number_1, number_2):
        nthRoot_val = math.pow(number_1, 1/number_2)
        return nthRoot_val

choice = 'yes'               #initializing choice to run the program
calc = calculator()          #object calc with class calculator


#greeting message
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~( ´ ▽ ` )ﾉ WELCOME TO DIGICALC ( ´ ▽ ` )ﾉ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

#input for operation choice
operation = int(input('\nPlease enter your choice of operation:\n 1)Addition\n 2)Subtraction\n 3)Multiplication\n 4)Division\n 5)Exponent\n 6)Nth root\n'))

#while loop
#contains all the conditions and applications of the functions from class calculator
while (choice == 'yes'):
     
    #if loop for invalid operation choice
    if(operation>6 or operation<0):
        operation=int(input('PLEASE ENTER A VALID OPERATION CHOICE'))
    
    #elif loop for outputs of the calculator for the first 5 operation choices
    elif(operation in range(1,7)):
        number_1 = float(input('\nENTER THE FIRST NUMBER: '))  #asks for the first number 
        number_2 = float(input('ENTER THE SECOND NUMBER/Nth ROOT VALUE/EXPONENT VALUE BASED ON THE CHOICE OF OPERATION: '))  #asks for the second number
        
        #if loop for first choice, addition
        if (operation == 1):
            add_val = calc.add(number_1, number_2)
            print('Addition: {} + {} = {}\n'.format(number_1, number_2, add_val))
        
        #if loop for second choice, subtraction
        if (operation == 2):
            diff_val = calc.subtract(number_1, number_2)
            print('Subtraction: {} - {} = {}\n'.format(number_1, number_2, diff_val))
        
        #if loop for third choice, multiplication
        if (operation == 3):
            product_val = calc.multiply(number_1, number_2)
            print('Multiplication: {} * {} = {}\n'.format(number_1, number_2, product_val))
        
        #if loop for fourth choice, division
        if (operation == 4):
            try:     
                quotient_val = calc.division(number_1, number_2)
                print('Division: {} / {} = {}\n'.format(number_1, number_2, quotient_val))
            except ZeroDivisionError:
                print('INVALID DIVISION. DIVISION BY 0\n')
                
        #if loop for fifth choice, exponent     
        if (operation == 5):
            exp_val = calc.exponent(number_1, number_2)
            print('Exponent: {} ^ {} = {}\n'.format(number_1, number_2, exp_val))
          
        #if loop for sixth choice, Nth root
        if (operation == 6):
            nroot_val = calc.nth_root(number_1, number_2)
            print('Root: {}√{} = {}\n'.format(number_2, number_1, nroot_val))
                
    #asks user if they want to continue the program or not    
    choice = input('DO YOU WANT TO PERFORM MORE CALCULATIONS? ENTER yes OR no.\n')
    
    #checks if the choice entered is yes or no
    while(choice not in ['yes','no']):
        choice = input('INVALID ANSWER. ANSWER USING yes OR no\n')

    #if loop for when choice is yes    
    #continues the calculations
    if(choice=='yes'):
        operation = int(input('\nPlease enter your choice of operation:\n 1)Addition\n 2)Subtraction\n 3)Multiplication\n 4)Division\n 5)Exponent\n 6)Nth root\n'))

                  
#if loop for when choice is no
#ends the interaction
if (choice == 'no'):
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~♡♡ Thank you for using DigiCalc ♡♡~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')        
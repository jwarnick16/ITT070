# Name: Justine
# Date: 4/15/2024
# Program Name: 14-1
# Description: Object-oriented programming
# 
# Create a program where the user enters two numbers and, using OOP, the program should:
# 
# 1. Add the numbers together.
# 
# 2. Subtract the second number from the first.
# 
# 3. Multiply the numbers together.
# 
# 4. Divide the first number by the second.
# 
# The text should be formatted nicely
# There should be appropriate descriptions.
# There should be some basic directions for the user 
# There will be one function for each math operation for a total of 4 functions
# The program will use the template that I showed you in class.
# Programs will be submitted as runnable .py files. 


# Functions --------------------------------------
class Calc():                                           # Creating class
    def __init__(self, a, b):                           
        self.a = a                                      # Defining Attributes
        self.b = b                                      # Defining Attributes

    def add(self):                                      # Creating Method - Addition
        return self.a + self.b
    def sub(self):                                      # Creating Method - Subtraction
        return self.a - self.b
    def mul(self):                                      # Creating Method - Multiplication
        return self.a * self.b
    def div(self):                                      # Creating Method - Division with remainders
        first = self.a // self.b                        # Division
        second = self.a%self.b                          # Remainders
        return (f"{first}, remainder of {second}")



# Variables --------------------------------------
response = 0

# Main -------------------------------------------
num1 = (int(input("Enter the first number: ")))         # User Input
num2 = (int(input("Enter the second number: ")))        # User Input    

equation = Calc(num1, num2)                             # Calling class

while response != 6:                                    # Creating While Loop to loop until user instructs it to stop
    print("\nPlease select an operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Start Over "
                         "\n6. Exit \n")                
    response = int(input("Please select an option: "))  # Allowing user to choose output
    if response == 1:
        print(f"{num1} + {num2} = ", equation.add())    # Calling Addition Method
    elif response == 2:
        print(f"{num1} - {num2} = ", equation.sub())    # Calling Subtraction Method
    elif response == 3:
        print(f"{num1} * {num2} = ", equation.mul())    # Calling Mutliplication Method
    elif response == 4:
        print(f"{num1} / {num2} = ", equation.div())    # Calling Division Method
    elif response == 5:                                 # Allowing User to Start Over
        num1 = (int(input("Enter the first number: ")))
        num2 = (int(input("Enter the second number: ")))
    elif response == 6:                                 # Exits loop/program
        print("Exiting Program")
        break

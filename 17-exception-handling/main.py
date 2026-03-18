"""
Experiment: 17
Program: Exception Handling
Author: Abhishek Choudhery
Description: Python program to handle division by zero using exception handling.
"""

try:
    num1 = int(input("Enter the numerator (number to be divided): "))
    num2 = int(input("Enter the denominator (number to divide by): "))
    
    result = num1 / num2

except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Program execution finished.")
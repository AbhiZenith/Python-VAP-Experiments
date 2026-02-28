"""
Experiment: 05
Program: Largest of Three numbers
Author: Abhishek Choudhery
Description: Python program to find the largest of three numbers using conditional statements.
"""

# Taking three inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third numbere: "))

# Logic to find the largest
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num3):
    largest = num2
else:
    largest = num3
    
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

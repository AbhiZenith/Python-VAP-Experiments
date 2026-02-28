"""
Experiment: 06
Program: Menu-driven Calculator
Author: Abhishek Choudhery
Description: Python program to develop a menu-driven calculator using if-elif-else.
"""

print("--- Simple Calculator Menu ---")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Mutliplication (*)")
print("4. Division (/)")

# Taking choice from the user
choice = input("Enter your choice (1/2/3/4): ")

# Taking the numbers to calculate
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Logic for the operations
if choice == '1':
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == '4':
    # Checking for Division by Zero
    if num2 == 0:
        print("Error! Division by zero is not allowed")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid input! Please choose a number between 1 and 4.")    
"""
Experiment: 08
Program: Prime Number
Author: Abhishek Choudhery
Description: Python program to check whether a number is prime or not.
"""

# Taking input from the user
num = int(input("Enter a number to check if it is prime or not: "))
count = 0
if num < 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(1, num +1):
        if (num % i) == 0:
            count +=1
    
    if count > 2:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")


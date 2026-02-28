"""
Experiment: 07
Program: Fibonacci Series
Author: Abhishek Choudhery
Description: Python program to print Fibonacci series up to N terms using loops.
"""

n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series: ")
for i in range(n):
    print(a, end = " ")
    a, b = b, a + b
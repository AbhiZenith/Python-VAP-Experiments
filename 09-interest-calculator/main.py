"""
Experiment: 09
Program: Simple Interest and Compound Interest
Author: Abhishek Choudhery
Description: Python program to calculate simple interest and compound
"""

# Taking inputs
p = float(input("Enter the Principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years) "))

# 1. Calculate Simple Interest
si = (p * r * t) / 100

# 2. Calculate Compound Interest
# Formula: A = P(1 + r / n) ^ nt
# For annual compounding: A = P(1 + r / 100) ^ t
amount = p * (pow((1 + r / 100), t))
ci = amount - p

print(f"Simple Interest: {si:.2f}")
print(f"Compound Interest: {ci:.2f}")


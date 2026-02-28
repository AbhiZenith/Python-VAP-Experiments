"""
Experiment: 14
Program: Remove Duplicated
Author: Abhishek Choudhery
Description: Python program to remove duplicate elements from a list using sets.
"""

# List with duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]

# Remove duplcates
unique_list = list(set(my_list))

# Display result
print(unique_list)
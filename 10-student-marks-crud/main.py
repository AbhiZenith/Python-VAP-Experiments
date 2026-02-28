"""
Experiment: 10
Program: Student Marks CRUD Operations
Author: Abhishek Choudhery
Description: Python program to perform CRUD operations on a list of student marks.
"""

# Initial List
marks = [85, 90, 88]

# READ
print(f"Current Marks: {marks}")

# CREATE
marks.append(99)
print(f"After Adding: {marks}")

# Update
marks[0] = 95
print(f"After Updating: {marks}")

# DELETE
marks.remove(88)
print(f"After Deleting 88: {marks}")
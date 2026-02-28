"""
Experiment: 12
Program: Employee Dictionary
Author: Abhishek Choudhery
Description: Python program to search employee details using employee ID.
"""

employees = { 
            101: "X",
            102: "y",
            103: "z",
            }

id = int(input("Enter Employee ID to search: "))

if id in employees:
    print(f"Record Found: Name: {employees[id]}")
else:
    print("Record not found!")
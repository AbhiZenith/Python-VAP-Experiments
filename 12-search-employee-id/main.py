"""
Experiment: 12
Program: Employee Dictionary
Author: Abhishek Choudhery
Description: Python program to search employee details using employee ID.
"""

employees = { 
            101: {"name": "X", "salary": 55000},
            102: {"name": "y", "salary": 65000},
            103: {"name": "z", "salary": 95000}
            }

id = int(input("Enter Employee ID to search: "))

if id in employees:
    details = employees[id]
    print(f"Record Found: Name: {details['name']}, Salary: {details['salary']}")
else:
    print("Record not found!")
"""
Experiment: 11
Program: Employee Dictionary
Author: Abhishek Choudhery
Description: Python program to create a dictionary of employees with ID, name, and salary.
"""

# Dictionary: { ID: {Details}}
employees = { 
            101: {"name": "X", "salary": 55000},
            102: {"name": "y", "salary": 65000},
            103: {"name": "z", "salary": 95000}
            }

# Displaying all records
for emp_id, data in employees.items():
    print(f"ID: {emp_id}, Name: {data['name']}, Salary: {data['salary']}")
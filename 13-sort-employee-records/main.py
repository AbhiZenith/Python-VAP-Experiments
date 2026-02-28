"""
Experiment: 13
Program: Employee Records Sorting
Author: Abhishek Choudhery
Description: Python program to sort employee records based on salary.
"""
# List of Dictionaries
employees = [
    {"id": 101, "name": "X", "salary": 85000},
    {"id": 102, "name": "Y", "salary": 65000},
    {"id": 103, "name": "Z", "salary": 75000}
]

# Sort by the 'salart' ket in each dictionary
sorted_employees = sorted(employees, key = lambda x: x['salary'])

# Display the result
for emp in sorted_employees:
    print(f"{emp['name']}: {emp['salary']}")
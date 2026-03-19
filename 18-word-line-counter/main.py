"""
Experiment: 18
Program: File Handling
Author: Abhishek Choudhery
Description: Python program to read a text file and count the number of lines and words.
"""
with open("sample.txt", "r") as f:
    data = f.read()
    
print("Lines:", data.count("\n"))
print("Words:", len(data.split()))
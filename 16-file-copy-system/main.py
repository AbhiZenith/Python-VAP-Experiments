"""
Experiment: 16
Program: File Copying
Author: Abhishek Choudhery
Description: Python program to copy content from one file to another file.
"""

#Open the original file to read
with open('first.txt', 'r') as file1:
# Save the text into a variable
    content = file1.read() 

#Open (or create) a new file to write 
with open('second.txt', 'w') as file2:
# Paste the text into the new file
    file2.write(content) 

"""
Experiment: 15
Program: Character Counting
Author: Abhishek Choudhery
Description: Python program to count vowels, consonants, digits, and special characters in a string.
"""

# Get input from the user
text = input("Enter a string: ")

# Initialize counters to zero
vowels = 0
consonants = 0
digits = 0
special = 0

# Define a string containing all vowels for easy checking
vowel_list = "aeiouAEIOU"

# Loop through every single character in the input string
for char in text:
    
    # 1. Check if the character is an alphabet letter
    if char.isalpha():
        # Check if the letter is in our vowel list
        if char in vowel_list:
            vowels += 1
        else:
            # If it's a letter but not a vowel, it must be a consonant
            consonants += 1
            
    # 2. Check if the character is a number
    elif char.isdigit():
        digits += 1
        
    # 3. If it's not a letter and not a number, it's a special character
    else:
        special += 1

# Print the final counts
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special Characters: {special}")
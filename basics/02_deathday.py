"""2. Write a program that asks the user for their name name age. 
Output a message that tells them the year in which they will be 100 years old. Do not use modules/packages.
"""
# Code goes here
current_year = 2023
user_name = input("What is your name?")
user_age = int(input("What is your age?"))

output_year = current_year - user_age + 100

print("In the year " + str(output_year) + " you will be 100 years old!")
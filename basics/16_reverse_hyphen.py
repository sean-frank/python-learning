"""
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""

# Code goes here
input = "green-red-yellow-black-white"

def sorter(input):
    my_input = input
    sorted_input = my_input.split("-")
    sorted_input_final = "-".join(sorted(sorted_input))
    return sorted_input_final
print(sorter(input))

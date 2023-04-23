"""
Write a Python function that checks whether a passed string is a palindrome or not. Go to the editor
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""

# Code goes here
word = "nurses run"

def check(word):
    removed_spaces = word.lower().replace(" ","")[::-1]
    reversed_word = removed_spaces[::-1]
    return reversed_word == removed_spaces
    
validator = check(word)
if validator == True:
    print("The word %s is a palindrome." %word)
else:
    print(f"The word {word} is not a palindrome")



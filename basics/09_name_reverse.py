"""
    Program Name: Name Reverse
    Processing: Program asks for a users name and reverses the name.
    Sample Input:
        Enter your name: John Smith
    Sample Output:
        Your name reversed is: htiM nhoJ
"""

# Code goes here
word = input("Enter your name: ")
for i in range(len(word) -1, -1, -1):
    print(i, word[i])

"""
    Program Name: Get Extension from File Name
    Processing: Provided a filename, extract the file extension and output 
                the name without the extension and the extension.
    Sample Input:
        <<< test.txt
        <<< Python file.py
        <<< my_program.java
        <<< My Totally Secret Keys.docx
        <<< Totally not my passwords
        
    Sample Output:
        Filename: test
        Extension: txt
        
        Filename: Python file
        Extension: py
        
        Filename: my_program
        Extension: java
        
        Filename: My Totally Secret Keys
        Extension: docx
        
        Filename: Totally not my passwords
        Extension: 
"""

# Code goes here
user_input = input("Please enter a filename including the extenstion: ")

def split_name(filename):
    dot_starting = filename.find('.') ##will save location of where the '.' is.
    if dot_starting >= 0: 
        print("Filename: " + filename[:dot_starting])
        print("Extension: " + filename[dot_starting +1:])
    else:
        print("Filename: " + filename)
        print("Extension: ")
        
split_name(user_input)




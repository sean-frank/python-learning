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
#user_input = input("Please enter a filename including the extension: ")
user_input = "test.py java.exe list.sh"
first_split = user_input.split('.')
print(first_split)


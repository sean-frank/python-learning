"""
Write a Python function that accepts a string and counts the number of upper and lower case letters. Go to the editor
Sample String : 'The quick Brown Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 13
"""
# Code goes here
input = "The quick Brown Fox"

def find_caps(input):
    s = input.strip()
    count = 0
    for i in s:
        if i.isupper():
            count = count + 1 
    return count
def find_lower_case(input):
    s = input.strip()
    count = 0
    for i in s:
        if i.islower():
            count = count + 1
    return  count  

print(f"No. of Upper case characters : {find_caps(input)}")
print(f"No. of Lower case characters : {find_lower_case(input)}")
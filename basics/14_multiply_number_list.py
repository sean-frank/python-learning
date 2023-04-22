"""
Write a Python function to multiply all the numbers in a list. 
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336 
"""
my_list = [8,2,3,-1,7]

def multiply_number(number_list):
    total = 1 
    for i in number_list:
        total *= i
    return total
print(multiply_number(my_list))


"""
4. Write a program that has a defined list of numbers, for example [11, 24, 102, 444, 1213, 4, 1], 
with the output being a new list that consists only the first and last elements of the list. Do not use modules/packages. 
"""

starting_list = [11, 24, 102, 444, 1213, 4, 1] ##should be able to input any list of numbers.
list_length = len(starting_list)
first_point = starting_list[0]
end_point = starting_list[-1]
final_list = [first_point, end_point]
print(final_list)
"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

"""
# Code goes here

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
def main(input):
    newlist = []
    for i in input:
        if i % 2 == 0:
            newlist.append(i)
    print(newlist)

main(input)
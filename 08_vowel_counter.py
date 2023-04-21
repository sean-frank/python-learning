# Program Name: Vowel Counter
# Processing: Program asks for a users name and checks whether the name
#             contains a vowel. Output each vowel that they have in their 
#             name and the number of each vowel in their name.
# Sample Input:
# Enter your name: John Smith
# Sample Output:
#     Your name contains the following vowels:
#     a: 0
#     e: 0
#     i: 1
#     o: 1
#     u: 0

name = input("Enter your first and last name: ")


a_count = name.upper().count("A")
e_count = name.upper().count("E")
i_count = name.upper().count("I")
o_count = name.upper().count("O")
u_count = name.upper().count("U")

print("Your name contains the following vowels: ")
print("a: " + str(a_count))
print("e: " + str(e_count))
print("i: " + str(i_count))
print("o: " + str(o_count))
print("u: " + str(u_count))


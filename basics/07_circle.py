"""
7. Write a program that asks the user for the radius of a circle, calculate the diameter, 
circumference and volume of the circle. Output the radius given, diameter, circumference, 
and volume each on their own line.
"""

pi = 3.141592653589793
radius = input("Please enter the radius of any circle: ")
radiussquared = int(radius) * int(radius)
diameter = int(radius) * 2

circumference = 2 * pi * int(radius)

area = pi * int(radiussquared) 

print("The radius given was " + radius + ".")
print("The diameter is " + str(diameter) + ".")
print("The cirumference is " + str(circumference) + ".")
print("The area is " + str(area) + ".")


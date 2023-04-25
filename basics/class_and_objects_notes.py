
class Person:
    name = "No Name"
    age = 0


##### METHOD 1 - Intensionally Broken

# The following is a not great use-case for using classes,
# without including the () following the class names,
# a copy is not create and MERELY points to the Class and
# all changes are shared between the two variables is SHARED.

dave = Person # Create a pointer to Person
sam = Person # Also create another pointer to Person

# change Person.name to "Dave"
dave.name = "Dave"

# Seeing below, not only did dave.name get changed,
# sam.name did as well since they both point to the same
# thing.
print(sam.name) # >>> "Dave"


##### METHOD 1 - Proper Method

# This is the proper method of using classes, as it creates
# a unique copy of the Class and all changes to the variable
# sticks to that variable and is not shared.

dave = Person() # Creates unique copy of the class Person
sam = Person()

dave.name = "Dave"

# Seeing below, the only value that was changed was for variable
# dave, whereas variable sam remains the default to Class Person.

print(sam.name) # >>> "No Name"
print(dave.name) # >>> "Dave"

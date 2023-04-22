##3. Write a program that asks the user for number, then determine if the number is odd or even. Output an appropriate message to the user determined by whether it's odd or even. Do not use modules/packages.

num = int(input("Please enter a number."))
if num % 2 == 0:
    print("Your number is even")
else:
    print("The number " +str(num) + " is odd")
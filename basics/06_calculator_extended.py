## Write a program that asks the user to select a basic arithmetic operation like addition, subtraction, multiplication, or division; asking the user for 2 numbers of **any type** that 
## will be used in the arithmetic. Output to the user the arithmetic and its value, decimals should be rounded to the 2nd decimal place, An example `"112 x 111 = 12432"`, `"3.1415 / 2 = 1.57"`. **No modules/packages allowed**

num1 = input("Enter your first number: ")
operator = input("Enter any operator (ex. +,-,*,/ ): ")
num2 = input("Enter your last number: ")

if "." in num1:
    num1option = float(num1)
else: 
    num1option = int(num1)

if "." in num2:
    num2option = float(num2)
else: 
    num2option = int(num2)


if operator == "+":
    result = num1option + num2option
elif operator == "-":
    result = num1option - num2option
elif operator == "*":
    result = num1option * num2option
elif operator == "/":
    result = num1option / num2option

result_rounded = round(result, 2)

print(str(num1option) + " " + operator + " " + str(num2option) + " = " + str(result_rounded))



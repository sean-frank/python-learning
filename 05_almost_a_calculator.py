## 5. Write a program that asks the user to select a basic arithmetic operation like addition, subtraction, multiplication, or division; asking the user for 2 integers that will be used in the arithmetic. Output to the user the arithmetic and its value. An example "112 x 111 = 12432". *No modules/packages allowed*

first_num = int(input("Please enter your first number."))
operator = input("Please enter the operator you would like to use. (ex. +, -, *, / )")
second_num = int(input("Please enter your last number."))

if operator == "+" :
    result = first_num + second_num 
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/":
    result = first_num / second_num

print(str(first_num) + " " + str(operator) + " " + str(second_num) + " = " + str(result))
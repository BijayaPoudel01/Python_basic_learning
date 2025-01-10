#1.program to find greater number between three numbers.
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
number3 = int(input("Enter third number:"))

if number1 > number2 and number1 > number3:
    print("number1 is great")
elif number2 > number1 and number2 > number3:
        print("number2 is great")
elif number3 > number1 and number3 > number2:
    print("number3is great")
else:
    print("other than number 1 is great")

#2. Program to add two numbers in python.
a = int(input("enter num1:")) #adding with user input
b = int(input("enter num2:"))
sum = a + b
print("sum:" , + sum)

num1 = 1#adding with + operator
num2 = 2
sum = num1 + num2
print("sum of", num1, "and" ,num2, "is", sum)



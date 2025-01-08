#first python
age = 20
print(age)

#variables
grade = 2 #integer
price = 20.5 #floating point
first_name = "Bijaya poudel" #string
is_online = False #boolean
print(grade, price, first_name, is_online)

#Example of variable to store these.suppose John Smith is a patient in hospital. He is 20 years old. He is a new patient.
patient = "John Smith"
age = 20
is_new_patient =  True
print(patient, age, is_new_patient)

#Recieving Input
name = input("What is your name? ")
print("Hello" + name) #string concatenation i.e joining two strings with + operator.

#Type Conversion
birth_year = input("Enter your birth year")
age = (2024 - int(birth_year)) # we used integer to print int type data.
print(age)
# example: First:20, second:10.1, sum:30.1
First_number = input("Enter first number")
Second_number = input("Enter second number")
sum = (int(First_number) + (float(Second_number)))
print("sum:" + str(sum))
#or
First = float(input("First:"))
Second = float(input("Second:"))
sum = First + Second
print("sum:" + str(sum))





#functions
def sayhi():
    print("hello bijaya")
print("top")
sayhi()
print("bottom")

def say_hi(Name, age):
 print("hello " + Name, "you are " + age)
say_hi("bijaya", "23")
say_hi("Niraj", "24")

#return statement
def cube(num):
   return num * num * num
print(cube(3))

def max_num(num1, num2, num3): #greaterof 3 numbers
   if num1 >= num2 and num1 >= num3:
    return num1
   elif num2 >= num1 and num2 >= num3:
    return num2
   else:
          return num3
print(max_num(1,2,4))



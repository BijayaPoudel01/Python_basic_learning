#strings
course = "python for programming"
print(course.upper())
print(course.find("t"))
print(course.replace("for","4"))
print("python" in course) #in operator in python
print("java" not in course) #not in operator

#Arithmetic Operators
x=3
print(x + 3)
#assighnment operator
x += 5
print(x)

#operator precedence
x=2 + 10 * 2
print(x)
y= (2+10) *2
print (y)

#comparision operator
x = 3>2
print(x)
x= 3==2
print(x)

#logical operator and(both true), or(at least one), not (reverse)
price = 25
print(price>10 and price<30)
print(not price<3)

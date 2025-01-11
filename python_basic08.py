# factorial of number
num = 6
factorial = 1
for i in range (1, num + 1):
    factorial *= i
    print ("The factorial of", num, "is", factorial)

#To find a simple interest.
P = int(input("Enter the principle:"))
T = int(input("Enter the Time:"))
R = int(input("enter rate of interest"))
SI =  (P * T * R )/ 100
print(SI)


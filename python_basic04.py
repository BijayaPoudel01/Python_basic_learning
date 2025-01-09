#exercise: (weight:170, K(g) or (L)bs:l ,weight in kg:76.5)
weight = float(input("Weight: "))
unit = (input("K(g) or (L)bs: "))
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("weight in kg:" + str(converted))

 #loop cause a section of our program to be repeated for a certain number of time.
 #while loop
i = 1
while i<= 5:
     print(i * '*')
     i = i + 1 #whilethe statement is true the code will be executed.

#for loop
j= 1
for j in range (1, 20):
    print(j)

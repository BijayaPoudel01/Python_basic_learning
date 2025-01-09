#list and list methods.
names = ["Bijaya", "Niraj", "Nimesh", "Binaya"]
print(names[0])
print(names[-2])
names[0] = "Biju"
print(names)
names.remove("Niraj")
print(names)
print(names[0:2])
print(names)

numbers=[1,2,3,4,5]
numbers.append(6) #list Methods
print(numbers)
numbers.insert(0, 0)
#numbers.clear()
print(numbers)
print(1 in numbers)
print(len(numbers))

#FOR LOOP
numbers = [1,2,3,4,5,6,7]
for item in numbers:  #created item as loop variable
    print(item)

i = 0  #while loop
while  i < (len(numbers)):
      print(numbers[i])
      i = i + 1

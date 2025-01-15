# just revising previously done things
i = 1
while i <= 80:
    print(i)
    i += 1

j = 1
for j in range (1, 5):
    print(j * "*")

for  letter in "Bijaya Academy":
    print(letter)

#Building a translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + "G"
            else:
             translation = translation + "g" #if there are vowel letters then the vowel is translated with g.
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase:")))
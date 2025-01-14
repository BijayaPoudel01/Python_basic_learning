#Building a guessing game using variables, While loop, if statement etc.
print("Welcome to the Guessing Game! You have 3 chances to guess the secret word. Good luck!")
secret_word = "rose"
guess = " "
guess_count = 0
guess_warning = 2
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count == guess_warning:
        print("You have one last chance," + "Hint:It's a flower name")
    if guess_count < guess_limit:
     guess = input("Enter guess:")
     guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
         print("Oh no!," + "You've run out of guesses. Better luck next time!")

else:
        print("Congratulations! You guessed it right")



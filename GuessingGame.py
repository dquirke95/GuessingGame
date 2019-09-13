# This is a guessing game where you get 3 guesses to guess a secret word

secret_word = "coffee"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Please enter your guess:")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win")
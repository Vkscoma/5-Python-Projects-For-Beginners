# Create a random number between 1 and 100 - have the user guess the number
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

random_number = random.randint(1, 10)
user_guess = 0

while True:
    user_guess += 1
    user_input_number = int(input("Make a guess: "))
    if user_input_number == random_number:
        print("You got it! The answer was " + str(random_number))
        print("You got it in " + str(user_guess) + " guesses.")
        break
    elif user_input_number > random_number:
        print("Too high.")
    elif user_input_number < random_number:
        print("Too low.")
    else:
        print("Invalid input.")

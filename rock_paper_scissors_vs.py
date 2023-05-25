# Create a Rock, Paper, Scissors game that will play against the user.
import random

print("Welcome to the Rock, Paper, Scissors!")

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Choose rock, paper, or scissors: ").lower()

while True:
    if user_choice == computer_choice:
        print("It's a tie!")
        print("The computer chose " + computer_choice)
        break
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        print("The computer chose " + computer_choice)
        break
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        print("The computer chose " + computer_choice)
        break
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        break
    else:
        print("You lose.")
        print("The computer chose " + computer_choice + ".")
        break

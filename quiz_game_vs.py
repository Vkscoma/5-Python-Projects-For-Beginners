# Make a game that consists of 10 questions - Start by introducing them to the game and asking for their name
print("Welcome to the quiz game!")

user_name = input(
    "What is your name: ",
)
print("Hello", user_name)

question_1 = input("Do bass players use their fingers or a pick?: ")

if question_1 == "fingers" or "pick" or "both":
    print("That is correct!")
else:
    print("incorrect")

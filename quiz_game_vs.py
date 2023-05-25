# Make a game that consists of 3 questions - Start by introducing them to the game and asking for their name
print("Welcome to the quiz game!")

user_name = input(
    "What is your name: ",
)
print("Hello", user_name)
score = 0

question_1 = input("Do bass players use their fingers or a pick?: ")

if question_1 == "fingers".lower() or "pick".lower() or "both".lower():
    print("That is correct!")
    score += 1
else:
    print("incorrect")

question_2 = input("What kind of bass does Mark Hoppus use?: ")

if question_2 == "Fender Precision Bass".lower() or "Fender P Bass".lower():
    print("That is correct!")
    score += 1
else:
    print("incorrect")

question_3 = input("What is the name of the bassist for Green Day?: ")

if question_3 == "Mike Dirnt".lower():
    print("That is correct!")
    score += 1
else:
    print("incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score / 3 * 100) + "%")

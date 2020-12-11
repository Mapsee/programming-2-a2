# quiz.py

# Counter
counter = 0

# Introduction
input("Hello welcome to the mini quiz! Are you ready to answer questions? ")
print("Aight here we go! ")

# Simple addition question
number = input("\nQuestion 1: What is 4+5? ")
if number == "9":
    print(f"Good Job!")
    counter += 1
else:
    print(f"Sorry you got it wrong ;-;")
print(f"{counter}/5")

# What is acceleration of gravity?
print("\nQuestion 2: What is the acceleration of gravity?\nA = 1.0m/s^2\nB = 3.5m/s^2\nC = 1.9m/s^2\nD = 9.8m/s^2")
letter = input("Please input a letter: ").upper().strip("?!@#$%^&()")
if letter == "D":
    print("Yay you got it right. ")
    counter += 1
else:
    print("That wasn't the right answer .-.")
print(f"{counter}/5")

# Iron Man
answer = input("\nQuestion 3: I love you ____ ")
if answer == "3000":
    print("Congrats you got it right! ")
    counter += 1
else:
    print("Wrong answer. ")
print(f"{counter}/5")

# More physics
print("\nQuestion 4: What are two words that define a vector? ")
define1 = input("Enter the first word: ").lower().strip("!?@#$%^&*() ")
define2 = input("Enter the second word: ").lower().strip("!?@#$%^&*() ")
vector_definition = f"{define1}{define2}"
if vector_definition == "displacementdirection" or vector_definition == "directiondisplacement":
    print("Yay that's the correct answer! ")
    counter += 1
else:
    print("Tu as tort.")
print(f"{counter}/5\n")

# What was the answer for question 1
re_answer = input("Question 5: What was the answer for Question 1? ")
if re_answer == "9":
    print("Wow you have a good memory! Good job you got it right. ")
    counter += 1
else:
    print("Incorrect. ")
print(f"{counter}/5\n")

# Rate the quiz
rating = input("!!!ALERT BOSS FIGHT!!! Bonus Question: Did you enjoy the quiz? ")
counter += 1
print(f"Alright thanks bro\n{counter}/5\n")

# Print results
if counter == 0:
    print("You failed :(, You got 0/5 in total")
elif counter == 1:
    print("At least you got a point yay! 1/5")
elif counter == 2:
    print("Could be better bro, 2/5")
elif counter == 3:
    print("You passed! 3/5")
elif counter == 4:
    print("Chicken nuggets, 4/5")
elif counter == 5:
    print("Good job you got full marks! 5/5")
else:
    print("Woooaaahhhh you scored 6/5, your brain big ")

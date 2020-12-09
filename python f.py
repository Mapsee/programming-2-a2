# quiz.py

counter = 0

x = float(input("Question 1: What is 4+5? "))
if x == 9:
    print("Good Job")
    counter += 1
else:
    print("Sorry you got it wrong ;-;")

print("Question 2: What is the acceleration of gravity?\nA = 1.0m/s^2\nB = 3.5m/s^2\nC = 1.9m/s^2\nD = 9.8m/s^2")
letter = input("Please input a letter: ").upper()
if letter == "D":
    print("Good job")
    counter += 1
else:
    print("Bruh")

answer = input("What is Karen's last name? ")
if answer == "Yao":
    print("Yea she's hot i know")
    counter+=1
else:
    "i don't like ur cut g"

yes = input("Give me two words that define a vector: ")
physics = yes.lower().strip( )
if physics == "displacementdirection":
    print("Good job even I couldn't believe my eyes that your actually competent")
    counter+=1
else:
    print("tu es stupide")

if counter == 1:
    print("your iq low, you got 1/5")
elif counter ==2:
    print("could be better bro, 2/5")
elif counter == 3:
    print("ur passed, 3/5")
elif counter ==4:
    print("chicken nuggets, 4/5")
else:
    print("Good job you got 5/5 ")
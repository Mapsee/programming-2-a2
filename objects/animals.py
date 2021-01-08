# animals.py
# a look at object-oriented programming

class Animal():
    # CONSTRUCTOR
    def __init__(self):
        self.legs = 0
        self.hairy = False

    def talk(self):
        return "Hello."

    def eat(self, food):
        if food == "meat":
            return "Yuuuuummmm. Meat."
        elif food in ["veggies", "vegetables"]:
            return "Yuuuuummmm. Vegetables."
        elif food == "poison":
            return "I'm not eating that."
        else:
            return "Poop."

dog = Animal()
dog.legs = 4
dog.hairy = True

# if dog.hairy:
#    print("You'll need to brush its hair. ")

print(dog.talk())
print(dog.eat("poison"))

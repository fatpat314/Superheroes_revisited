# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        # print("dog initialized!")

    def bark(self):
        print("Woof!")

    def sit(self):
        print("<> sits")

    def roll_over(self):
        print("<> rolls over")


# my_dog = Dog("Rex", "SuperDog")
# my_dog.bark()

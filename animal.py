class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')

class Frog(Animal):
    def jump(self):
        print(f'{self.name} is jumping')

my_animal = Animal("Tiger")
my_animal.eat()
my_animal.drink()

my_frog = Frog("Frog")
my_frog.jump()

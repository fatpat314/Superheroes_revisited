import random

class Ability:
    def __init__(self, name, attack_strength):
        '''
        Initialize the values passed into this method as instace variables
        '''

        # max_damage == attack_strength???

        #Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage'''

        # Pick a random value between 0 and self.attack_strength
        random_value = random.randint(0,self.attack_strength)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        ''' Instantiage instance properties '''
        self.name = name
        self.max_block = max_block

    def block(self):
        random_block_value = random.randint(0,self.max_block)
        return random_block_value

class Hero:
    #We want our hero to have a defaule "starting_health",
    #so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:'''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)

    def attack(self):
        ''' Calculate the total damage from all ability attacks.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors'''
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense'''
        defense = self.defend(damage)
        self.current_health -= damage - defense

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the oppoent hero passed in'''
        #TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        pass



if __name__ == "__main__":
    #If you run this file from the terminal
    #this block is executed

    # ability = Ability("Debugging ability", 20)
    # print(ability.name)
    # print(ability.attack())

    # armor = Armor("Debugging Shield", 10)
    # print(armor.name)
    # print(armor.block())

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    # sheild = Armor("Shield", 50)
    # hero.add_armor(sheild)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    #print(hero.abilities)
    # print(my_hero.name)
    # print(my_hero.current_health)

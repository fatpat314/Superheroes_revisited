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
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths


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

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense'''
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in'''
        #TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if len(opponent.abilities) and len(self.abilities) <= 0:
            print("DRAW")
        # 1) else, start the fighting loop until a hero has won
        else:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())

        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
                if self.current_health > 0:
                    print(f"{self.name} won")
                    self.add_kill(1)
                    opponent.add_death(1)

                else:
                    opponent.current_health > 0
                    print(f"{hero2.name} won")
                    opponent.add_kill(1)
                    self.add_death(1)

        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop

        '''Update fight'''
        # TODO: Refactor this method to update the following:
        # 1) the number of kills the hero (self) has when the opponent dies. check

        # 2) then number of kills the opponent has when the hero (self) dies check

        # 3) the number of deaths of the opponent if they die    in the fight check

        # 4) the number of deaths of the hero (self) if they die in the fight check

    def add_weapon(self, weapon):
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        half_attack_strength = self.attack_strength / 2
        # then return a random integer between half of max_damage and max_damage
        rand_half_attack_strength = random.randint(0, half_attack_strength)
        return rand_half_attack_strength

class Team():
    def __init__ (self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        ''' Add Hero object to self.heroes '''
            # TODO: Add the Hero object that is passed in to the list of heroes in
            # self.heroes
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            #if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                #set our indicator to True
                foundHero = True
            #if we looped through out list and did not fond our hero,
            #The indicator would have never changed, so return 0
            if not foundHero:
                return 0

    def view_all_heroes(self):
        """ Prints out all heroes to the console """
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.

        for hero in self.heroes:
            print (hero.name)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            self.current_health = health

    def attack(self, other_team):
        '''Battle each team against each other.'''

        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            hero1 = random.choice(living_heroes)
            opponent1 = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            hero1.fight(opponent1)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if hero1.is_alive() == False:
                living_heroes.remove(hero1)
            else:
                living_opponents.remove(opponent1)










if __name__ == "__main__":

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)

    print(hero.attack())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyers", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

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
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
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

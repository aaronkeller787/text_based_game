#!/usr/bin/env python3
import os

class Races():

    def __init__(self, race_name, weight, lifespan, adulthood, size, speed, languages, common_traits):
        self.race_name = race_name
        self.race_weight = weight
        self.lifespan = lifespan
        self.adulthood = adulthood
        self.size = size
        self.speed = speed
        self.languages = languages
        self.common_traits = common_traits

###### Halfling and Subraces ######
class Halfling(Races):

    bonus_dexterity = 2
    race_name = 'Halfling'
    lifespan = 150
    adulthood = 20
    size = 'Small'
    speed = 25
    languages = ['Common','Halfling']
    common_traits = ['Lucky', 'Brace', 'Halfling nimbleness']

    def __init__(self):
        
        while True:
            self.race_weight = int(input('Please enter your weight, between 37 and 45: '))
            if self.race_weight >= 37 and self.race_weight <= 45:
                break
            else:
                print('Please enter a number within the range')
        
    
class Lightfoot(Halfling):

    bonus_charisma = 1
    subrace_trait = ['Naturally Stealthy']
    race_name = 'Lightfoot'

class Stout(Halfling):

    bonus_constitution = 1
    race_name = 'Stout'
    subrace_trait = ['Stout Resilliance']
        
###### Gnome and Subraces ########
class Gnome(Races):
    
    bonus_intelligence = 2
    race_name = 'Gnome'
    lifespan = 425
    adulthood = 40
    size = 'Small'
    speed = 25
    languages = ['Common', 'Gnomish']
    common_traits = ['Dark Vision', 'Gnome Cunning']

    def __init__(self):

        while True:
            self.race_weight = int(input('Please enter your weight, between 37 and 45: '))
            if self.race_weight >= 37 and self.race_weight <= 45:
                break
            else:
                print('Please enter a number within the range')

class ForestGnome(Gnome):

    race_name = 'Forest Gnome'
    bonus_dexterity = 1
    subrace_trait = ['Natural Illusionist','Speak with Small Beasts']

class RockGnome(Gnome):

    race_name = 'Rock Gnome'
    bonus_constitution = 1
    subrace_trait = ['Artificer\'s Lore','Tinker']

###### Dwarf and Subraces ########
class Dwarf(Races):

    race_name = 'Dwarf'
    lifespan = 350
    adulthood = 50
    size = 'Medium'
    speed = 25
    languages = ['Common', 'Dwarvish']
    bonus_constitution = 2
    common_traits = ['Dark Vision', 'Dwarven Resiliance', 'Combat Training', 'Tool Proficiency', 'Stonecunning']

    def __init__(self):

        while True:
            self.race_weight = int(input('Please enter your weight, between 119 and 226: '))
            if self.race_weight >= 119 and self.race_weight <= 226:
                break
            else:
                print('Please enter a number within the range')
 

class HillDwarf(Dwarf):

    race_name = 'Hill Dwarf'
    bonus_wisdom = 1
    subrace_trait = ['Dwarven Toughness']

class MountainDwarf(Dwarf):

    race_name = 'Mountain Dwarf'
    bonus_strength = 2
    subrace_trait = ['Armor Training']

###### Elf and Subraces ########
class Elf(Races):

    race_name = 'Elf'
    bonus_dexterity = 2
    lifespan = 750
    adulthood = 100
    size = 'Medium'
    speed = 30
    languages = ['Common', 'Elvish']
    common_traits = ['Dark Vision', 'Keen Sense', 'Fey Ancestry', 'Trance']

    def __init__(self):
        while True:
            self.race_weight = int(input('Please enter your weight, between 79 and 180: '))
            if self.race_weight >= 79 and self.race_weight <= 180:
                break
            else:
                print('Please enter a number within the range')
     
class HighElf(Elf):

    race_name = 'High Elf'
    bonus_intelligence = 1
    subrace_trait = ['Weapon Training', 'Cantrip', 'Extra Language']

class WoodElf(Elf):

    race_name = 'Wood Elf'
    bonus_wisdom = 1
    subrace_trait = ['Weapon Training', 'Fleet of Foot', 'Mask of the Wild']

class DarkElf(Elf):

    race_name = 'Dark Elf'
    bonus_charisma = 1
    subrace_trait = [bonus_charisma, 'Weapon Training', 'Superior Darkvision', 'Sunlight Sensitivity', 'Drow Magic']

###### Half Elf ########
class HalfElf(Races):

    speed = 30
    languages = ['Common','Elvish']
    common_traits = ['Darkvision', 'Fey Ancestry']
    
    def __init__(self):
        while True:
            self.race_weight = int(input('Please enter your weight, between 79 and 180: '))
            if self.race_weight >= 79 and self.race_weight <= 180:
                break
            else:
                print('Please enter a number within the range')
        self.third_language = input('Please select a 3rd language: ')
        self.third_skill = input('Please select a 3rd skill: ')
        self.fourth_skill = input('Please select a 4th skill: ')
        self.bonus_attributes_one = input('Please select a 2nd attribute: ')
        self.bonus_attributes_two = input('Please select a 3rd attribute: ')


###### Tiefling ########
class Tiefling(Races):

    race_name = 'Tiefling'
    bonus_charisma = 2
    bonus_intelligence = 1
    lifespan = 85
    adulthood = 18
    size = 'Medium'
    speed = 30
    languages = ['Common','Infernal']
    common_traits = ['Dark Vision', 'Hellish Resistance', 'Infernal Legacy']

    def __init__(self):
        while True:
            self.race_weight = int(input('Please enter your weight, between 114 and 238: '))
            if self.race_weight >= 114 and self.race_weight <= 238:
                break
            else:
                print('Please enter a number within the range')

###### Human ########
class Human(Races):

    race_name = 'Human'
    bonus_strength = 1
    bonus_charisma = 1
    bonus_intelligence = 1
    bonus_dexterity = 1
    bonus_constitution = 1
    bonus_wisdom = 1
    lifespan = 80
    adulthood = 18
    size = 'Medium'
    speed = 30
    languages = ['Common']
    
    

    def __init__(self):
        while True:
            self.race_weight = int(input('Please enter your weight, between 114 and 270: '))
            if self.race_weight >= 114 and self.race_weight <= 270:
                break
            else:
                print('Please enter a number within the range')
        self.second_language = input('Please select a 2nd language: ')
    

        
#################################################
# Need to add variant traits for the human race #
#################################################

###### Half-Orc ########
class HalfOrc(Races):

    race_name = 'Half-Orc'
    bonus_strength = 2
    bonus_constitution = 1
    lifespan = 75
    adulthood = 14
    size = 'Medium'
    speed = 30
    languages = ['Common','Orc']
    common_traits = ['Dark Vision', 'Menacing', 'Relentless Endurance', 'Savage Attacks']

    def __init__(self):
        while True:
            self.race_weight = int(input('Please enter your weight, between 144 and 280: '))
            if self.race_weight >= 144 and self.race_weight <= 280:
                break
            else:
                print('Please enter a number within the range')
        

###### Dragonborn ########
class Dragonborn(Races):

    race_name = 'Dragonborn'
    bonus_strength = 2
    bonus_charisma = 1
    lifespan = 80
    adulthood = 15
    size = 'Medium'
    speed = 30
    languages = ['Common','Draconic']
    common_traits = ['Draconic Ancestry', 'Breath Weapon', 'Damage Resistance']

    def __init__(self):
        while True:
            self.race_weight = int(input('Please enter your weight, between 179 and 376: '))
            if self.race_weight >= 179 and self.race_weight <= 376:
                break
            else:
                print('Please enter a number within the range')


def choose_race():

    print("Which race would you like to play?",'\n',
          "Press 'h' for Halfling",'\n',
          "Press 'g for Gnome",'\n',
          "Press 'd' for Dwarf",'\n',
          "Press 'e' for Elf",'\n',
          "Press 'a' for HalfElf",'\n',
          "Press 't' for Tiefling",'\n',
          "Press 'n' for Human",'\n',
          "Press 'o' for HalfOrc",'\n',
          "Press 'r' for Dragonborn",'\n'
          )
    print('\n')
    prace=input(">>> ")

    if prace == 'h' or prace == 'H':
        response = input('Would you like to choose a subrace? (y/n)')
        if response == 'y':
            print("Which subrace would you like to play?",'\n',
            "Press 'l' for Lightfoot",'\n',
            "Press 's' for Stout",'\n',)
            prace = input(">>> ")
            if prace == 'l' or prace == 'L':
                Race = Lightfoot()
            elif prace == 's' or prace == 'S':
                Race = Stout()    
        else:
            Race = Halfling()
    elif prace == 'g' or prace == 'G':
        response = input('Would you like to choose a subrace? (y/n)')
        if response == 'y':
            print("Which subrace would you like to play?",'\n',
            "Press 'f' for Forest Gnome",'\n',
            "Press 'r' for Rock Gnome",'\n',)
            prace = input(">>> ")
            if prace == 'f' or prace == 'F':
                Race = ForestGnome()
            elif prace == 'r' or prace == 'R':
                Race = RockGnome()    
        else:
            Race = Gnome()
    elif prace == 'd' or prace == 'D':
        response = input('Would you like to choose a subrace? (y/n)')
        if response == 'y':
            print("Which subrace would you like to play?",'\n',
            "Press 'h' for Hill Dwarf",'\n',
            "Press 'm' for Mountain Dwarf",'\n',)
            prace = input(">>> ")
            if prace == 'h' or prace == 'H':
                Race = HillDwarf()
            elif prace == 'm' or prace == 'M':
                Race = MountainDwarf()    
        else: 
            Race = Dwarf()
    elif prace == 'e' or prace == 'E':
        response = input('Would you like to choose a subrace? (y/n)')
        if response == 'y':
            print("Which subrace would you like to play?",'\n',
            "Press 'h' for High Elf",'\n',
            "Press 'w' for Wood Elf",'\n',
            "Press 'd' for Drow (Dark Elf)",'\n')
            prace = input(">>> ")
            if prace == 'h' or prace == 'H':
                Race = HighElf()
            elif prace == 'w' or prace == 'W':
                Race = WoodElf()    
            elif prace == 'd' or prace == 'D':
                Race = DarkElf()  
        else:
            Race = Elf()
    elif prace == 'a' or prace == 'A':
        Race = HalfElf()
    elif prace == 't' or prace == 'T':
        Race = Tiefling()
    elif prace == 'n' or prace == 'N':
        Race = Human()
    elif prace == 'o' or prace == 'O':
        Race = HalfOrc()
    elif prace == 'r' or prace == 'R':
        Race = Dragonborn()
    return Race


    
if __name__=="__main__":
    new_race = choose_race()


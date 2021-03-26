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

    def __init__(self):
        self.race_name = 'Halfling'
        self.race_weight = input('Please enter your weight, between 37 and 45: ')
        self.lifespan = 150
        self.adulthood = 20
        self.size = 'Small'
        self.speed = 25
        self.languages = {'Language1': 'Common', 'Language2': 'Halfling'}
        self.common_traits = ['Lucky', 'Brave', 'Halfling numbleness']

class Lightfoot(Halfling):

    bonus_charisma = 1
    subrace_trait = ['Naturally Stealthy']
    
    def __init__(self):
        self.race_name = 'Lightfoot'


class Stout(Halfling):

    bonus_constitution = 1

    def __init__(self,subrace_trait):
        self.race_name = 'Stout'
        self.subrace_trait = ['Stout Resilliance']
        
###### Gnome and Subraces ########

class Gnome(Races):
    
    bonus_intelligence = 2

    def __init__(self):
        self.race_name = 'Gnome'
        self.race_weight = input('Please enter your weight, between 37 and 45: ')
        self.lifespan = 425
        self.adulthood = 40
        self.size = 'Small'
        self.speed = 25
        self.languages = {'Language1': 'Common', 'Language2': 'Gnomish'}
        self.common_traits = ['Dark Vision', 'Gnome Cunning']

class ForestGnome(Gnome):

    bonus_dexterity = 1

    def __init__(self,subrace_trait):
        self.race_name = 'Forest Gnome'
        self.subrace_trait = [bonus_dexterity,'Natural Illusionist','Speak with Small Beasts']

class RockGnome(Gnome):

    def __init__(self,bonus_constitution,subrace_trait):
        self.race_name = 'Rock Gnome'
        self.bonus_constitution = 1
        self.subrace_trait = [bonus_constitution,'Artificer\'s Lore','Tinker']

###### Dwarf and Subraces ########

class Dwarf(Races):

    def __init__(self,bonus_constitution):
        self.race_name = 'Dwarf'
        self.race_weight = input('Please enter your weight, between 119 and 226: ')
        self.lifespan = 350
        self.adulthood = 50
        self.size = 'Medium'
        self.speed = 25
        self.languages = {'Language1': 'Common', 'Language2': 'Dwarvish'}
        self.bonus_constitution = 2
        self.common_traits = ['Dark Vision', 'Dwarven Resiliance', 'Combat Training', 'Tool Proficiency', 'Stonecunning']

class HillDwarf(Dwarf):

    def __init__(self, bonus_wisdom, subrace_trait):
        self.race_name = 'Hill Dwarf'
        self.bonus_wisdom = 1
        self.subrace_trait = [bonus_wisdom, 'Dwarven Toughness']

class MountainDwarf(Dwarf):

    def __init__(self, bonus_strength, subrace_trait):
        self.race_name = 'Mountain Dwarf'
        self.bonus_strength = 2
        self.subrace_trait = [bonus_strength, 'Armor Training']


###### Elf and Subraces ########

class Elf(Races):

    bonus_dexterity = 2

    def __init__(self):
        self.race_name = 'Elf'
        self.race_weight = input('Please enter your weight, between 79 and 180: ')
        self.lifespan = 750
        self.adulthood = 100
        self.size = 'Medium'
        self.speed = 30
        self.languages = {'Language1': 'Common', 'Language2': 'Elvish'}
        self.common_traits = ['Dark Vision', 'Keen Sense', 'Fey Ancestry', 'Trance']


class HighElf(Elf):

    def __init__(self, bonus_intelligence, subrace_trait):
        self.race_name = 'High Elf'
        self.bonus_intelligence = 1
        self.subrace_trait = [bonus_intelligence, 'Weapon Training', 'Cantrip', 'Extra Language']


class WoodElf(Elf):

    def __init__(self, bonus_wisdom, subrace_trait):
        self.race_name = 'Wood Elf'
        self.bonus_wisdom = 1
        self.subrace_trait = [bonus_wisdom, 'Weapon Training', 'Fleet of Foot', 'Mask of the Wild']

class DarkElf(Elf):

    def __init__(self, bonus_charisma, subrace_trait):
        self.race_name = 'Dark Elf'
        self.bonus_charisma = 1
        self.subrace_trait = [bonus_charisma, 'Weapon Training', 'Superior Darkvision', 'Sunlight Sensitivity', 'Drow Magic']


if __name__=="__main__":
    new_race = Lightfoot()
    print(new_race.bonus_charisma)
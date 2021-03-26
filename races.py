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
        self.race_weight = input('Please enter your weight, between 37 and 45: ')

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
        self.race_weight = input('Please enter your weight, between 37 and 45: ')
     
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
    languages = {'Language1': 'Common', 'Language2': 'Dwarvish'}
    bonus_constitution = 2
    common_traits = ['Dark Vision', 'Dwarven Resiliance', 'Combat Training', 'Tool Proficiency', 'Stonecunning']

    def __init__(self,bonus_constitution):
        self.race_weight = input('Please enter your weight, between 119 and 226: ')

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
    languages = {'Language1': 'Common', 'Language2': 'Elvish'}
    common_traits = ['Dark Vision', 'Keen Sense', 'Fey Ancestry', 'Trance']

    def __init__(self):
        self.race_weight = input('Please enter your weight, between 79 and 180: ')
     
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
    
    
    def __init__(self,third_language,third_skill,fourth_skill,bonus_attributes_one,bonus_attributes_two):
        self.third_language = third_language
        self.third_skill = third_skill
        self.fourth_skill = fourth_skill
        self.bonus_attributes_one = bonus_attributes_one
        self.bonus_attributes_two = bonus_attributes_two

    @classmethod
    def get_values(values):
        return values(
        third_language = input('Please select a 3rd language: '),
        third_skill = input('Please select a 3rd skill: '),
        fourth_skill = input('Please select a 4th skill: '),
        bonus_attributes_one = input('Please select a 2nd attribute: '),
        bonus_attributes_two = input('Please select a 3rd attribute: '),
        )


if __name__=="__main__":
    new_race = HalfElf.get_values()
    new_race.languages.append(new_race.third_language)
    print(new_race.languages)
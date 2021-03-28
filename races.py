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
    languages = ['Common', 'Dwarvish']
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
    languages = ['Common', 'Elvish']
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
        self.race_weight = input('Please enter your weight, between 79 and 180: ')
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
        self.race_weight = input('Please enter your weight, between 114 and 238: ')

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

    def __init__(self,second_language):
        self.race_weight = input('Please enter your weight, between 114 and 270: ')
        self.second_language = second_language
    
    @classmethod
    def get_values(values):
        return values(
            second_language = input('Please select a 2nd language: ')
        )


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
        self.race_weight = input('Please enter your weight, between 144 and 280: ')


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
        self.race_weight = input('Please enter your weight, between 179 and 367: ')


if __name__=="__main__":
    new_race = HalfElf.get_values()
    new_race.languages.append(new_race.third_language)
    print(new_race.languages)
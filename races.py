#!/usr/bin/env python3
import os

class Races():

    def __init__(self, race_name, weight, lifespan, adulthood, size, speed, languages, common_traits, description):
        self.race_name = race_name
        self.race_weight = weight
        self.lifespan = lifespan
        self.adulthood = adulthood
        self.size = size
        self.speed = speed
        self.languages = languages
        self.common_traits = common_traits
        self.description = description

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
    description = ('Halflings are isolated, cheerful people who love the commodity of their homes and communities. That’s the main reason most of them don’t abandon their birthplaces (shires).\n' 
    'However, a strong sense of curiosity inhabits in most of them, leading these little folk to become adventurers or travel to other places. They are extremely agile, but as a result of their short legs, not as fast as the other races')

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
    description = ('These halflings can easily hide behind anything that is higher than themselves and tend to be more charismatic than the rest from their race.')

class Stout(Halfling):

    bonus_constitution = 1
    race_name = 'Stout'
    subrace_trait = ['Stout Resilliance']
    description = ('Stout halflings have are similar in a certain way to dwarves. They are stout as their name says and have a resistance to poison.')
        
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
    description = ('Gnomes are weird super positive beings. Their spirits shine even in the darkest nights. Great inventors, pranksters, and even better intellectuals.\n' 
    'Living away from other communities they tend to live pretty normal lives in their about 500 years. However, just like halflings, curiosity is something that every one of them carries, as well as their impulsive behavior, creating excellent and many adventurers out of them.')

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
    description = ('They stealthily move through the forest, creating illusions to trick whoever gets close. Their affinity with animals let them communicate simple ideas to these beasts.')

class RockGnome(Gnome):

    race_name = 'Rock Gnome'
    bonus_constitution = 1
    subrace_trait = ['Artificer\'s Lore','Tinker']
    description = ('Rock gnomes are known as the best tinkerers. These hardy beings can create little gadgets or things with a specific purpose, to be used for commodity or to maybe get them out of trouble.')

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
    description = ('Stout, short and hardworking. Those might be the best words to describe a dwarf. Having their race forged by the god Moradin, they were taught of the benefits of hard labor, perfection in their works, and the importance of their clans.\n'
    'Dwarves live their long lives with a spirit of good and justice, that may only be corrupted by greed. Their sturdiness allows them to be more resistant than other classes in combat as well as resist poison. They tend to vary depending of the place they are from')

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
    description = ('Wiser than their mountain siblings, they also tend to be even more sturdy than them, meaning they are able to stand more hits before falling in combat.')

class MountainDwarf(Dwarf):

    race_name = 'Mountain Dwarf'
    bonus_strength = 2
    subrace_trait = ['Armor Training']
    description = ('The mountain and the labor in there has made them stronger. Their skin tends to be lighter toned as well as their stature a bit higher.')

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
    description = ('Elves are magical and gracious beings, as well as very close to being eternal. They develop many different attitudes during their life.\n' 
    'When young (young being up to 100 years old) they have an adventurous and curious way of thought, making them go for adventures. By the time they reach adulthood their personalities change and become much more peaceful, but don’t discard the idea of going exploring until they become elders.\n' 
    'They make for excellent artists and tend to be quite chaotic when it comes to laws. Last but not least, they don’t sleep but enter trances for 4 hours a day in which they remain semiconscious.')

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
    description = ('High elves are more studious and value art in a greater way than the other subraces. In addition, they master both longswords and shortswords, as well as shortbows and longbows.')

class WoodElf(Elf):

    race_name = 'Wood Elf'
    bonus_wisdom = 1
    subrace_trait = ['Weapon Training', 'Fleet of Foot', 'Mask of the Wild']
    description = ('Their intuition and keen senses are found to be the best among all elves, as well as their speed. Their training with weapons is similar to their high elves siblings, making them proficient in the use of longswords, shortswords, shortbows and longbows.')

class DarkElf(Elf):

    race_name = 'Dark Elf'
    bonus_charisma = 1
    subrace_trait = [bonus_charisma, 'Weapon Training', 'Superior Darkvision', 'Sunlight Sensitivity', 'Drow Magic']
    description = ('Drows were banished from the surface world for betraying Corellon, the elven god. That developed a hate from them towards the other elves. However, a very low number are indifferent about the quarrel and decide to go back to the surface in search for adventure. They are normally very charismatic and can master drow magic.')

###### Half Elf ########
class HalfElf(Races):

    speed = 30
    languages = ['Common','Elvish']
    common_traits = ['Darkvision', 'Fey Ancestry']
    description = ('These beings combine the best parts of elves and humans, or so they say. They don’t really belong in either of both worlds, having to decide the community they find themselves more identified with. That’s the reason why they work excellently as ambassadors or wander off feeling excluded from all places, sometimes in the search for weird adventurers with whom they can find a sense of belonging.')
    
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
    description = ('Tieflings take lots of forms and colors. They can have different kinds of horns and tails, as well as be from a great variety of colors. Nevertheless, they share some kind of curse. These are beings of infernal lineage due to a pact that someone in the long past made with Asmodeus (lord of Hell).\n' 
    'They look mostly human, not taking into account the features described above. Even though they are mostly intellectual and highly charismatic beings, they tend to be received with mistrust by superstitious people.')

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
    description = ('Well… I suppose you are a human, so you should know what we are good at. Absolutely nothing! Or more precisely, a bit in everything. Humans are quite more anxious and eager to adventure than the other races due to their short lives (in comparison with the others).')
    

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
    description = ('Half orcs have orc blood running through their veins. This makes them much stronger than normal people, as well as hardy. However, that also can make them act impulsively and savagely.\n' 
    'They often live, or at least used to in orc tribes and may or may not feel the rage of Gruumsh within them (Gruumsh being the orc god). While many of them triumph as leaders in their tribe due to their high IQ in comparison with the others,\n' 
    'others are exiled and go in search of jobs in communities or go adventuring. Their high endurance makes them almost impossible to fall in combat.')

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
    description = ('Descendants of dragons, these draconic humanoids live in clans who they value more than their life itself. Depending on their color, they get a breath attack of a specific type, as well as resistance to that same type of damage in combat. They tend to be as strong as they are charismatic, just like their fellow ancestors.\n' 
    'Even though they are covered in scales, they lack the tail and wings that make dragons so characteristic.')

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


#!/usr/bin/env python3
import os

class PlayerClass():

    def __init__(self,class_name,description,hit_die,primary_ability,saving_throws,proficiencies,player_name):

        self.class_name = class_name
        self.description = description
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throws = saving_throws
        self.proficiencies = proficiencies
        self.player_name = player_name

# Class attributes for the Barbarian 
class Barbarian(PlayerClass):

    class_name = 'Barbarian'
    description = 'A fierce warrior of primitive background who can enter a battle rage'
    hit_die = 12
    primary_ability = 'Strength'
    saving_throws = ['Strength', 'Constitution']
    proficiencies = ['Light Armor', 'Medium Armor', 'Shields', 'Simple Weapons', 'Martial Weapons']

    def __init__(self):
        self.playername = input('Please name your character: ')



# Class attributes for the Bard
class Bard(PlayerClass):

    class_name = 'Bard'
    description = 'An inspiring magician whose power echoes the music of creation'
    hit_die = 8
    primary_ability = 'Charisma'
    saving_throws = ['Dexterity','Charisma']
    proficiencies = ['Light Armor', 'Simple Weapons', 'Hand Crossbows', 'Longswords', 'Rapiers', 'Shortswords']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Cleric
class Cleric(PlayerClass):

    class_name = 'Cleric'
    description = 'A priestly champion who wields divine magic in service of a higher power' 
    hit_die = 8
    primary_ability = 'Wisdom'
    saving_throws = ['Wisdom', 'Charisma']
    proficiencies = ['Light Armor', 'Medium Armor', 'Shields', 'Simple Weapons']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Druid
class Druid(PlayerClass):

    class_name = 'Druid'
    description = 'A priest of the Old Faith, wielding the powers of nature — moonlight and plant growth, fire and lightning — and adopting animal forms'
    hit_die = 8
    primary_ability = 'Wisdom'
    saving_throws = ['Intelligence','Wisdom']
    proficiencies = ['Light (Non-metal) Armor','Medium (Non-Metal) Armor','Shields (Non-Metal)','Clubs', 'Daggers', 'Darts', 'Javelins', 'Maces', 'Quarterstaffs', 'Scimitars', 'Sickles', 'Slings', 'Spears']

    def __init__(self):
        self.playername = input('Please name your character: ')

# Class attributes for the Fighter
class Fighter(PlayerClass):

    class_name = 'Fighter'
    description = 'A master of martial combat, skilled with a variety of weapons and armor'
    hit_die = 10
    primary_ability = ['Strength', 'Dexterity'] # One or the other - build logic for this
    saving_throws = ['Strength', 'Constitution']
    proficiencies = ['All Armor', 'Shields', 'Simple Weapons', 'Martial Weapons']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Monk
class Monk(PlayerClass):

    class_name = 'Monk'
    description = 'A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection'
    hit_die = 8
    primary_ability = ['Dexterity', 'Wisdom']
    saving_throws = ['Strength', 'Dexterity']
    proficiencies = ['Simple Weapons', 'Shortswords']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Paladin
class Paladin(PlayerClass):

    class_name = 'Paladin'
    description = 'A holy warrior bound to a sacred oath'
    hit_die = 10
    primary_ability = ['Strength', 'Charisma']
    saving_throws = ['Wisdom', 'Charisma']
    proficiencies = ['All Armor', 'Shields', 'Simple Weapons', 'Martial Weapons']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Ranger
class Ranger(PlayerClass):

    class_name = 'Ranger'
    description = 'A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization'
    hit_die = 10
    primary_ability = ['Dexterity', 'Wisdom']
    saving_throws = ['Strength','Dexterity']
    proficiencies = ['Light Armor', 'Medium Armor', 'Shields', 'Simple Weapons', 'Martial Weapons']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Rogue
class Rogue(PlayerClass):

    class_name = 'Rogue'
    description = 'A scoundrel who uses stealth and trickery to overcome obstacles and enemies'
    hit_die = 8
    primary_ability = 'Dexterity'
    saving_throws = ['Dexterity', 'Intelligence']
    proficiencies = ['Light Armor', 'Simple Weapons', 'Hand Crossbows', 'Longswords', 'Rapiers', 'Shortswords']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Sorcerer
class Sorcerer(PlayerClass):

    class_name = 'Sorcerer'
    description = 'A spellcaster who draws on inherent magic from a gift or bloodline'
    hit_die = 6
    primary_ability = 'Charisma'
    saving_throws = ['Constitution','Charisma']
    proficiencies = ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Warlock
class Warlock(PlayerClass):

    class_name = 'Warlock'
    description = 'A wielder of magic that is derived from a bargain with an extraplanar entity'
    hit_die = 8
    primary_ability = 'Charisma'
    saving_throws = ['Wisdom','Charisma']
    proficiencies = ['Light Armor', 'Simple Weapons']

    def __init__(self):
        self.playername = input('Please name your character: ')


# Class attributes for the Wizard
class Wizard(PlayerClass):

    class_name = 'Wizard'
    description = 'A scholarly magic-user capable of manipulating the structures of reality'
    hit_die = 6
    primary_ability = 'Intelligence'
    saving_throws = ['Intelligence','Charisma']
    proficiencies = ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows']

    def __init__(self):
        self.playername = input('Please name your character: ')

def choose_class():

    while True:
        try:
            print("Which class would you like to play?",'\n',
                "Press b for Barbarian",'\n',
                "Press a for Bard",'\n',
                "Press c for Cleric",'\n',
                "Press d for Druid",'\n',
                "Press f for Fighter",'\n',
                "Press m for Monk",'\n',
                "Press p for Paladin",'\n',
                "Press r for Ranger",'\n',
                "Press o for Rogue",'\n',  
                "Press s for Sorcerer",'\n',
                "Press w for Warlock",'\n',
                "Press z for Wizard"
                )

            pclass=input(">>> ")

            if pclass.lower() == 'b':
                player_class = Barbarian()
            elif pclass.lower() == 'a':
                player_class = Bard()
            elif pclass.lower() == 'c':
                player_class = Cleric()
            elif pclass.lower() == 'd':
                player_class = Druid()
            elif pclass.lower() == 'f':
                player_class = Fighter()
            elif pclass.lower() == 'm':
                player_class = Monk()
            elif pclass.lower() == 'p':
                player_class = Paladin()
            elif pclass.lower() == 'r':
                player_class = Ranger()
            elif pclass.lower() == 'o':
                player_class = Rogue()
            elif pclass.lower() == 's':
                player_class = Sorcerer()
            elif pclass.lower() == 'w':
                player_class = Warlock()
            elif pclass.lower() == 'z':
                player_class = Wizard()
            return player_class
        except:
            print('Please make a valid selection')
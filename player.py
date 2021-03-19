#!/usr/bin/env python3
import random
from items import Sword, Mace, Wand, Bow

class Player():

    def __init__(self,char_name,player_hp,player_power,player_gold, player_exp):
        self.char_name = char_name
        self.player_hp = player_hp
        self.player_power = player_power
        self.player_gold = player_gold
        self.player_exp = player_exp


class Fighter(Player):

    profession = 'Fighter'
    starting_weapon = Sword()
    class_description = "The figher is a warrior, and expert in weapons and, if he is clever, tactics and strategy."
        
    def __init__(self):
        self.char_name = input('What is your character name? ')
        self.player_hp = 15
        self.player_power = 1
        self.player_gold = 1
        self.player_exp = 1

        print("{}\n=====\n{}\n".format(self.profession, self.class_description))
        print(self.starting_weapon)


class Paladin(Player):

    profession = 'Paladin'
    starting_weapon = Mace()
    class_description = "The paladin is a noble and heroic warrior, the symbol of all that is right and true in the world."
        
    def __init__(self):
        self.char_name = input('What is your character name? ')
        self.player_hp = 15
        self.player_power = 1
        self.player_gold = 1
        self.player_exp = 1

        print("{}\n=====\n{}\n".format(self.profession, self.class_description))
        print(self.starting_weapon)

   
class Mage(Player):
       
    profession = 'Mage'
    starting_weapon = Wand()
    class_description = "Mages are the most versitile types of Wizard, those who choose not to specialize in any single school of magic."
        
    def __init__(self):
        self.char_name = input('What is your character name? ')
        self.player_hp = 15
        self.player_power = 1
        self.player_gold = 1
        self.player_exp = 1

        print("{}\n=====\n{}\n".format(self.profession, self.class_description))
        print(self.starting_weapon)


class Ranger(Player):

    profession = 'Ranger'
    starting_weapon = Bow()
    class_description = "The ranger is a hunter and woodsman who lives by not only his sword, but also his wits."
        
    def __init__(self):
        self.char_name = input('What is your character name? ')
        self.player_hp = 15
        self.player_power = 1
        self.player_gold = 1
        self.player_exp = 1

        print("{}\n=====\n{}\n".format(self.profession, self.class_description))
        print(self.starting_weapon)


def choose_profession():
    print("Which class would you like to play?",'\n',
          "Press f for Fighter",'\n',
          "Press c for Paladin",'\n',
          "Press m for Mage",'\n',
          "Press r for Ranger")
    print('\n')
    pclass=input(">>> ")

    if pclass == 'b' or pclass == 'B':
        Prof = Fighter()
    elif pclass == 'p' or pclass == 'P':
        Prof = Paladin()
    elif pclass == 'm' or pclass == 'M':
        Prof = Mage()
    elif pclass == 'r' or pclass == 'R' :
        Prof = Ranger()
    else:
        Prof = Fighter()
    return Prof


    
if __name__=="__main__":
    choose_profession()



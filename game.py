#!/usr/bin/env python3
import os
from os import system
from time import sleep

from dungeon import intro, room_one
from player_classes import Player, choose_profession
from program_functions import print_slow

from races import choose_race
from races import *

def welcome():

    os.system('clear')

    print('\t##############################################################################################')
    print('\t     #############        H o a r d  o f  t h e  D r a g o n  Q u e e n    ############')
    print('\t          ########################################################################')
    print("\n\n")

    

if __name__=="__main__":
    welcome()
    new_race = choose_race()
    print(new_race.race_name)
    os.system('clear')
    print("\n{}\n=====\n{}\n".format(new_race.race_name, new_race.description))
    print("\n{}\n=====\nWeight: {}\nLifespan: {}\nAdulthood Age: {}\nSize: {}\nSpeed: {}\n".format('About', new_race.race_weight, new_race.lifespan, new_race.adulthood, new_race.size, new_race.speed))

    
    

   



#!/usr/bin/env python3
import os
from os import system
from time import sleep

from dungeon import intro, room_one
from player import Player, choose_profession
from program_functions import print_slow


def welcome():

    os.system('clear')

    print('\t##############################################################################################')
    print('\t     #############        H o a r d  o f  t h e  D r a g o n  Q u e e n    ############')
    print('\t          ########################################################################')
    print("\n\n")

    choose_profession()

if __name__=="__main__":
    welcome()

   



#!/usr/bin/env python3
import os
from os import system
from time import sleep

from dungeon import intro, room_one
from player import Player, choose_profession
from program_functions import print_slow


def welcome():

    os.system('clear')

    print('\t############################################################################################')
    print('\t  #################     W e l c o m e  t o  T i d a l  F o r c e     #################')
    print('\t       ###########################################################################')
    print("\n\n")

    f = open("intro.txt", "r")
    print_slow(f.read())

    choose_profession()

if __name__=="__main__":
    welcome()

   



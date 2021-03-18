#!/usr/bin/env python3
import os
from os import system
from time import sleep

from dungeon import intro, room_one
from player import Player


def welcome():

    os.system('clear')

    print('\t############################################################################################')
    print('\t  #################     W e l c o m e  t o  T i d a l  F o r c e     #################')
    print('\t       ###########################################################################')




if __name__=="__main__":

    welcome()
    print('\n')
    new_player = Player(input('Please enter your character name: '), 10, 5, 1)
    new_player.player_stats.update({'Name': {new_player.char_name}, 'HP': {new_player.player_hp}, 'Power': {new_player.player_power},'Gold':{new_player.player_gold}})
    
    
    room_one()


   



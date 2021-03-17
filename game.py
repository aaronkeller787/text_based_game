#!/usr/bin/env python3
from time import sleep
from dungeon import intro, room_one
from player import Player


def welcome():
    pass


if __name__=="__main__":
    new_player = Player(input('Please enter your character name: '), 10, 5, 1)
    print(f'Welcome {new_player.char_name}, to Space Marines')
    print(f'You start off with {new_player.player_gold} gold, and {new_player.player_hp} hit points')
    new_player.player_stats.update({'Name': {new_player.char_name}, 'HP': {new_player.player_hp}, 'Power': {new_player.player_power},'Gold':{new_player.player_gold}})
    
    
    room_one()


   



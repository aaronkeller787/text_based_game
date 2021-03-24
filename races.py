#!/usr/bin/env python3
import os
from player import Player


class Races():

    def __init__(self, race_name, weight, lifespan, adulthood, size, speed, languages, common_traits):
        self.race_name = race_name
        self.race_weight = input('Please enter your weight: ')
        self.lifespan = lifespan
        self.adulthood = adulthood
        self.size = size
        self.speed = speed
        self.languages = {}
        self.common_traits = []

###### Halfling and Subraces ######

class Halfling(Races):

    def __init__(self, bonus_dexterity):
        self.race_name = Halfling
        self.race_weight = input('Please enter your weight, between 37 and 45')
        self.lifespan = 150
        self.adulthood = 20
        self.size = 'Small'
        self.speed = 25
        self.languages = {'Language1': 'Common', 'Language2': 'Halfling'}
        self.bonus_dexterity = 2
        self.common_traits = ['Lucky', 'Brave', 'Halfling numbleness']

class Lightfoot(Halfling):

    def __init__(self, bonus_charisma, subrace_trait):
        self.race_name = Lightfoot
        self.bonus_charisma = 1
        self.subrace_trait = [bonus_charisma,'Naturally Stealthy']

class Stout(Halfling):

    def __init__(self, bonus_constitution, subrace_trait):
        self.race_name = Stout
        self.bonus_constitution = 1
        self.subrace_trait = [bonus_constitution,'Stout Resilliance']
        
###### Gnome and Subraces ########

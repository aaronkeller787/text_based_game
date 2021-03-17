#!/usr/bin/env python3

class Player():

    def __init__(self,name,faction, hp):
        self.name = name
        self.faction = faction
        self.hp = hp


if __name__=="__main__":
    name = input("Please type your characters name: ")
    faction = input("Please enter in your Faction: ")

    new_player = Player(name, faction)
    print("Welcome %s of the %s" % (name, faction))

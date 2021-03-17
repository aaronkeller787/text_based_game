#!/usr/bin/env python3

from time import sleep
from program_functions import print_slow

def intro():
    print('Tutorial Room')

def room_one():
    
    text = '''You awaken to find yourself, stripped down, lying on the cold steel floor of what is presumably a holding cell. Your head is aching, ears ringing, and a pungent odor clings to your nose. You attempt to stand but your lefts are too weak. You sit up, rubbing your head, and take in your surroundings. In the dimly lit room, you notice that the walls are coated with filth, and realize only very few lights are actually working. As you gaze across the room a light in the corner begins to flicker, and you notice, what appears to be, a days old corpse, tucked away in the corner. You summon all of your strength to stand and begin limping to the corner of the room. As you approach you notice that the man is wearing a familiar looking uniform. Dark blue pants, matching top, and no shoes. Upon arriving you can see that he had been stabbed in his left breast. Suddenly, in the distance, you hear the sound of heavy footsteps approaching your position. The sound continues to grow louder and you begin to wonder if they are coming to collect the corpse.'
You have a choice: (S)tay as you are and tempt fate, or put on the uniform and (T)rade places with the corpse?'''

    print_slow(text)

    print('\n')
    print('*' * 25)
    print('Type the single letter, surrounded by () to make your decision')
    print('*' * 25)
    

    while True:
        choice = input('Please enter in your selection:  ')

        if choice == 'T':
            text = '''You hurriddly remove the clothes from the body and put them on. You drag the body to the middle of the room, face down, so the guards cound not see the wound.
You move back to the corner of the room and try to assume the same position the body was in. You close your eyes, slump your head, and wait for the door to open.
The door rushes open and you hear footsteps enter the room. Too afraid to open your eyes, you slow your breathing as the footsteps drawn closer to you.
The guards each grab one of your arms and drag you out of the room. You feel the atmosphere change, and the steps from the guards echo. You are drug around a corner and you barely open your eye
to check your surroundings. You see a long white hallway, terminated by a door. Above the door, you can barely make out what is says, Crematory. The guards open the door and drag you inside.
They lift you up onto a cold steel table, turn and leave the room.'''
            print_slow(text)
            print('You have chosen to trade places')
            room_two()
            break
            
        elif choice == 'S':
            text = '''As you stand over the body, you hear a the doors rush open, and two armed guards enter the room. One guard walk towards you, and punches you in the stomach.
You crumble to the ground gasping for air. The guard who hit you begins to laugh, pulls out his knife, and stabs you in the chest. As you lie on the floor bleeding out,
you regret not taking a chance to escape.'''
            #print('You have decided to stay')
            print_slow(text)
            print('\n')
            print_slow('Game Over...')
            sleep(5)
            break

        else:
            print('Please make a valid choice')
                

def room_two():
    print('You have escaped, and are now in the Crematory')


def room_three():
    print('This is the third room')
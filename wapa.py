# Script to a board game-like game called Warrior Path
# The game:
    # The game consist in the player to choose a path and fight the enemies
    # The game has stages, each stage has a different board
    # The stages:
        # The player starts with 1 HP in the first stage
        # On subsequent stages, the player starts with the HP he ended in the previous stage
        # Every stage has a boss that the player has to fight
        # Every boss has a HP that is the sum of the HP of the enemies of the stage minus the HP of the player
        # Every boss is at the last column of the board
        # You can choose to defeat the boss or not
# The player: 
# The player can only go on blocks up, left, right, upleft, upright and go back to the start of the stage
# Block of the board has a different event
# Each can hold only one event
# The events can be: 
# fight enemy
    # Every enemy has a different HP
    # If the player has more HP than the enemy, the player wins and gets the enemy's HP
    # If the player has the same HP than the enemy, the player wins and gets half of the enemy's HP rounded down
    # If the player has less HP than the enemy, the player loses and go back to the start of the stage
#   get a weapon
    # Every weapon gives the player a different amount of HP
    # The player can only have one weapon at a time
    # If the player gets a weapon, he gets the weapon's HP
    # If the player gets a weapon and already has a weapon, he gets the weapon's HP and loses the previous weapon's HP
#   get an armor
    # Every armor gives the player a different amount of HP
    # The player can only have one armor at a time
    # If the player gets an armor, he gets the armor's HP
    # If the player gets an armor and already has an armor, he gets the armor's HP and loses the previous armor's HP
#   nothing

import random
import time
import sys
import pygame
from pygame.locals import *
import pygame.mixer
import os

# Global variables
# The board is a grid of 5x5 as: '0,0', '0,1', etc.
board = [[0 for x in range(5)] for y in range(5)]
# The player starts with 1 HP
player_hp = 1
# The player starts with no weapon
player_weapon = 0
# The player starts with no armor
player_armor = 0
# The player starts at a random position in the first column of the board
player_initial_position = [random.randint(0,4),0]
# event_dict is a dictionary with the events and their HP
# HP is randomically generated based on the current player HP
event_dict = {'enemy':random.randint(1,player_hp),'weapon':random.randint(1,player_hp),'armor':random.randint(1,player_hp),'nothing':0, 'boss':0}
# The player starts at the initial position
player_position = player_initial_position
# The boss hp is the sum of the HP of the enemies of the stage minus the HP of the player
boss_hp = 0




def main():
    # The board has a 5x5 grid
    board_x = [0,1,2,3,4]
    board_y = [0,1,2,3,4]
    # The player starts with 1 HP
    player_hp = 1
    # The player starts with no weapon
    player_weapon = 0
    # The player starts with no armor
    player_armor = 0
    # The player starts at position 0, of board
    player_position = [board_x[0], board_y[0]]
    # Input to start the game
    print('You are a warrior and you have to defeat the enemies to get to the boss')
    print('You are at the top left corner of the board')
    m_input = input('choose a direction: 1 - right, 2 - down, 3 - downright: ')
    # If the player chooses to go right
    if m_input == 1:
        # the player goes right
        player_position[1] += 1
        # generate a random event
        generate_event()
        # call the movement function
        return movement(player_position)
    # If the player chooses to go down
    elif m_input == 2:
        # the player goes down
        player_position[0] += 1
        # generate a random event
        generate_event()
        # call the movement function
        return movement(player_position)
    # If the player chooses to go downright
    elif m_input == 3:
        # the player goes downright
        player_position[0] += 1
        player_position[1] += 1
        # generate a random event
        generate_event()
        # call the movement function
    return movement(player_position)
                







def movement(player_position): # this function should be recursive
    # Define all the possible movements based on the player position
    if player_position == [0,0] or player_position == [1,0] or player_position == [2,0] or player_position == [3,0] or player_position == [4,0]:
        # The player can only go right, down and downright
        m_input = input('choose a direction: 1 - right, 2 - down, 3 - downright: ')
        # If the player chooses to go right
        if int(m_input) == 1:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event(player_hp, player_weapon, player_armor, boss_hp)
            # call the movement function
            return movement(player_position)
        # If the player chooses to go down
        elif m_input == 2:
            # the player goes down
            player_position[0] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downright
        elif m_input == 3:
            # the player goes downright
            player_position[0] += 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    elif player_position == [0,1] or player_position == [1,1] or player_position == [2,1] or player_position == [3,1] or player_position == [4,1]:
        # The player can only go right, down, downright and downleft
        m_input = input('choose a direction: 1 - right, 2 - down, 3 - downright, 4 - downleft: ')
        # If the player chooses to go right
        if m_input == 1:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go down
        elif m_input == 2:
            # the player goes down
            player_position[0] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downright
        elif m_input == 3:
            # the player goes downright
            player_position[0] += 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downleft
        elif m_input == 4:
            # the player goes downleft
            player_position[0] += 1
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    elif player_position == [0,2] or player_position == [1,2] or player_position == [2,2] or player_position == [3,2] or player_position == [4,2]:
        # The player can only go right, down, downright, downleft and up
        m_input = input('choose a direction: 1 - right, 2 - down, 3 - downright, 4 - downleft, 5 - up: ')
        # If the player chooses to go right
        if m_input == 1:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go down
        elif m_input == 2:
            # the player goes down
            player_position[0] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downright
        elif m_input == 3:
            # the player goes downright
            player_position[0] += 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downleft
        elif m_input == 4:
            # the player goes downleft
            player_position[0] += 1
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go up
        elif m_input == 5:
            # the player goes up
            player_position[0] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    elif player_position == [0,3] or player_position == [1,3] or player_position == [2,3] or player_position == [3,3] or player_position == [4,3]:
        # The player can only go right, down, downright, downleft, up and upright
        m_input = input('choose a direction: 1 - right, 2 - down, 3 - downright, 4 - downleft, 5 - up, 6 - upright: ')
        # If the player chooses to go right
        if m_input == 1:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go down
        elif m_input == 2:
            # the player goes down
            player_position[0] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downright
        elif m_input == 3:
            # the player goes downright
            player_position[0] += 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downleft
        elif m_input == 4:
            # the player goes downleft
            player_position[0] += 1
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go up
        elif m_input == 5:
            # the player goes up
            player_position[0] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go upright
        elif m_input == 6:
            # the player goes upright
            player_position[0] -= 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    elif player_position == [0,4] or player_position == [1,4] or player_position == [2,4] or player_position == [3,4] or player_position == [4,4]:
        # The player can only go down, downleft, up and upright
        m_input = input('choose a direction: 1 - down, 2 - downleft, 3 - up, 4 - upright: ')
        # If the player chooses to go down
        if m_input == 1:
            # the player goes down
            player_position[0] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go downleft
        elif m_input == 2:
            # the player goes downleft
            player_position[0] += 1
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go up
        elif m_input == 3:
            # the player goes up
            player_position[0] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # If the player chooses to go upright
        elif m_input == 4:
            # the player goes upright
            player_position[0] -= 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    # If the player chooses to go back to the start of the stage
    elif m_input == 5:
        gb_input = input('Do you want to go back to the start of the stage? 1 - yes, 2 - no')
        # If the player chooses to go back to the start of the stage
        if gb_input == 1:
            # the player goes back to the start of the stage
            player_position = player_initial_position
        # generate a random event
        generate_event()
        # call the movement function
        return movement(player_position)

    




def generate_event(player_hp, player_weapon, player_armor, boss_hp):
    # event is a random event from the event_dict
    event = random.choice(list(event_dict.keys()))
    # if the event is an enemy
    if event == 'enemy':
        print('You found an enemy')
        # the player fights the enemy
        player_hp = fight_enemy(player_hp)
        return player_hp
    # if the event is a weapon
    elif event == 'weapon':
        print('You found a weapon')
        # the player gets the weapon
        player_weapon = get_weapon(player_weapon, player_hp)
        return player_weapon
    # if the event is an armor
    elif event == 'armor':
        print('You found an armor')
        # the player gets the armor
        player_armor = get_armor(player_armor)
        return player_armor
    # if the event is nothing
    elif event == 'nothing':
        print('You found nothing')
        # nothing happens
        pass
    elif event == 'boss':
        # Ask the player if he wants to fight the boss
        b_input = input('Do you want to fight the boss? 1 - yes, 2 - no')
        # if the player chooses to fight the boss
        if b_input == 1:
            # the player fights the boss
            player_hp = fight_boss(player_hp, boss_hp)
            return player_hp
        # if the player chooses not to fight the boss
        elif b_input == 2:
            # the player goes back to the last position
            player_position = player_position[0] - 1, player_position[1] - 1
            return player_position
    return event







def fight_enemy(event, player_hp, boss_hp):
    if event == 'enemy':
        # if the player has more HP than the enemy
        if player_hp > event_dict['enemy']:
            # the player wins and gets the enemy's HP
            player_hp += event_dict['enemy']
            print(f'You defeated the enemy and got {event_dict["enemy"]} HP')
            boss_hp += event_dict['enemy']
            print(f'The boss has {boss_hp} HP now')
        # if the player has the same HP than the enemy
        elif player_hp == event_dict['enemy']:
            # the player wins and gets half of the enemy's HP rounded down
            player_hp += event_dict['enemy']//2
            print(f'You defeated the enemy and got {event_dict["enemy"]//2} HP')
            boss_hp += event_dict['enemy']//2
            print(f'The boss has {boss_hp} HP now')
        # if the player has less HP than the enemy
        elif player_hp < event_dict['enemy']:
            # the player loses and go back to the start of the stage
            player_hp = 0
            print('You lost')
    return player_hp






def fight_boss(event, player_hp, boss_hp):
    if event == 'boss':
        # if the player has more HP than the boss
        if player_hp > boss_hp:
            # the player wins and gets the boss's HP
            player_hp += boss_hp
        # if the player has the same HP than the boss
        elif player_hp == boss_hp:
            # the player wins and gets half of the boss's HP rounded down
            player_hp += boss_hp//2
        # if the player has less HP than the boss
        elif player_hp < boss_hp:
            # the player loses and go back to the start of the stage
            player_hp = 0
    return player_hp
            








def get_weapon(event, player_hp, player_weapon):
    if event == 'weapon':
        # if the player gets a weapon, he gets the weapon's HP
        player_hp += event_dict['weapon']
        # if the player gets a weapon and already has a weapon
        if player_weapon != 0:
            # he gets the weapon's HP and loses the previous weapon's HP
            player_hp += event_dict['weapon']
            player_hp -= player_weapon
        # the player gets the weapon
        player_weapon = event_dict['weapon']









def get_armor(event, player_hp, player_armor):
    if event == 'armor':
        # if the player gets an armor, he gets the armor's HP
        player_hp += event_dict['armor']
        # if the player gets an armor and already has an armor
        if player_armor != 0:
            # he gets the armor's HP and loses the previous armor's HP
            player_hp += event_dict['armor']
            player_hp -= player_armor
        # the player gets the armor
        player_armor = event_dict['armor']









def nothing(event):
    if event == 'nothing':
        # nothing happens
        pass
    
# Run the program
main()
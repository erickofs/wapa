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
    # Main function
    # The game starts with the first stage
    stage = 1
    # The game starts with the first board
    board = [[0 for x in range(5)] for y in range(5)]
    # The player starts with 1 HP
    player_hp = 1
    # The player starts with no weapon
    player_weapon = 0
    # The player starts with no armor
    player_armor = 0
    # The player starts at position 0,0
    player_position = [0,0]
    # Input to start the game
    print('You are a warrior and you have to defeat the enemies to get to the boss')
    print('You are at the top left corner of the board')
    input('choose a direction: 1 - right, 2 - down, 3 - downright')
    # If the player chooses to go right
    if input == 1:
        # the player goes right
        player_position[1] += 1
        # generate a random event
        generate_event()
        # call the movement function
        movement(player_position)
    # If the player chooses to go down
    elif input == 2:
        # the player goes down
        player_position[0] += 1
        # generate a random event
        generate_event()
        # call the movement function
        movement(player_position)
    # If the player chooses to go downright
    elif input == 3:
        # the player goes downright
        player_position[0] += 1
        player_position[1] += 1
        # generate a random event
        generate_event()
        # call the movement function
        movement(player_position)
                







def movement(player_position): # this function should be recursive
    # if the player is at the top of the board
    if player_position[0] == 0:
        # the player can only go left or right
        input('Choose a direction: 1 - left, 2 - right')
        # if the player chooses to go left
        if input == 1:
            # the player goes left
            player_position[1] -= 1
            # generate a random event
            generate_event()
            return movement(player_position)
        # if the player chooses to go right
        elif input == 2:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    # if the player is at the bottom of the board
    elif player_position[0] == 4:
        # the player can only go left or right
        input('Choose a direction: 1 - left, 2 - right')
        # if the player chooses to go left
        if input == 1:
            # the player goes left
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # if the player chooses to go right
        elif input == 2:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    # if the player is not at the top or bottom of the board
    else:
        # the player can go up, left, right, upleft or upright
        input('Choose a direction: 1 - up, 2 - left, 3 - right, 4 - upleft, 5 - upright')
        # if the player chooses to go up
        if input == 1:
            # the player goes up
            player_position[0] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # if the player chooses to go right
        elif input == 3:
            # the player goes right
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # if the player chooses to go upleft
        elif input == 4:
            # the player goes upleft
            player_position[0] -= 1
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # if the player chooses to go upright
        elif input == 5:
            # the player goes upright
            player_position[0] -= 1
            player_position[1] += 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
        # if the player chooses to go left
        elif input == 2:
            # the player goes left
            player_position[1] -= 1
            # generate a random event
            generate_event()
            # call the movement function
            return movement(player_position)
    return player_position

    




def generate_event():
    # event is a random event from the event_dict
    event = random.choice(list(event_dict.keys()))
    # if the event is an enemy
    if event == 'enemy':
        # the player fights the enemy
        player_hp = fight_enemy(player_hp)
    # if the event is a weapon
    elif event == 'weapon':
        # the player gets the weapon
        player_weapon = get_weapon(player_weapon)
    # if the event is an armor
    elif event == 'armor':
        # the player gets the armor
        player_armor = get_armor(player_armor)
    # if the event is nothing
    elif event == 'nothing':
        # nothing happens
        pass
    elif event == 'boss':
        # Ask the player if he wants to fight the boss
        input('Do you want to fight the boss? 1 - yes, 2 - no')
        # if the player chooses to fight the boss
        if input == 1:
            # the player fights the boss
            player_hp = fight_boss(player_hp)
        # if the player chooses not to fight the boss
        elif input == 2:
            # the player goes back to the last position
            player_position = player_position[0] - 1, player_position[1] - 1
    return event







def fight_enemy(event):
    if event == 'enemy':
        # if the player has more HP than the enemy
        if player_hp > event_dict['enemy']:
            # the player wins and gets the enemy's HP
            player_hp += event_dict['enemy']
            boss_hp += event_dict['enemy']
        # if the player has the same HP than the enemy
        elif player_hp == event_dict['enemy']:
            # the player wins and gets half of the enemy's HP rounded down
            player_hp += event_dict['enemy']//2
            boss_hp += event_dict['enemy']//2
        # if the player has less HP than the enemy
        elif player_hp < event_dict['enemy']:
            # the player loses and go back to the start of the stage
            player_hp = 0






def fight_boss(event):
    if event == 'boss':
        # the boss has a HP that is the sum of the HP of the enemies of the stage minus the HP of the player
        boss_hp = 0
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
            








def get_weapon(event):
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









def get_armor(event):
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
    
main()
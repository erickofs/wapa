# WarriorPath.py

import random
import numpy as np
import motion
import time
from events import Events
from board import Board

class WarriorPath:
    def __init__(self):
        self.board = Board()
        self.events = Events()
        self.motion = motion.Motion()  # Instanciando a classe Motion
        self.first_play = True
        self.reset_game()

    def reset_game(self):
        start_x = random.randint(0, 7)
        start_y = random.randint(0, 7)
        self.player = {'position': (start_x, start_y), 'HP': 10, 'weapon': 0, 'armor': 0}
        self.boss_position = (random.randint(0, 7), random.randint(0, 7))  # Posição aleatória do boss
        self.game_over = False

    def display_introduction(self):
        intro_text = self.motion.intro_text()
        for line in intro_text.split('\n'):
            print(line)
            time.sleep(0.05)  # Breve pausa para efeito dramático

    def display_revived_message(self):
        revived_text = self.motion.revived_text()
        for line in revived_text.split('\n'):
            print(line)
            time.sleep(0.05)  # Breve pausa para efeito dramático

    def start_game(self):
        if self.first_play:
            self.display_introduction()
            self.first_play = False
        else:
            self.display_revived_message()

        self.board.create_board()
        while not self.game_over:
            print(f"\nCurrent position: {self.player['position']}")
            print(f"Current HP: {self.player['HP']}, Weapon: {self.player['weapon']}, Armor: {self.player['armor']}")
            direction = input("Choose a direction (north, south, east, west): ").lower()
            if direction in ['north', 'south', 'east', 'west']:
                new_position = self.board.move(direction, self.player['position'])
                if new_position != self.player['position']:
                    self.player['position'] = new_position
                    if new_position == self.boss_position:
                        print("You have found the boss!")
                        self.player['HP'] = self.events.fight_boss(self.player['HP'], self.player['weapon'], self.player['armor'])
                        if self.player['HP'] <= 0:
                            self.game_over = True
                    else:
                        self.process_event(new_position)
                if self.player['HP'] <= 0:
                    print(self.motion.game_over())  # Exibe a imagem de Game Over
                    self.game_over = True
            else:
                print("Invalid direction. Please choose 'north', 'south', 'east', or 'west'.")

        self.end_game()

    def process_event(self, position):
        event = self.board.get_event(position)  # Obter o evento baseado na posição
        if event == 0:
            print(self.motion.nothing_happens())  # Exibe a imagem de vento soprando quando nada acontece
        elif event == 1:
            print(self.motion.enemy_encounter())  # Exibe a imagem de olhos maliciosos ao encontrar um inimigo
            self.player['HP'] = self.events.fight_enemy(self.player['HP'], self.player['weapon'], self.player['armor'])
            if self.player['HP'] > 20:
                print("You feel a sense of foreboding... the enemies are becoming stronger as you gain power.")
        elif event == 2:
            self.player['weapon'] = self.events.get_weapon(self.player['weapon'], self.player['HP'])
        elif event == 3:
            self.player['armor'] = self.events.get_armor(self.player['armor'], self.player['HP'])
        else:
            print(self.motion.nothing_happens())  # Exibe a imagem de vento soprando quando nada acontece

    def end_game(self):
        while True:
            restart = input("\nWould you like to restart the game? (yes/no): ").lower()
            if restart == "yes":
                self.reset_game()
                self.start_game()
                break
            elif restart == "no":
                print("Thank you for playing Warrior's Path. Farewell, brave warrior!")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    game = WarriorPath()
    game.start_game()

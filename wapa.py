import random
import numpy as np
import time
import keyboard
from events import Events
from board import Board
from movements import Movements
from player import Player
from motion import Motion

class WarriorPath:
    def __init__(self):
        self.motion = Motion()
        self.board = Board()
        self.reset_game()
        self.movements = Movements(self.player)
        self.events = Events(self.player, self.board)
        self.first_play = True
        self.game_over = False

    def start_game(self):
        if self.first_play:
            self.events.display_introduction()
            self.first_play = False
            self.game_over = False
        else:
            self.events.display_revived_message()
            self.game_over = False

        self.board.create_board()
        while not self.game_over:
            print(f"\nCurrent position: {self.player.position}")
            print(f"Current Status: HP: {self.player.hp}, Weapon: {self.player.weapon}, Armor: {self.player.armor}")
            print("Press the arrow keys to move.")

            direction = self.movements.key_listener()  # Obtém a direção do jogador
            current_position = self.player.position  # Salva a posição atual
            new_position = self.movements.move(direction)  # Calcula a nova posição

            if new_position == current_position:
                print("You cannot move in that direction. Try a different move.")
                continue  # Pede uma nova entrada ao jogador

            self.player.position = new_position  # Atualiza a posição do jogador

            if new_position == self.board.boss_position:
                print("You have found the boss!")
                self.player.hp = self.events.fight_boss(self.player.hp, self.player.weapon, self.player.armor)
                if self.player.hp <= 0:
                    self.game_over = True
                continue

            self.events.process_event(new_position)  # Processa o evento na nova posição

            if self.player.hp <= 0:
                print(self.motion.game_over())  # Imprime a mensagem de "Game Over"
                self.game_over = True

        self.end_game()

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

    def reset_game(self):
        start_x = random.randint(0, 7)
        start_y = random.randint(0, 7)
        self.player = Player(start_x, start_y)
        print(f"Player starting position: {self.player.position}")

if __name__ == "__main__":
    game = WarriorPath()
    game.start_game()

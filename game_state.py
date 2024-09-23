# game_state.py

import random
import time

class States:
    def __init__(self, player, board, movements, events):
        self.player = player
        self.board = board
        self.movements = movements
        self.events = events

    def start_game(self):
        while True:
            print(f"Current position: {self.player.position}")
            print(f"Current Status: HP: {self.player.hp}, Weapon: {self.player.weapon}, Armor: {self.player.armor}")
            
            direction = self.movements.key_listener()  # Obtém a direção usando a função key_listener
            
            new_position = self.movements.move(direction, self.player.position)
            if new_position == self.player.position:
                print("You can't move in that direction.")
            else:
                self.player.position = new_position
                self.events.process_event(new_position)

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
        self.player.position = (start_x, start_y)
        self.player.hp = 10
        self.player.weapon = 0
        self.player.armor = 0
        self.board.boss_position = (random.randint(0, 7), random.randint(0, 7))
        print(f"Player starting position: {self.player.position}")
#board.py

import numpy as np
import random

class Board:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)  # Initialize an 8x8 board with zeros
        self.explored = np.zeros((8, 8), dtype=bool)  # Track explored blocks with a boolean matrix
        self.boss_position = None

    def create_board(self):
        # Randomly assign events to the board
        for i in range(8):
            for j in range(8):
                self.board[i, j] = random.choices([0, 1, 2, 3], weights=[4, 3, 2, 1], k=1)[0]
        # Randomly place the boss
        boss_x = random.randint(0, 7)
        boss_y = random.randint(0, 7)
        self.boss_position = (boss_x, boss_y)

    def is_position_explored(self, position):
        x, y = position
        return self.explored[x, y]

    def mark_position_explored(self, position):
        x, y = position
        self.explored[x, y] = True

    def get_event(self, position):
        x, y = position
        return self.board[x, y]

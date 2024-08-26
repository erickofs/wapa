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

    def move(self, direction, player_position):
        x, y = player_position
        if direction == 'north':
            if x > 0:
                x -= 1
            else:
                north_messages = [
                    "You can't move north. There's nothing but a void there.",
                    "A steep mountain blocks your way to the north.",
                    "You see a dense fog up ahead, making it impossible to proceed further.",
                    "The path ends abruptly, with sheer cliffs preventing further progress north."
                ]
                print(random.choice(north_messages))
                return player_position
        elif direction == 'south':
            if x < 7:
                x += 1
            else:
                south_messages = [
                    "You can't move south. The path ends in an abyss.",
                    "A deep chasm stretches out before you to the south, impassable and deadly.",
                    "Dark waters block your path, with no way to continue south.",
                    "The ground crumbles away to the south, leading to a bottomless pit."
                ]
                print(random.choice(south_messages))
                return player_position
        elif direction == 'west':
            if y > 0:
                y -= 1
            else:
                west_messages = [
                    "You can't move west. A steep cliff blocks your way.",
                    "The western horizon is filled with impassable mountains.",
                    "The path to the west is blocked by a dense and thorny forest.",
                    "A massive stone wall looms to the west, impossible to scale."
                ]
                print(random.choice(west_messages))
                return player_position
        elif direction == 'east':
            if y < 7:
                y += 1
            else:
                east_messages = [
                    "You can't move east. There's nothing but darkness beyond.",
                    "A vast desert stretches out to the east, with no end in sight.",
                    "The eastern skies are filled with ominous storm clouds, making it unsafe to proceed.",
                    "You see the edge of the world to the east, where everything falls into the void."
                ]
                print(random.choice(east_messages))
                return player_position
        return (x, y)  # Return the new player position

    def get_event(self, position):
        x, y = position
        if self.explored[x, y]:  # Check if the block has already been explored
            return 0  # Always return 'nothing' for previously explored blocks
        else:
            self.explored[x, y] = True  # Mark the block as explored
            return self.board[x, y]  # Return the event as per the initial logic

import numpy as np
import random

class Board:
    def __init__(self):
        # A board with method zeros, containing a shape of 8x8 with data type (dtype) int
        # This will return int blocks (1x1, 1x2, 1x3, etc)
        self.blocks = np.zeros((8, 8), dtype=int)

    
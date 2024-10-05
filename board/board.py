import numpy as np
import random

class Block():
    def __init__(self, position):
        self.position = position  # Por exemplo, uma tupla (x, y)
        self.events = []       # Lista de eventos ocorridos no bloco
    
    def add_event(self, event):
        self.events.append(event)
    
    def __repr__(self):
        return f"Bloco(posicao={self.position})"

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = self.create_blocks()
    
    def create_blocks(self):
        blocks = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                block = Block(position=(x, y))
                line.append(block)
            blocks.append(line)
        return blocks
    
    def get_block(self, x, y):
        return self.blocks[y][x]
    
    def __repr__(self):
        return f"Tabuleiro({self.width}x{self.height})"


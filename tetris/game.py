from grid import Grid
from tetrominos import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [I(), J(), L(), O(), S(), T(), Z()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [I(), J(), L(), O(), S(), T(), Z()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

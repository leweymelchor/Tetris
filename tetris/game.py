from grid import Grid
from tetrominos import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.tetrominos = [I(), J(), L(), O(), S(), T(), Z()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.mp3")
        self.clear_sound = pygame.mixer.Sound("sounds/tetris-clear.mp3")
        self.land_sound = pygame.mixer.Sound("sounds/tetris-land.mp3")
        self.over_sound = pygame.mixer.Sound("sounds/game-over.mp3")
        pygame.mixer.music.load("sounds/tetris-theme.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 250
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 750
        elif lines_cleared >= 5:
            self.score += 1000
        self.score += move_down_points

    def get_random_block(self):
        if len(self.tetrominos) == 0:
            self.tetrominos = [I(), J(), L(), O(), S(), T(), Z()]
        block = random.choice(self.tetrominos)
        self.tetrominos.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
            self.land_sound.play()
            self.land_sound.set_volume(0.3)

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.clear_sound.set_volume(0.2)
        self.update_score(rows_cleared, 0)

        if self.block_fits() == False:
            self.game_over = True
            pygame.time.delay(100)
            self.over_sound.play()
            self.over_sound.set_volume(1)

    def reset(self):
        self.grid.reset()
        self.tetrominos = [I(), J(), L(), O(), S(), T(), Z()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()
            self.rotate_sound.set_volume(0.5)

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.fill(screen, 270, 270)

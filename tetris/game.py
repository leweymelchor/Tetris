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
        self.multiplier = 1
        if self.multiplier > 4:
            self.multiplier = 4

        self.cleared_lines = 0

        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.mp3")
        self.clear_sound = pygame.mixer.Sound("sounds/tetris-clear.mp3")
        self.land_sound = pygame.mixer.Sound("sounds/tetris-land.mp3")
        self.over_sound = pygame.mixer.Sound("sounds/game-over.mp3")

        pygame.mixer.music.load("sounds/tetris-theme.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += (100 * self.multiplier)
            self.cleared_lines += 1
        elif lines_cleared == 2:
            self.score += (300 * self.multiplier)
            self.cleared_lines += 2
        elif lines_cleared == 3:
            self.score += (600 * self.multiplier)
            self.cleared_lines += 3
        elif lines_cleared == 4:
            self.score += (1000 * self.multiplier)
            self.cleared_lines += 4
            self.multiplier += 1
        self.score += (move_down_points * self.multiplier)

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

    def add_speed(self):
        self.speed_up = 0

        if self.cleared_lines >= 10 and self.cleared_lines < 20:
            self.speed_up += 75
        elif self.cleared_lines >= 20 and self.cleared_lines < 30:
            self.speed_up += 100
        elif self.cleared_lines >= 30 and self.cleared_lines < 40:
            self.speed_up += 150
        elif self.cleared_lines >= 40 and self.cleared_lines < 50:
            self.speed_up += 200
        elif self.cleared_lines >= 50 and self.cleared_lines < 60:
            self.speed_up += 250
        elif self.cleared_lines >= 60:
            self.speed_up += 300

        return self.speed_up

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
            if self.speed_up >= 400:
                pygame.time.delay(600)
            else:
                pygame.time.delay(300)
            self.over_sound.play()
            self.over_sound.set_volume(1)

    def reset(self):
        self.grid.reset()
        self.tetrominos = [I(), J(), L(), O(), S(), T(), Z()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.multiplier = 1
        self.cleared_lines = 0

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

    # def tet_speed(self):
    #     speed = 1
    #     if self.cleared_lines >= 10 and self.cleared_lines / 10 == self.cleared_lines // 10:
    #         speed -= 20

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 235)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 220)
        else:
            self.next_block.fill(screen, 270, 215)

import pygame, sys
from game import Game

pygame.init
dark_blue = (44, 44, 127)
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

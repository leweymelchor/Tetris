import pygame, sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

font = pygame.font.Font('freesansbold.ttf', 16)
restart_message = font.render('Press any key to play again...', True, white)
textRect = restart_message.get_rect()
textRect.center = (300 // 2, 600 // 2)

clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 20)


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()

        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()


    screen.fill(dark_blue)
    game.draw(screen)
    if game.game_over == True:
        screen.fill(black)
        screen.blit(restart_message, textRect)

    pygame.display.update()
    clock.tick(60)

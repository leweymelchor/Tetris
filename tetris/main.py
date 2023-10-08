import pygame, sys
from game import Game
from colors import Colors

pygame.init()

X = 500
Y = 620

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Tetris")

font = pygame.font.Font('freesansbold.ttf', 20)
restart_message = font.render('Press any key to play again...', True, Colors.white)
textRect = restart_message.get_rect()
textRect.center = (X // 2), (Y // 2)

score_text = font.render('Score', True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)
next_text = font.render('Next', True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)

clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


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


    screen.fill(Colors.dark_blue)
    screen.blit(score_text, (365, 20, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(next_text, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    game.draw(screen)
    if game.game_over == True:
        screen.fill(Colors.dark_blue)
        screen.blit(restart_message, textRect)

    pygame.display.update()
    clock.tick(60)

import pygame, sys
from game import Game
from colors import Colors

pygame.init()

X = 500
Y = 620

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Tetris")

# TEXT
font = pygame.font.Font('fonts/Rajdhani-Medium.ttf', 20)
restart_message = font.render('Press any key to play again...', True, Colors.white)
textRect = restart_message.get_rect()
textRect.center = (X // 2), (Y // 2)

score_text = font.render('Score', True, Colors.white)
score_rect = pygame.Rect(320, 50, 170, 60)
next_text = font.render('Next', True, Colors.white)
next_rect = pygame.Rect(320, 175, 170, 150)
x_text = font.render('x', True, Colors.white)
mult_text = font.render('Multiplier', True, Colors.white)
mult_rect = pygame.Rect(315, 530, 170, 60)
cleared_text = font.render('Lines Cleared', True, Colors.white)
cleared_rect = pygame.Rect(315, 400, 170, 60)

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.3)
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s and game.game_over == False:
                game.rotate_sound.play()
                game.rotate_sound.set_volume(0.4)
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP or event.key == pygame.K_w and game.game_over == False:
                game.rotate()

        if game.game_over == False:
            increase = game.add_speed()
            speed = 400 - increase
            GAME_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(GAME_UPDATE, speed)

        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()


    score_value = font.render(str(game.score), True, Colors.white)
    mult_value = font.render(str(game.multiplier), True, Colors.white)
    cleared_value = font.render(str(game.cleared_lines), True, Colors.white)

    screen.fill(Colors.dark_blue)

    screen.blit(score_text, (380, 15, 50, 50))
    screen.blit(next_text, (385, 140, 50, 50))
    screen.blit(mult_text, (365, 490, 50, 50))
    screen.blit(cleared_text, (350, 360, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, mult_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, cleared_rect, 0, 10)

    game.draw(screen)

    score = screen.blit(score_value, score_value.get_rect(
        centerx = score_rect.centerx, centery = score_rect.centery))


    mult = screen.blit(mult_value, mult_value.get_rect(
        centerx = mult_rect.centerx, centery = mult_rect.centery))
    screen.blit(x_text, (385, 547, 50, 50))

    cleared = screen.blit(cleared_value, cleared_value.get_rect(
        centerx = cleared_rect.centerx, centery = cleared_rect.centery))

    if game.game_over == True:
        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play(0)

        screen.fill(Colors.dark_blue)
        screen.blit(score_text, (360, 20, 50, 50))
        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        score = screen.blit(score_value, score_value.get_rect(
            centerx = score_rect.centerx, centery = score_rect.centery))

        screen.blit(restart_message, textRect)



    pygame.display.update()
    clock.tick(30)

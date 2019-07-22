from Ball import Ball
from Player import Player
import pygame
import sys

HEIGHT = 600
WIDTH = 800
delta = 0.0
pygame.init()

font = pygame.font.SysFont("comicsans", 60, True)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player_one = Player(20, HEIGHT/2-40)
player_two = Player(WIDTH-35, HEIGHT/2-40)
ball = Ball(15, 15)
clock = pygame.time.Clock()
game_over = False
score = [0, 0]

while not game_over:
    delta += clock.tick()/1000
    while delta > 0.005:
        screen.fill((10, 10, 10))
        ball.move_ball()
        delta -= 0.005
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
        ball.check_platform_collisions(player_one.platform, -1)
        ball.check_platform_collisions(player_two.platform, 1)
        player_one.move_player(1, screen)
        player_two.move_player(2, screen)

        if ball.check_wall_collisions(HEIGHT, WIDTH, score):
            ball = Ball(15, 15)
            player_one = Player(20, HEIGHT / 2 - 40)
            player_two = Player(WIDTH - 35, HEIGHT / 2 - 40)

        scoreboard_one = font.render(str(score[0]), 1,(255, 0, 0))
        scoreboard_two = font.render(str(score[1]), 1, (0, 0, 255))
        screen.blit(scoreboard_one, (600, 20))
        screen.blit(scoreboard_two, (200, 20))

        pygame.draw.rect(screen, (255, 255, 255), ball.pilka)
        pygame.draw.rect(screen, (0, 0, 255), player_one.platform)
        pygame.draw.rect(screen, (255, 0, 0), player_two.platform)
        pygame.display.flip()


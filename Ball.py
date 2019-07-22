import pygame
import random
import math
from math import pow
from Player import Player

clock = pygame.time.Clock()

class Ball:
    def __init__(self, h, w):
        direction = random.randint(1,2)
        self.height = h
        self.width = w
        Xpos = 400
        Ypos = 300
        self.const_speed = 4
        if direction == 1:
            self.speed = [2,0]
        if direction == 2:
            self.speed = [-2,0]
        self.pilka = pygame.Rect((Xpos, Ypos), (self.width, self.height))
        self.timer = 0.0
    def move_ball(self):
        self.timer += clock.tick()
        if self.timer > 3000:
            self.pilka.move_ip(self.speed)

    def check_wall_collisions(self, HEIGHT, WIDTH, score):
        if self.pilka.x <= 0:
            score[0] +=1
            return True
        if self.pilka.x >= WIDTH-self.width:
            score[1] += 1
            return True
        if self.pilka.y <= 0:
            self.speed[1] *= -1
            return False
        if self.pilka.y >= HEIGHT-self.height:
            self.speed[1] *= -1
            return False

    def check_platform_collisions(self, platform, direction):
        if self.pilka.colliderect(platform):
            y_b = self.pilka.top + self.pilka.h/2
            y_p = platform.top + platform.h/2
            factor = (y_b - y_p) / (platform.h/2+ self.pilka.h/2)
            print(factor)
            print(y_b)
            print(y_p)
            if abs(factor) < 1.0:
                    self.speed[1] = factor*self.const_speed

            self.speed[0] = (4 - abs(self.speed[1])) * -direction
            if abs(factor) > 1.0:
                self.speed[0] = 2 * direction
                self.speed[1] = self.const_speed * factor

            if self.speed[0] < 1 and self.speed[0] > 0:
                self.speed[0] = 1
            elif self.speed[0] > -1 and self.speed[0] < 0:
                self.speed[0] = 1

        print(self.speed[1])

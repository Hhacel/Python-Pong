import pygame

class Player:

    def __init__(self, posx, posy):
        self.height = 80
        width = 15
        self.platform = pygame.Rect((posx, posy), (width, self.height))

    def move_player(self, player_number, screen):
        pygame.event.get()
        if player_number == 2:
            if pygame.key.get_pressed()[pygame.K_DOWN] and self.platform.y < screen.get_size()[1] - self.height:
                self.platform.y += 3
            if pygame.key.get_pressed()[pygame.K_UP] and self.platform.y > 0:
                self.platform.move_ip((0, -3))
        if player_number == 1:
            if pygame.key.get_pressed()[pygame.K_s] and self.platform.y < screen.get_size()[1] - self.height:
                self.platform.y += 3
            if pygame.key.get_pressed()[pygame.K_w] and self.platform.y > 0:
                self.platform.move_ip((0, -3))
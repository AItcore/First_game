import pygame
from random import randint


class Player(pygame.sprite.Sprite):

    def __init__(self, ai_settings):
        super(Player, self).__init__()
        self.width = ai_settings.player_width
        self.speed = ai_settings.player_speed
        self.color = (randint(0, 210), randint(0, 210), randint(0, 210))

        self.x = randint(0, ai_settings.display_width)
        self.y = randint(0, ai_settings.display_height)

        self.surf = pygame.Surface(ai_settings.display_size)
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


class Bot():
    
    def __init__(self, ai_settings):
        self.width = ai_settings.player_width
        self.speed = ai_settings.player_speed
        self.color = (randint(0, 210), randint(0, 210), randint(0, 210))

        self.x = randint(0, ai_settings.display_width)
        self.y = randint(0, ai_settings.display_height)

        self.near_food = None
        self.near_food_x = None
        self.near_food_y = None

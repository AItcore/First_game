from settings import Settings
import game_functions as gf
from character import Bot, Player
import update_screen
import pygame


bots = []

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode(ai_settings.display_size)
    pygame.display.set_caption("Agar.io")
    for i in range(0, ai_settings.count_bots):
        bots.append(Bot(ai_settings))
    player = Player(ai_settings)
    while True:
        update_screen.food_create(screen, ai_settings, player, bots)
        gf.check_events(player, bots, ai_settings)
        screen.fill(ai_settings.bg_color)
        update_screen.update(player, ai_settings, bots)
        update_screen.draw(player, screen, bots)
run_game()
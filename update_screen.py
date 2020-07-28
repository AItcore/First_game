import pygame
from food import Food
from character import Bot, Player


foods = [] # лист расположений еды

def draw(player, screen, bots):
    pygame.draw.circle(screen, player.color, (player.x, player.y), round(player.width))
    for food in foods:
        pygame.draw.circle(screen, food.color, (food.x, food.y), food.width)
    for bot in bots:
        pygame.draw.circle(screen, bot.color, (bot.x, bot.y), round(bot.width))
    pygame.display.flip()

def update(player, ai_settings, bots):
    if player.moving_up:
        player.y -= player.speed
    if player.moving_down:
        player.y += player.speed
    if player.moving_left:
        player.x -= player.speed
    if player.moving_right:
        player.x += player.speed
    
    if player.x > ai_settings.display_width:
        player.x = ai_settings.display_width
    elif player.x < 0:
        player.x = 0

    if player.y > ai_settings.display_height:
        player.y = ai_settings.display_height
    if player.y < 0:
        player.y = 0
    for bot in bots:
        if bot.x > ai_settings.display_width:
            bot.x = ai_settings.display_width
        elif bot.x < 0:
            bot.x = 0

        if bot.y > ai_settings.display_height:
            bot.y = ai_settings.display_height
        if bot.y < 0:
            bot.y = 0
    
# БОТЫ СУКИ ЖРАТЬ НЕ УМЕЮТ!!!!
def food_eating(player, bots, ai_settings):
    for food in foods:
        if abs(player.x - food.x) < player.width and abs(player.y - food.y) < player.width:
            player.width += food.score/50
            foods.remove(food)
        for bot in bots:
            if abs(bot.x - food.x) < bot.width and abs(bot.y - food.y) < bot.width:
                bot.width += food.score/50
                bot.near_food = None
                foods.remove(food) # <-- Здесь ошибка и далее
        #     # if abs(player.x - bot.x) < player.width and abs(player.y - bot.y) < player.width and player.width > bot.width:
        #     #     player.width += bot.width
        #     #     bots.remove(bot)
        #     #     bots.append(ai_settings)
        #     #     break
        #     if abs(player.x - bot.x) > player.width and abs(player.y - bot.y) > player.width and player.width < bot.width:
        #         bot.width += player.width
        #         # player = Player(ai_settings)


def food_create(screen, ai_settings, player, bots):
    if len(foods) < ai_settings.food_count:
        foods.append(Food(ai_settings))
    food_eating(player, bots, ai_settings)

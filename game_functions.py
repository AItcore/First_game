import pygame
import sys
from update_screen import foods


def check_events(player, bots, ai_settings):
    bots_move(bots, player, ai_settings)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, player)
        elif event.type == pygame.KEYUP:
            keyup(event, player)        

def keydown(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    if event.key == pygame.K_LEFT:
        player.moving_left = True
    if event.key == pygame.K_DOWN:
        player.moving_down = True
    if event.key == pygame.K_UP:
        player.moving_up = True

def keyup(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    if event.key == pygame.K_LEFT:
        player.moving_left = False
    if event.key == pygame.K_DOWN:
        player.moving_down = False
    if event.key == pygame.K_UP:
        player.moving_up = False

def bots_move(bots, player, ai_settings):
    for bot in bots:
        for bt in bots:
            if abs(bot.x - bt.x) < 100 + bt.width and bot.width < bt.width and abs(bot.y - bt.y) < 100 + bt.width:
                if bot.x > bt.x:
                    bot.x += ai_settings.player_speed
                else:
                    bot.x -= ai_settings.player_speed
                if bot.y > player.y:
                    bot.y += ai_settings.player_speed
                else:
                    bot.y -= ai_settings.player_speed
        if abs(bot.x - player.x) < 100 + player.width and bot.width < player.width and abs(bot.y - player.y) < 100 + player.width:
            if bot.x > player.x:
                bot.x += ai_settings.player_speed
            else:
                bot.x -= ai_settings.player_speed
            if bot.y > player.y:
                bot.y += ai_settings.player_speed
            else:
                bot.y -= ai_settings.player_speed
        if bot.near_food == None:
            bot.near_food = bot.x + bot.y - foods[0].x - foods[0].y
            bot.near_food_x = foods[0].x 
            bot.near_food_y = foods[0].y
            for food in foods:
                if bot.near_food > bot.x + bot.y - food.x - food.y:
                    bot.near_food = bot.x + bot.y - foods[0].x - foods[0].y
                    bot.near_food_x = food.x 
                    bot.near_food_y = food.y
        if bot.x < bot.near_food_x:
            bot.x += bot.speed
        elif bot.x > bot.near_food_x:
            bot.x -= bot.speed
        if bot.y < bot.near_food_y:
            bot.y += bot.speed
        elif bot.y > bot.near_food_y:
            bot.y -= bot.speed
        bot.near_food = None
                    
                    
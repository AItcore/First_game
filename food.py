from random import randint


class Food():
    
    def __init__(self, ai_settings):
        self.width = ai_settings.food_width
        self.score = ai_settings.food_score
        self.color = (randint(0, 210), randint(0, 210), randint(0, 210))
        self.x = randint(0, ai_settings.display_width)
        self.y = randint(0, ai_settings.display_height)
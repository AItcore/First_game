from os import path


class Settings():

    def __init__(self):
        self.parent_dir = path.dirname(path.abspath(__file__)+'\\img\\' ) # если вдруг понадобятся картиники

        self.count_bots = 5

        self.food_width = 5         # 
        self.food_score = 3         # настройки еды
        self.food_count = 500       #

        self.player_width = 15 # стартовое значение игрока
        self.player_speed = 2

        self.bg_color = (255, 255, 255)                                # Цвет фона
        self.display_width = 1200                                      # 
        self.display_height = 800                                      # Размер приложения
        self.display_size = (self.display_width, self.display_height)  #
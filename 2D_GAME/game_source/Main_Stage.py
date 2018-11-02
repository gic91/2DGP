from pico2d import *


class Stage:
    def __init__(self):
        self.image = load_image('game_sprite\\main_background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)


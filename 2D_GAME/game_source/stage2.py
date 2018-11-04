from pico2d import *

import game_framework
import random
import Main_Stage

time_time = Main_Stage.time_time



class Back:
    def __init__(self):
        self.image = load_image('game_sprite\\stage2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)

class Time:
    def __init__(self):
        self.timer =0
        self.font = load_font('ENCR10B.TTF', 60)
        self.main_time =100
        self.timer2=100
    def update(self):
        global time_time
        self.timer =int(get_time())
        self.main_time = self.timer2 - self.timer
        time_time = self.main_time
        if self.main_time ==0:
            game_framework.quit()
    def draw(self):
        self.font.draw(1060, 670, '%3d' % self.main_time, (255, 0, 0))

class Hero:
    def __init__(self):
        self.image = load_image('game_sprite\\stage2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)



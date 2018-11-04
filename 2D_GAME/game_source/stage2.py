from pico2d import *

import game_framework
import random
import Main_Stage
import stage2_state

time_time = Main_Stage.time_time


X=[]
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
        self.image = load_image('game_sprite\\stage2_item.png')
        self.state =0
    def update(self):
        global X
        if stage2_state.key ==1:
            self.state = 1
        elif stage2_state.key ==2:
            self.state = 2
        elif stage2_state.key ==3:
            self.state = 3
        elif stage2_state.key ==4 or stage2_state.key ==5  or stage2_state.key ==6:
            self.state = 0
    def draw(self):
        if self.state ==0: #<-
            self.image.clip_draw(80, 250, 90, 130, 1160,1560)
        elif self.state == 1: #l
            self.image.clip_draw(80, 250, 90, 130, 60,560)
        elif self.state == 2: #->
            self.image.clip_draw(80, 250, 90, 130, 60,300)
        elif self.state == 3:
            self.image.clip_draw(80, 250, 90, 130,60,430)


class Bomb:
    def __init__(self):
        global X
        self.image = load_image('game_sprite\\stage2_item.png')
        self.Y=[0,1,2,1,2,0,1,2,0,2]
        X=[]
        self.count =10
        for i in range(0,self.count):
            X.append(i*0)
        self.timer=0
        self.num=0
    def update(self):
        global X
        self.timer +=1
        if self.timer %50 ==0:
            self.timer=0
            self.num+=1
            if self.num >10:
                self.num=10
        for i in range(0, self.num):
            X[i] += 5

    def draw(self):
        global X
        for j, i in enumerate(self.Y):
            if self.Y[j]==0: #<-
                self.image.clip_draw(0, 300, 50, 100, 1200-X[j], 560)
            elif self.Y[j] == 1: #l
                self.image.clip_draw(0, 300, 50, 100, 1200-X[j], 300)
            elif self.Y[j] == 2: #->
                self.image.clip_draw(0, 300, 50, 100, 1200-X[j], 430)

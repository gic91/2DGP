from pico2d import *
import random

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,100),90
        self.frame =random.randint(0,7)
        self.image = load_image('run_animation.png')
        self.random_move=random.randint(3,10)

    def update(self):
        self.frame = (self.frame+1) %8
        self.x +=self.random_move

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 600
        self.image_small = load_image('ball21x21.png')
        self.image_big = load_image('ball41x41.png')
        self.random_move = random.randint(3, 10)
        self.ball_shape = random.randint(1, 2)
    def update(self):
        if self.y <=70:
            self.y=70

        else:
            self.y -=self.random_move

    def draw(self):
        if self.ball_shape==1:
            self.image_small.draw(self.x, self.y)

        else:
            self.image_big.draw(self.x, self.y)
# initialization code
open_canvas()

team =[Boy() for i in range(11)]
Balls =[Ball() for i in range(20)]
grass = Grass()
running =True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for Ball in Balls:
        Ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for Ball in Balls:
        Ball.draw()
    update_canvas()

    delay(0.05)

# finalization code

close_canvas()
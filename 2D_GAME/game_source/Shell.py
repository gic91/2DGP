from pico2d import *

import math
import game_world
import game_framework
import stage1_state
import stage1
import random
# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RAD = PIXEL_PER_METER * 3
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 8

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN,UP_UP= range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP
}


# Boy States
coin =None
box1 =False
box2=False
box3=False
box4=False
class IdleState:

    @staticmethod
    def enter(boy, event):
        global coin
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.timer2 = int(get_time())
        if boy.Coin_count ==4:
            if event == UP_DOWN:
                if boy.x > 920 and boy.x<1100:
                    game_framework.exit()
    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.jump_on = True

    @staticmethod
    def do(boy):
        pass



    @staticmethod
    def draw(boy):

            if int(boy.frame) == 0:
                boy.image.clip_draw(0, 365, 50, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 1:
                boy.image.clip_draw(50, 365, 50, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 2:
                boy.image.clip_draw(110, 365, 50, 90, boy.x,  boy.y + boy.jump)
            elif int(boy.frame) == 3:
                boy.image.clip_draw(225, 365, 60, 90, boy.x,  boy.y + boy.jump)
            elif int(boy.frame) == 4:
                boy.image.clip_draw(225, 365, 60, 90, boy.x,  boy.y + boy.jump)



next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,  SPACE: IdleState, UP_DOWN :IdleState},




}


class Shell:

    def __init__(self):
        self.x, self.y = 50, 148

        self.dir = 1
        self.velocity = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame = 0
        self.timer = 0
        self.timer2 = 0
        self.image = load_image('game_sprite\\shell.png')
        self.Count = 10
        self.out_on = [False]
        self.Y = []
        self.color = [1, 0, 0, 2, 0, 1, 2, 0, 1, 2]
        for i in range(0, self.Count):
            # self.color.append(random.randint(0,2))
            self.Y.append(i * 200)
        self.start = 500
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.sleep_on = 0


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        #self.font.draw(self.x - 60, self.y + 50, '(Time:%3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

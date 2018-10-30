from pico2d import *
from ball import Ball
import math
import game_framework
import random
import game_world
import boy

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER =(10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 8


# Ghost event
MOVE_TIMER,SLEEP_TIMER =range(2)
# Boy States


class IdleState:

    @staticmethod
    def enter(ghost, event):
        ghost.timer2 = int(get_time())

    @staticmethod
    def exit(ghost, event):
        pass
    @staticmethod
    def do(ghost):
        ghost.frame = (ghost.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        ghost.timer = int(get_time())
        if ghost.timer-ghost.timer2 == 1:
            ghost.add_event(SLEEP_TIMER)
    @staticmethod
    def draw(ghost):
        ghost.image.clip_draw(int(ghost.frame) * 100, 300, 100, 100, ghost.x, ghost.y)

class Runstate:
    @staticmethod
    def enter(ghost, event):
        ghost.make = random.randint(20, 60) / 100
        global th,r
        ghost.timer = get_time()
        th = math.radians(3.14)*90
    @staticmethod
    def exit(ghost, event):
        pass

    @staticmethod
    def do(ghost):
        global th,r
        ghost.frame = (ghost.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        ghost.image.opacify(ghost.make)
        ghost.timer = get_time()
        ghost.make = int(ghost.timer - ghost.timer2)

        
        th += 0.05



    @staticmethod
    def draw(ghost):
        global th
        if ghost.dir == 1:
            ghost.image.clip_draw(int(ghost.frame) * 100, 300, 100, 100, (ghost.x + 10 * PIXEL_PER_METER * math.cos(th)),(ghost.y + 350 + 10 * PIXEL_PER_METER * math.sin(th)))
        else:
            ghost.image.clip_draw(int(ghost.frame) * 100, 300, 100, 100, (ghost.x + 10 * PIXEL_PER_METER*math.sin(th)), (ghost.y+ 350+10*PIXEL_PER_METER*math.cos(th)))



class SleepState:
    @staticmethod
    def enter(ghost,event):
        ghost.frame = 0
        ghost.timer2 = get_time()
        ghost.make = 2
    @staticmethod
    def exit(ghost,event):
        pass
    @staticmethod
    def do(ghost):
        ghost.frame = (ghost.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        ghost.timer = get_time()+2
        ghost.make = (ghost.timer-ghost.timer2)*5
        if ghost.make >= 20:
            ghost.add_event(MOVE_TIMER)
        ghost.image.opacify(0.3)
    @staticmethod
    def draw(ghost):
        if ghost.dir == 1:
            ghost.image.clip_composite_draw(int(ghost.frame) * 100, 300, 100, 100, (3.141592)*2 / ghost.make, '', ghost.x - 25 +(ghost.make), ghost.y - 25 +(ghost.make*1.8), 100, 100)
        else:
            ghost.image.clip_composite_draw(int(ghost.frame) * 100, 200, 100, 100, -3.141592 / ghost.make, '', ghost.x + 25, ghost.y - 25, 100, 100)


next_state_table = {  IdleState: {SLEEP_TIMER : SleepState} , SleepState: {MOVE_TIMER : Runstate}  }

class Ghost:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.timer2 =1
        self.sleep_on =0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


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


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


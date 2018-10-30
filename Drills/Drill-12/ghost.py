from pico2d import *
from ball import Ball
import math
import game_world
import boy
# Ghost event
MOVE_TIMER =range(1)
# Boy States

class IdleState:

    @staticmethod
    def enter(ghost, event):
        ghost.timer = 300

    @staticmethod
    def exit(ghost, event):
        pass
    @staticmethod
    def do(ghost):
        ghost.frame = (ghost.frame + 1) % 8
        ghost.timer -= 1
        if ghost.timer == 0:
            ghost.add_event(MOVE_TIMER)
    @staticmethod
    def draw(ghost):
        ghost.image.clip_draw(ghost.frame * 100, 300, 100, 100, ghost.x, ghost.y)

class Runstate:
    @staticmethod
    def enter(ghost, event):
        global th,r
        ghost.timer = 300
        ghost.timer2 =1
        ghost.make =2
        th = math.radians(3.14)
        r = 300
    @staticmethod
    def exit(ghost, event):
        pass

    @staticmethod
    def do(ghost):
        global th,r
        ghost.frame = (ghost.frame + 1) % 8
        ghost.image.opacify(ghost.timer2)
        ghost.timer2 -=0.01
        if ghost.timer2 ==0:
            ghost.timer2 =1
        if ghost.make >= 50:
            ghost.make = 50
            ghost.x = 800 + r * math.cos(th)
            ghost.y = 300 + r * math.sin(th)
            th += 0.005
        ghost.make +=1


    @staticmethod
    def draw(ghost):

            ghost.image.clip_composite_draw(ghost.frame * 100, 300, 100, 100,
                                            3.141592 / ghost.make, '', ghost.x , ghost.y+ghost.make, 100, 100)
next_state_table = {  IdleState: {MOVE_TIMER : Runstate}


                      }

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


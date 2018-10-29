from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP , SLEEP_TIMER ,DASH_DOWN, DASH_UP = range(7)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): DASH_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): DASH_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): DASH_DOWN,
    (SDL_KEYUP, SDLK_RSHIFT): DASH_UP
    }



# Boy States

class IdleState:
    @staticmethod
    def enter(boy):
        boy.frame = 0
        boy.timer = 1000
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:

    @staticmethod
    def enter(boy):
        boy.frame = 0

        boy.dir = boy.velocity

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)

        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:
    @staticmethod
    def enter(boy):
        boy.frame = 0
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
            3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
            -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
    RIGHT_DOWN: RunState, LEFT_DOWN: RunState,SLEEP_TIMER : SleepState,DASH_DOWN: IdleState, DASH_UP: IdleState},

    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
    LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, DASH_DOWN: DashState, DASH_UP: IdleState},

    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
    LEFT_UP: RunState, RIGHT_UP: RunState,DASH_DOWN: IdleState, DASH_UP: IdleState},


}


class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self)



    def change_state(self,  state):

        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)


    def add_event(self, event):

        self.event_que.insert(0, event)

    def change_state(self, state):

        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)

    def update(self):

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):

        self.cur_state.draw(self)

    def handle_event(self, event):

        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.velocity += 1
            elif key_event == LEFT_DOWN:
                self.velocity -= 1
            elif key_event == RIGHT_UP:
                self.velocity -= 1
            elif key_event == LEFT_UP:
                self.velocity += 1
            self.add_event(key_event)
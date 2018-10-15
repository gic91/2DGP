import game_framework
from pico2d import *

import main_state

name = "TitleState"
image = None
count = 0

def enter():
    global image, image2
    image = load_image('pause.png')
    image2 = load_image('erase.png')

def exit():
    global image,image2
    del(image)
    del(image2)
def update():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()

        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    global  count

    if count%10 <=5 :

        image.draw(400,300)
    else:
        image2.draw(400,300)
    count += 1
    update_canvas()
    delay(0.1)
    pass

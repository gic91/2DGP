from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def Move_01():
    x,y=203,535
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 300, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()

def Move_02():
    x, y = 132, 243
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 200, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()

def Move_03():
    x, y = 535, 470
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 300, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()
def Move_04():
    x, y = 477, 203
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 200, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()

def Move_05():
    x, y = 715, 136
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 300, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()
def Move_06():
    x, y = 316, 225
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 200, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()

def Move_07():
    x, y = 510, 92
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 300, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()
def Move_08():
    x, y = 692, 518
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 300, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()
def Move_09():
    x, y = 682, 336
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 200, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()
def Move_10():
    x, y = 712, 349
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(100, 300, 100, 100, x, y)
    update_canvas()
    delay(1)
    get_events()

while True:
    Move_01()
    Move_02()
    Move_03()
    Move_04()
    Move_05()
    Move_06()
    Move_07()
    Move_08()
    Move_09()
    Move_10()


close_canvas()

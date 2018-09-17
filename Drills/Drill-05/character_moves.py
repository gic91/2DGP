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
    pass
def Move_03():
    pass
def Move_04():
    pass
def Move_05():
    pass
def Move_06():
    pass
def Move_07():
    pass
def Move_08():
    pass
def Move_09():
    pass
def Move_10():
    pass

while True:
    Move_01()
    Move_02()
   # Move_03()
    #Move_04()
   # Move_05()
    #Move_06()
    #Move_07()
   # Move_08()
    #Move_09()
   # Move_10()


close_canvas()

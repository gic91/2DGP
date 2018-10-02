from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

hide_lattice()
def Move_left():
    x,y=0+25,90
    frame =0
    while (x < 800-25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
        get_events()
def Move_right():
    x, y = 800-25, 90
    frame = 0
    while (x > 0+25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        check = 0
        delay(0.03)
        get_events()

while True:
    Move_left()
    Move_right()

close_canvas()


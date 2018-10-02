from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir =0
move_Frame = 300
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, move_Frame * 1, 100, 100, x,y)
    update_canvas()


    frame = (frame + 1) % 8
    x += dir*5
    delay(0.05)

close_canvas()


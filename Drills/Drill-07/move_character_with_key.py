from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024



open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
size =20
point_x = [(random.randint(0, 1000))for i in range(size)]
point_y = [(random.randint(0, 1000))for i in range(size)]
frame = 0
dir =0
move_Frame = 300
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    n=0
    x= point_x[n]
    y=point_y[n]
    character.clip_draw(frame * 100, move_Frame * 1, 100, 100,x,y)
    update_canvas()
    frame = (frame + 1) % 8
    size = 20
    
    n+=1
    if(n>20):
        n=0

close_canvas()


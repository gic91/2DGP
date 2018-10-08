from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


size = 12
points_x = [(random.randint(0, 800)) for i in range(size)]
points_y = [(random.randint(0, 800)) for i in range(size)]
points = [(random.randint(100, 800),random.randint(0, 1000)) for i in range(size)]
r = 1
frame = 0
while True:
    for j in range(0, size):
     for i in range(0, 100 + 1 , 3):
            t = i / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * points[j][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j + 1) % (size)][0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * points[(j + 2) % (size)][0] + (t ** 3 - t ** 2) * points[(j + 3) % (size)][0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * points[j][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j + 1) % (size)][1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * points[(j + 2) % (size)][1] + (t ** 3 - t ** 2) * points[(j + 3) % (size)][1]) / 2
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            if points_x[r-1] < points_x[r]:
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
            else:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
            frame=(frame+1) % 6;
            handle_events()
            update_canvas()
            delay(0.05)





close_canvas()

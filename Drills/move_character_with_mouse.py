from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x,y
    global save_x,save_y
    global move_ani
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running =False
        elif event.type ==SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            save_x,save_y = x,y
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            move_ani =300
        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running =False



open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
move_ani=300
save_x,save_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, move_ani * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    move_ani =300
    delay(0.02)
    handle_events()

close_canvas()





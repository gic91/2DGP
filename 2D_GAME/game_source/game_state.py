import random
import json
import os

from pico2d import *
import game_framework
import game_world


from Main_Stage import Stage
name = "GameState"

Main_Stage=None

def enter():
    global Main_Stage
    Main_Stage = Stage()
    game_world.add_object(Main_Stage, 0)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()


def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







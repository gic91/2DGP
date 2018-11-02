import game_framework
import pico2d

import menu_state
import game_state

pico2d.open_canvas(1200, 800, sync=True)
#game_framework.run(menu_state)
game_framework.run(game_state)
pico2d.close_canvas()
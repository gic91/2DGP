from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def Move_rect():
      def Move_from_center_to_right():
            x, y = 800 / 2, 90
            while x < 800 - 25:
                  clear_canvas()
                  grass.draw(400, 30)
                  character.draw(x, y)
                  x += 2
                  delay(0.01)
                  update_canvas()
      def Move_up():
            x, y = 800 - 25, 90
            while y < 600 - 50:
                  clear_canvas()
                  grass.draw(400, 30)
                  character.draw(x, y)
                  y += 2
                  delay(0.001)
                  update_canvas()
      def Move_left():
            x, y = 800 - 25, 600 - 50
            while x > 0 + 25:
                  clear_canvas()
                  grass.draw(400, 30)
                  character.draw(x, y)
                  x -= 2
                  delay(0.001)
                  update_canvas()

      def Move_down():
            x, y = 0 + 25, 600 - 50
            while y > 90 + 25:
                  clear_canvas()
                  grass.draw(400, 30)
                  character.draw(x, y)
                  y -= 2
                  delay(0.001)
                  update_canvas()

      def Move_form_left_to_center():
            x, y = 0 + 25, 90
            while x < 800 / 2:
                  clear_canvas()
                  grass.draw(400, 30)
                  character.draw(x, y)
                  x += 2
                  delay(0.001)
                  update_canvas()

      Move_from_center_to_right()
      Move_up()
      Move_left()
      Move_down()
      Move_form_left_to_center()

import math

def Move_circle():
      cx, cy, r = 800 /2, 600/2, (600-180)/2
      degree = -90
      while degree <270:
            radian = math.radians(degree)
            x = cx + r * math.cos(radian)
            y = cy + r * math.sin(radian)
            clear_canvas()
            grass.draw(400,30)
            character.draw(x,y)
            degree+=1
            delay(0.01)
            update_canvas()


while True:
      #Move_rect()
      Move_circle()
close_canvas()

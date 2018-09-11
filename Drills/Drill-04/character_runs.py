from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame =0
check=0
hide_lattice()
while(True):

    if (check==0):
     while (x<800):
         clear_canvas()
         grass.draw(400,30)
         character.clip_draw(frame * 100, 90, 100, 100, x,90)
         update_canvas()
         frame = (frame +1) %8
         x+=5
         delay(0.03)
         check=1
         get_events()
    elif (check==1):
     while (x>0):
         clear_canvas()
         grass.draw(400,30)
         character.clip_draw(frame * 100, 0, 100, 100, x,90)
         update_canvas()
         frame = (frame +1) %8
         x-=5
         check=0
         delay(0.03)
         get_events()




close_canvas()


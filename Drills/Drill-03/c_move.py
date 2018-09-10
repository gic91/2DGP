from pico2d import *
import math 
os.chdir('C:\\Users\\sangjik_PC\\Desktop\\과제\\2018 2학기\\2018-2DGP 과제\\2DGP\\Drills\\Drill-03')
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=10
y= 90
count =0
deg=0
th = math.radians(3.14)
r=230
check =0
check2 = 0
while(True):
      clear_canvas_now()
      grass.draw_now(400,30)
      character.draw_now(x,y)
      if count ==0:
            if x==780 and y==90:#right
                  right = 1
                  left = 0
                  up =0
                  down =0
                  
            elif x==10 and y==550:#left
                  left = 1
                  right = 0
                  up =0
                  down =0
            elif x==780 and y==550:#up
                  up =1
                  right = 0
                  left = 0
                  down =0
                  check=1
            elif x==10 and y==90:#down
                  down =1
                  right = 0
                  left = 0
                  up=0

            if count==0 and x==400 and y ==90 and check==1:
                 count=1
                 
            if right ==1:
                  y+=2
            elif left ==1:
                  y-=2
            elif up ==1:
                  x-=2
            elif down ==1:
                  x+=2
            delay(0.001)
      elif count == 1:
            x =400+ r * math.cos(th)
            y =300+ r * math.sin(th)
            th+=1
            check2 +=10
            if check2==360:
                  check2=0
                  check=0
                  count=0
                  x=400
                  y=90
                  down =1
            delay(0.1)
            

    
close_canvas()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:
###student_id:6201012620139
###assignment1
import pygame 
import random

black = 0,0,0
white = 255,255,255
# initialize PyGame
pygame.init()

# set window caption
pygame.display.set_caption('Assignment1 non-overlapping circles ') 

# create a clock
clock = pygame.time.Clock()
#set up screen
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

#list of info
cir_cle = []
Name = []
radius = []
#random color rbg
COLORS = [(119, 141, 252), 
          (119, 252, 181),
          (252, 243, 119),
          (225,142,197),
          (253,170,115)]

def random_color():
    return random.choice(COLORS)

#make n=10 circles
def draw_circle():
    for n in range(10):
        r = random.randint(10,20) #random radius 10-20 
        x = random.randint(r,scr_w-r) #random x position
        y = random.randint(r,scr_h-r) #random y position
        color= random_color() #random color
        draw_cir=pygame.draw.circle( screen, color, (x,y), r ,0) #make circle

        #add info
        Name.append(draw_cir)
        cir_cle.append((x,y,r))
        radius.append(r)

    return 0

# delete the most radius of circles
def get_cir_rm():
    max_r = max(radius)
    for x,y,r in cir_cle :
        if r == max_r: 
            c = cir_cle[cir_place.index((x,y,r))]   # Let c = circle with the most radius
            index = cir_place.index((x,y,r))          # find index of circle with the most radius
            circle = Name[index]                      # Let circle = val of  circle 
            print("The biggest circle is ", circle)
            return circle

# get the most radius
def get_r_rm():
    max_r = max(radius)
    for x,y,r in cir_cle :
        if r == max_r: 
            return r 


def rm_data():
    circle = get_cir_rm()                     # circle = วงกลมที่จะลบ
    index = Name.index(circle)                # fin dindex of data about circle
    Name.remove(Name[index])                  # Remove val from Name
    cir_cle.remove(cir_cle[index])        # Remove position from cir_place
    radius.remove(radius[index])              # Remove radius from radius
    return 0    

#do circle
draw_circle()

# Run until the user asks to quit
running = True
while running:

    clock.tick( 10 ) 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
    for event in pygame.event.get():
            if ( event.type == pygame.MOUSEBUTTONUP ):         
                mouse_pos = pygame.mouse.get_pos()             
                circle_remove = get_cir_rm()                   
                r = get_r_rm()
                if ( circle_remove.collidepoint( mouse_pos ) ):   
                    pygame.draw.circle(screen, black, mouse_pos, r*2 ,0)    
                    rm_data()                                  
    
    # update the screen display
    pygame.display.update()

pygame.quit()

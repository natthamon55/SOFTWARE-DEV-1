#!/usr/bin/env python
# coding: utf-8

# In[ ]:
###student_id:6201012620139
###assignment1
### ref1:  https://stackoverflow.com/questions/58717367/how-does-the-collidepoint-function-in-pygame-work
### ref2:  https://stackoverflow.com/questions/28999287/generate-random-colors-rgb
import pygame
from random import randint
from random import choice

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
# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
#list of info
Name = [ ]
cir_cle = [ ]
rad = [ ]
#random color
COLORS = [(119, 141, 252), 
          (119, 252, 181),
          (252, 243, 119),
          (225,142,197),
          (253,170,115)]

def random_color():
    return choice(COLORS)

# make 10 circles
def draw_Circle():
    for num in range(10):
        r = randint(10,20) #random radius 10-20
        x = randint(r,scr_w-r) #random x position
        y = randint(r,scr_h-r) #random y position
        
        draw = pygame.draw.circle(screen, random_color(), (x,y), r ,0)
        # add info to list
        Name.append(draw)
        cir_cle.append((x,y,r))
        rad.append(r)
    return True

# remove the biggest radius of circle
def get_cir_rm():
    max_r = max(rad) #max value of radius
    for x,y,r in cir_cle :
        if r == max_r: 
            c = cir_cle[cir_cle.index((x,y,r))]   # Let c = circle with the most radius
            index = cir_cle.index((x,y,r))          # find index of circle with the most radius
            circle = Name[index]                      # Let circle = draw of  circle 
            print('The Biggest circle is :{}'.format(circle))
            return circle
# get the most radius
def get_max_r():
    max_r = max(rad)
    for x,y,r in cir_cle :
        if r == max_r: 
            return r

def  rm_info():
    circle = get_cir_rm()                     # circle that want to remove
    index = Name.index(circle)                # fin dindex of data about circle
    Name.remove(Name[index])                  # Remove val from Name
    cir_cle.remove(cir_cle[index])        # Remove position from cir_place
    rad.remove(rad[index])              # Remove radius from radius
    return 0    

# Draw circle
draw_Circle()

running = True

while running :

    clock.tick(10)

    event_get=pygame.event.get()

    #when user click close button
    for event in event_get  :
        if event.type == pygame.QUIT:
            running = False

    for event in event_get :
        if ( event.type == pygame.MOUSEBUTTONUP ):         # click left mouse 
            mouse_pos = pygame.mouse.get_pos()             # Location of the mouse-click
            circle_remove = get_cir_rm()                   # Select circle to remove 
            r = get_max_r()
            if ( circle_remove.collidepoint( mouse_pos ) ):   # click circle 
                pygame.draw.circle(screen, black, mouse_pos, r*3 ,0)    # Draw another circle over selected circle 
                rm_info()   #delete circle from list
    
    # update the screen display
    pygame.display.update()

pygame.quit()


#!/usr/bin/env python
# coding: utf-8

# In[ ]:
###student_id:6201012620139
###assignment1
import pygame 
import random
import math
# initialize PyGame
pygame.init()

# set window caption
pygame.display.set_caption('Assignment1 non-overlapping circles ') 

# create a clock
clock = pygame.time.Clock()
#set up screen
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
#list of info
cir_cle = []
Name_cir = []
radius_cir = []

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
        x,y = random.randint(r,scr_w-r), random.randint(r,scr_h-r) #random x,y position
        color= random_color() #random color
        draw_cir=pygame.draw.circle( surface, color, (x,y), r ) #make circle

        Name_cir.append(draw_cir)
        cir_cle.append((x,y,r))
        radius_cir.append(r)

    return True


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
                    del_data()                                  
    
    
    # fill the screen with the white color
    screen.fill((255,255,255))

    # draw the surface on the screen
    screen.blit(surface, (0,0))

    # update the screen display
    pygame.display.update()

pygame.quit()

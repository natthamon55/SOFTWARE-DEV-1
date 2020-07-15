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
pygame.display.set_caption('Assignment1 Drawing Circle') 

# create a clock
clock = pygame.time.Clock()
#set up screen
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# Run until the user asks to quit
running = True
while running:
    # This limits the while loop to a max of 10 times per second.
    clock.tick( 15 ) 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = rectangle.collidepoint(pygame.mouse.get_pos())

            if click == 1:
                print ('CLICKED!')

    # random value between 10-20 for the radius
    r = random.randint(10,20)

    #random color rbg
    COLORS = [(119, 141, 252), 
          (119, 252, 181),
          (252, 243, 119),
          (225,142,197),
          (253,170,115)]

    def random_color():
        return random.choice(COLORS)

    # random a position (x,y)
    x,y = random.randint(r,scr_w-r), random.randint(r,scr_h-r)

    # draw a circle filled with the random color on the surface
    pygame.draw.circle( surface,random_color(), (x,y), r )

    # fill the screen with the white color
    screen.fill((255,255,255))

    # draw the surface on the screen
    screen.blit(surface, (0,0))

    # update the screen display
    pygame.display.update()

pygame.quit()

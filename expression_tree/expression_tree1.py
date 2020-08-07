#student id :6201012620139
#ref1 : https://riptutorial.com/pygame/example/21726/drawing-shapes--text-and-images-on-the-screen-with-a-small-animation
#ref2 : https://www.daniweb.com/programming/software-development/code/454765/save-a-pygame-drawing 
#Expression Tree

import pygame
import pygame.image
from pygame.locals import *
import sys #access to some variables used or maintained

# rgb color
black = (0,0,0)
red   = (255,0,0)
green = (0, 255, 0)

# initialize PyGame
pygame.init()
pygame.display.set_caption('Expression Tree') 
scr_w, scr_h = 1000, 700
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#class of expression boolean
oparator= ['+','&','!']
var =['l0','l1','l2']
class Boolean_tree():
    def __init__(self,data):
        self.data = data



#for draw line
y_line = []
x_line = []
y_h = int(scr_h/4)
x_w = int(scr_w/4)
for i in range(4):
    y_line.append(int(y_h*(i+1)-100))
for i in range(4):
    x_line.append(int(x_w*(i+1)))

#font of text
font_obj = pygame.font.Font('freesansbold.ttf', 80)

####################################################
fname='expression_tree.jpg'
running = True
while running:
   
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False
            #save image file to directory    
            pygame.image.save(screen,fname)
            print("file {} has been saved".format(fname))
   
    
    #fill the screen with Light green
    screen.fill((230, 255, 230)) 
    #draw line
    pygame.draw.line(screen,red, (x_line[1],y_line[0]), (x_line[0],y_line[1]),4)
    pygame.draw.line(screen,red, (x_line[1],y_line[0]), (x_line[2],y_line[1]),4)
    pygame.draw.line(screen,red, (x_line[0],y_line[1]), (x_line[0]-100,y_line[2]),4)
    pygame.draw.line(screen,red, (x_line[0],y_line[1]), (x_line[0]+100,y_line[2]),4)
    pygame.draw.line(screen,red, (x_line[2],y_line[1]), (x_line[2],y_line[2]),4)
    pygame.draw.line(screen,red, (x_line[2],y_line[2]), (x_line[2]-100,y_line[3]),4)
    pygame.draw.line(screen,red, (x_line[2],y_line[2]), (x_line[2]+100,y_line[3]),4)

    #show text
    text='+'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (475, 30)
    screen.blit(text_surface_obj, text_rect_obj.center)

    text='&'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (220,170)
    screen.blit(text_surface_obj, text_rect_obj.center)

   
    text='l0'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (110,400)
    screen.blit(text_surface_obj, text_rect_obj.center)

    text='l1'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300,400)
    screen.blit(text_surface_obj, text_rect_obj.center)

    text='!'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (730,170)
    screen.blit(text_surface_obj, text_rect_obj.center)

    text='&'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (730,380)
    screen.blit(text_surface_obj, text_rect_obj.center)

    text='l1'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (600,600)
    screen.blit(text_surface_obj, text_rect_obj.center)

    text='l2'
    text_surface_obj = font_obj.render(text, True, black, green)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (830,600)
    screen.blit(text_surface_obj, text_rect_obj.center)

    #update the display
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
print('Pygame  is Done....')
####################################################


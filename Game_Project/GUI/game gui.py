#Game Progect : ONE TOUCH (Pygame & Python Arcade)
#Blog Update : https://s6201012620139.blogspot.com/2020/09/one-touch-game-project-010123131.html
#student id : 1)นางสาวหทัยพัทร ชำนินวล 6201012620244 2) นางสาวนัทธมน บุญนิธิ  6201012620139
#----------------------------------------------------------------------------------------------#
import pygame
import sys

pygame.init()
pygame.font.init()

black = (0,0,0)
red = (161, 0, 0)
white = (250,250,250)

text_font2 = pygame.font.Font('freesansbold.ttf', 30)

pygame.display.set_caption('One Touch')
screen = pygame.display.set_mode((1000, 700))
surface =pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.fill(black)

#draw button
def draw_rect(color,rect):
    pygame.draw.rect(screen, color , rect)


#draw text
def create_text(text,x,y):
    text_surface = text_font2.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = ( x,y )
    screen.blit( text_surface , text_rect )
    return 0
    
################################# Game Window ##############################################

time_text = create_text('TIME :',80,60)
score_text = create_text('SCORE : ',820,60)
exit_button = pygame.draw.rect(screen, red , (800,600,180,80)) #(left,top,width,hight)
exit_text = create_text('EXIT',890,640)


clock = pygame.time.Clock()
running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
    screen.blit(surface,(0,0))
    pygame.display.update()

#Game Progect : ONE TOUCH (Pygame & Python Arcade)
#Blog Update : https://one-touch-game-project.blogspot.com/p/one-touch.html
#student id : 1)นางสาวหทัยพัทร ชำนินวล 6201012620244 
#             2) นางสาวนัทธมน บุญนิธิ  6201012620139
#----------------------------------------------------------------------------------------------#
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#rgb color
black = (0,0,0)
red = (161, 0, 0)
white = (250,250,250)

#font
text_font1 = pygame.font.Font('freesansbold.ttf', 80)
text_font2 = pygame.font.Font('freesansbold.ttf', 30)
text_font3 = pygame.font.Font('freesansbold.ttf', 20)

pygame.display.set_caption('One Touch')
screen = pygame.display.set_mode((1000, 700))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.fill(black)

#picture bg
image = pygame.image.load(r'C:\software\game\game+gui\ball.jpg') 

#draw button
def draw_rect(color,rect):
    pygame.draw.rect(screen, color , rect)

#show text ONE TOUCH
def text_show(text):
    text_surface = text_font1.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.midright = (750,100)
    screen.blit( text_surface , text_rect )
    return 0


#draw text
def create_text(text,x,y):
    text_surface = text_font2.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = ( x,y )
    screen.blit( text_surface , text_rect )
    return 0
    
#show text how to play
def text_howto(text,x,y):
    text_surface = text_font3.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit( text_surface , text_rect )
    return 0

 #--------------------------------------------------MAIN MENU------------------------------------------------------------#   
click = False
def main_menu():

    while True:
        
        screen.blit(image, (200, 400))
        text_show('ONE TOUCH')
        text_howto('** HOW TO PLAY ? : Touch/Click the ball through the camera ',500,400)
        text_howto('when you tap it, there will show your score with coundown timer :P **',500,450)

        mx1, my1 = pygame.mouse.get_pos()
        button_1 =  pygame.Rect(400,200,200,100)

        if button_1.collidepoint((mx1, my1)):
            if click:
                game()

        pygame.draw.rect(screen, red , button_1)
        create_text('START !',500,250)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def game():

    font = pygame.font.SysFont(None, 45)
    counter = 60
    text = font.render(str(counter), True, white)
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    running= True
    while running:
        clock.tick(60)

        mx2, my2 = pygame.mouse.get_pos()
        button_2 = pygame.Rect(800,600,180,80) #(left,top,width,hight)

        if button_2.collidepoint((mx2, my2)):
            if click:
                score()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                counter -= 1
                text = font.render(str(counter), True, white)
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        screen.fill(black)
        text_rect = text.get_rect()
        text_rect.center = (150,45)
        screen.blit(text, text_rect.center)
        create_text('TIME :',80,60)
        create_text('SCORE : ',820,60)
        pygame.draw.rect(screen, red , button_2)
        create_text('EXIT',890,640)

        pygame.display.flip() 
        pygame.display.update()


def score():

    is_running = True  
    while is_running :

        screen.fill(black)
        screen.blit(image, (200, 400))
        text_show('ONE TOUCH')
        
        mx3,my3 = pygame.mouse.get_pos()
        button_3 = pygame.Rect(400,380,200,100)

        if button_3.collidepoint((mx3, my3)):
            if click:
                main_menu()
        
        pygame.draw.rect(screen, red , button_3)
        create_text('RESTART !',500,440)
        create_text('SCORE : ',350,250)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)


main_menu()

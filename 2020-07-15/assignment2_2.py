### student_id:6201012620139
### assignment2
### ref1:  http://www.geometrian.com/programming/projects/index.php?project=Circle%20Collisions
### ref2:  https://stackoverflow.com/questions/58717367/how-does-the-collidepoint-function-in-pygame-work
### ref3:  https://stackoverflow.com/questions/28999287/generate-random-colors-rgb
import pygame
import math
import sys
from pygame.locals import *
from random import randint
from random import random
from random import choice

# initialize PyGame
pygame.init()
print( 'PyGame version: {}'.format( pygame.version.ver ) )
pygame.display.set_caption('Assignment2 Moving / Bouncing Circles ') 
#set up screen
screen = pygame.display.set_mode((800,600))
#create a clock
clock = pygame.time.Clock()

#empty lish for keep circle
Circles = [] #x,y,r,speed x/y
point_cir=[] #x,y,r
rad=[] #radius

#class of circle
class Circle:
    def __init__(self):
        self.radius = randint(10,20) #random radius 10-20
        self.x = randint(self.radius, 800-self.radius) #random x position
        self.y = randint(self.radius, 600-self.radius) #random y position
        self.speedx = 0.5*(random()+1.0) #speed for x position
        self.speedy = 0.5*(random()+1.0) #speed for y position
#color and random color
black = 0,0,0
COLORS = [(119, 141, 252), (119, 252, 181),(252, 243, 119),(225,142,197),(253,170,115)]
def random_color():
    return choice(COLORS)
#add infomation to list
def add1_info() :
    print('Enter Number of circle')
    n = int(input('Number of circle:'))
    for i in range(n):
        #add info to empty list
        Circles.append(Circle())
    return True   
add1_info()
def add2_info():
    for Circle in Circles:
        rad.append(Circle.radius)
        point_cir.append((Circle.x,Circle.y,Circle.radius))
    return True
add2_info()
#remove the biggest radius of circle
def know_cir_rm():
    max_rad = max(rad) #max value of radius
    for x,y,r in point_cir :
        if r == max_rad: 
            c = point_cir[point_cir.index((x,y,r))]   # Let c = circle with the most radius
            index = point_cir.index((x,y,r))          # find index of circle with the most radius
            circle = Circles[index]                      # Let circle = draw of  circle 
            print('The Biggest circle is :{}'.format(circle))
            return circle
# get the most radius
def know_max_r():
    max_rad = max(rad)
    for x,y,r in point_cir :
        if r == max_rad: 
            return r

def  rm_info():
    circle = know_cir_rm()                # circle that want to remove
    index = Circles.index(circle)         # find index of data about circle
    Circles.remove(Circles[index])        # Remove draw from Name
    point_cir.remove(point_cir[index])    # Remove position from point_cir
    rad.remove(rad[index])              # Remove radius from radius
    return 0    

#Create function for Moving / Bouncing Circles
def cir_crash(C1,C2):
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    C1.speedx = XSpeed
    C1.speedy = YSpeed
#move circle
def move_cir():
    for Circle in Circles:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy
#check when circle crash
def crash_check():
    for Circle in Circles:
        if Circle.x < Circle.radius or Circle.x > 800-Circle.radius: Circle.speedx *= -1
        if Circle.y < Circle.radius or Circle.y > 600-Circle.radius: Circle.speedy *= -1
    for Circle in Circles:
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    cir_crash(Circle,Circle2)
#draw circle
def draw_cir():
    #fill black color for terminal
    screen.fill(black)
    for Circle in Circles:
        pygame.draw.circle(screen,random_color(),(int(Circle.x),int(600-Circle.y)),Circle.radius)
#while loop main        
running= True
while running:
    clock.tick(40)
    draw_cir()
    move_cir()
    crash_check()
    keystate = pygame.key.get_pressed()
    event_get=pygame.event.get()
    #when user click close button or get the state of all keyboard buttons
    for event in event_get:
        if event.type == QUIT or keystate[K_ESCAPE] :
               running = False
    
    for event in event_get :
        if ( event.type == pygame.MOUSEBUTTONUP ):         # click left mouse 
            mouse_pos = pygame.mouse.get_pos()             # Location of the mouse-click
            cir_remove = know_cir_rm()                   # Select circle to remove 
            r = know_max_r()
            if ( cir_remove.collidepoint( mouse_pos ) ):   # click circle 
                pygame.draw.circle(screen, black, mouse_pos, r*3 ,0)    # Draw another circle over selected circle 
                rm_info()   #delete circle from list
    
    #update the full display Surface to the screen
    pygame.display.flip()
    #update the screen display
    pygame.display.update()

pygame.quit()

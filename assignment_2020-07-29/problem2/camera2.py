#student id: 6201012620139
#ref: pygame_camera_demo-1.py by RSP
###################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys #access to some variables used or maintained

# initialize PyGame
pygame.init()
scr_w, scr_h = 640 , 360
screen = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
pygame.display.set_caption('Pygame Camera ') 
##############################################
class Square_rect:
    def __init__(self, left, top, rw, rh):
        self.top = top
        self.left = left
        self.rh = rh
        self.rw = rw
        self.side = left, top, rw, rh

    def draw(self):
        pygame.draw.rect( img, (0,255,0) ,self.side, 1 )
        surface.blit( img, (self.left, self.top, self.rw, self.rh), self.side)

##############################################
list_rect = []
draw_black = []
add_rect = []

M,N = 4,3
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        rect = Square_rect(i*rw, j*rh, rw, rh)
        list_rect.append(rect)
        add_rect.append(rect)
########################################################

def open_camera( frame_size=(640,360),mode='RGB'):
    #it needs to be imported and initialized
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()#a list of cameras attached to the computer
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 
##########################################################

camera = open_camera()
#start camera
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)
##################################################################

img = None
is_running = True 
while is_running:
    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue
    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h

    # draw picture camera (MxN) on the screen
    for rect in list_rect:
        rect.draw()

    event_get = pygame.event.get()
    #when user click the screen and picture will appear
    for event in event_get:
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )

              
    for event in event_get:    
        # take position input from mouse
        if event.type == pygame.MOUSEBUTTONUP:
            global pos_start_rect
            if event.button == 1:
                for rect in list_rect:
                    mouse_pos = pygame.mouse.get_pos()
                    if((rect.left < mouse_pos[0] < rect.left+rect.rw) and (rect.top < mouse_pos[1] < rect.top+rect.rh)):
                            
                        if(pos_start_rect.side == rect.side):
                                print("Not in")
                   

        elif event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                for rect in list_rect:
                    mouse_pos = pygame.mouse.get_pos()
                    if(  (rect.left < mouse_pos[0] < rect.left+rect.rw) and (rect.top < mouse_pos[1] < rect.top+rect.rh)  ):
                        pos_start_rect = rect
                        

    # write the surface to the screen and update the display
    screen.blit(surface,(0,0))
    pygame.display.update()

# close the camera
camera.stop()
pygame.quit()
print('Pygame camera is Done....')
###################################################################
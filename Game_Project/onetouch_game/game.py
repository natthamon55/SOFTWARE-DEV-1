#Game Progect : ONE TOUCH (Pygame & Python Arcade)
#Blog Update : https://s6201012620139.blogspot.com/2020/09/one-touch-game-project-010123131.html
#student id : 1)นางสาวหทัยพัทร ชำนินวล 6201012620244 
#             2) นางสาวนัทธมน บุญนิธิ  6201012620139
#----------------------------------------------------------------------------------------------#

import pygame
import random
import pygame.camera
import time

pygame.init()
clock = pygame.time.Clock()


scr_w , scr_h = 1000,700
screen = pygame.display.set_mode( (scr_w , scr_h) )
pygame.display.set_caption('test')

class ball():
    def __init__(self,surface):
        position_ball = [ (100,150) , (100,600) , (900,150) , (900,600) ,
                        (100,350) , (900,350) , (500,150) , (500,600)]
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        self.r = 50
        self.color = (r,g,b)
        self.pos = random.choice(position_ball) 
        self.surface = surface
        self.draw = pygame.draw.circle( self.surface, self.color, self.pos, self.r ,0)
        self.surface_size = surface.get_size()

    def is_collided(self,mx, my):
        if self.draw.collidepoint((mx, my)):
            return True
        else : return False


def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 


def game_play():

    camera = open_camera()

    surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

    obj_ball = ball(surface)             #สร้างบอลลูกแรก

    running = True

    while running :

        clock.tick(1000)

        img = camera.get_image()
        screen.blit( img , (0,0) )  

        mx , my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_ball.is_collided(mx, my):
                    surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )          #เหมือนการรีหน้า surface ใหม่เพื่อลบบอลออก
                    pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
                    obj_ball = ball(surface)                                            #สร้างบอลลูกใหม่
            
        screen.blit( surface, (0,0) )

        pygame.display.flip()

    camera.stop()
    pygame.quit()


game_play()




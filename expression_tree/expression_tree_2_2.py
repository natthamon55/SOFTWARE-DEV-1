#student id : 6201012620139
#Name : Natthamon Bunnithi
#ref1 : https://riptutorial.com/pygame/example/21726/drawing-shapes--text-and-images-on-the-screen-with-a-small-animation
#ref2 : https://www.daniweb.com/programming/software-development/code/454765/save-a-pygame-drawing 
#expression tree
import pygame
import pygame.image
from pygame.locals import *
import sys #access to some variables used or maintained

#-----------------------------class of expression tree boolean-----------------------------------#
class boolean_tree():   
     
    def __init__(self,equ): 
        self.equ = equ 
        self.prefix = ['None']*15
        self.stack=[ ]

    #for check if prefix is empthy
    def isEmpty(self):
            return self.prefix == []

    #convert infix equation to prefix equation
    def InfixToPrefix(self) :
        num = 0
        vars=['I0','I1','I2']
        self.op= list()
        operator = ['+','&','!','(',')']

        #add equation to self.op
        for i in range(len(self.equ)):

            if self.equ[i] == 'I' and self.equ[i+1] == '0':
                self.op += vars[0]

            elif self.equ[i] == 'I' and self.equ[i+1] == '1':
                self.op += vars[1]

            elif self.equ[i] == 'I' and self.equ[i+1] == '2':
                self.op += vars[2]

            elif self.equ[i] in '01' and self.equ[i-1] != 'I':
                self.op += self.equ[i]
                
            if self.equ[i] in operator :
                self.op += self.equ[i]

        #add self.op are operator and operand and then add it to self.prefix
        for i in self.op :
            self.left = (num * 2) + 1                        
            self.right = (num * 2) + 2 

            if i == '(':
                if self.prefix[self.left] == 'None' :
                    num = self.left
                else :
                    num = self.right

            elif i == 'I1' or i == 'I0' or i == 'I2' or i == 'I3' or i == '1' or i == '0' : 

                if self.prefix[self.left] == 'None' :      
                    self.prefix[self.left] = i

                else :
                    self.prefix[self.right] = i

            elif i in operator :                                      
                self.prefix[num] = i 
                
            else :                              
                if num%2 == 1 :                   
                    num = int((num-1)/2)
                else :
                    num = int((num-2)/2)

        while not self.isEmpty() :
            return self.prefix

#---------------- test program-----------------#
#exp1 = "!(1+0)"
#exp2 = "!(!(0+I0&1))"
#exp3 = "(I0+!I1+!(I2))&(!I0+I1+I2)"
#exp4 = "!(I0&I1)+!(I1+I2)"
#exp5 = "(((I0&I1&!I2)+!I1)+I3)"
equ1 = input('Please input your equation :')
equ2 = equ1.replace(" "," ")
print('infix is {}'.format(equ1))
obj1 = boolean_tree(equ2) 
obj2 = obj1.InfixToPrefix()
print('prefix is: {}'.format(obj2))

#--------------------------Pygame--------------------------------------------------#
# initialize PyGame
pygame.init()
pygame.display.set_caption('Expression Tree') 
scr_w, scr_h = 1300, 900
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
# rgb color
black = (0,0,0)
red   = (255,0,0)
green = (0, 255, 0)
#x,y position
w0,h0 = 600,80
w1,h1 = 300,220
w2,h2 = 900,220
w3,h3 = 150,440
w4,h4 = 450,440
w5,h5 = 750,440
w6,h6 = 1050,440
w7,h7 = 75,660
w8,h8 = 225,660
w9,h9 = 375,660
w10,h10 = 525,660
w11,h11 = 675,660
w12,h12 = 825,660
w13,h13 = 975,660
w14,h14 = 1125,660

#font of text
font_obj = pygame.font.Font('freesansbold.ttf', 80)

#-------------------Running Pygame-------------------------------------------#
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
   
    #show text
    if obj2[0] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w0,h0),40)
        text_surface_obj = font_obj.render(obj2[0], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w0-18,h0-30)
        screen.blit(text_surface_obj, text_rect_obj.center)
    
    if obj2[1] != 'None':
        text_surface_obj = font_obj.render(obj2[1], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w1-17,h1-30)
        screen.blit(text_surface_obj, text_rect_obj.center)


    if obj2[2] != 'None':
        text_surface_obj = font_obj.render(obj2[2], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w2-17,h2-30)
        screen.blit(text_surface_obj, text_rect_obj.center)
    
    if obj2[3] != 'None':
        text_surface_obj = font_obj.render(obj2[3], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w3-17,h3-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[4] != 'None':   
        text_surface_obj = font_obj.render(obj2[4], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w4-17,h4-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[5] != 'None':   
        text_surface_obj = font_obj.render(obj2[5], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center =(w5-17,h5-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[6] != 'None':
        text_surface_obj = font_obj.render(obj2[6] , True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w6-17,h6-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[7] != 'None': 
        text_surface_obj = font_obj.render(obj2[7], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w7-17,h7-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[8] != 'None': 
        text_surface_obj = font_obj.render(obj2[8], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w8-17,h8-30)
        screen.blit(text_surface_obj, text_rect_obj.center)
    
    if obj2[9] != 'None': 
        text_surface_obj = font_obj.render(obj2[9], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w9-17,h9-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[10] != 'None': 
        text_surface_obj = font_obj.render(obj2[10], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w10-17,h10-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[11] != 'None': 
        text_surface_obj = font_obj.render(obj2[11], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w11-17,h11-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[12] != 'None': 
        text_surface_obj = font_obj.render(obj2[12], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w12-17,h12-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[13] != 'None': 
        text_surface_obj = font_obj.render(obj2[13], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w13-17,h13-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    if obj2[14] != 'None': 
        text_surface_obj = font_obj.render(obj2[14], True, black, green)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (w14-17,h14-30)
        screen.blit(text_surface_obj, text_rect_obj.center)

    #update the display
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
print('Pygame  is Done....')
#---------------------------
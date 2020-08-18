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
        self.prefix = ['--']*15
        self.stack= list()

    #for check if prefix is empthy
    def isEmpty(self):
            return self.stack == []

    #convert infix equation to prefix equation
    def InfixToPrefix(self) :
        num = 0
        vars=['I0','I1','I2']
        operator1 = set('+&!()')
        operator2 = set('+&!')

        #add equation to self.op
        for i in range(len(self.equ)):

            if self.equ[i] == 'I' and self.equ[i+1] == '0':
                self.stack += vars[0]

            elif self.equ[i] == 'I' and self.equ[i+1] == '1':
                self.stack += vars[1]

            elif self.equ[i] == 'I' and self.equ[i+1] == '2':
                self.stack += vars[2]

            elif self.equ[i] in '01' and self.equ[i-1] != 'I':
                self.stack += self.equ[i]
                
            if self.equ[i] in operator1 :
                self.stack += self.equ[i]

        #add self.stack that keep operator and operand  add to self.prefix
        for i in self.stack :
            self.left = (num * 2) + 1                        
            self.right = (num * 2) + 2 

            if i == '(':
                if self.prefix[self.left] == '--' :
                    num = self.left
                else :
                    num = self.right

            elif i == 'I1' or i == 'I0' or i == 'I2' or i == 'I3' or i == '1' or i == '0' : 

                if self.prefix[self.left] == '--' :      
                    self.prefix[self.left] = i

                else :
                    self.prefix[self.right] = i

            elif i in operator2:                                      
                self.prefix[num] = i 
                
            else :                              
                if num%2 == 1 :                   
                    num = int((num-1)/2)
                else :
                    num = int((num-2)/2)

        # if true will return the output of prefix
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
fname='expression1_tree.jpg' #name of picture file (.jpg)
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
   
    #draw expression tree (text,circle,line)
    if obj2[0] != '--':
        pygame.draw.circle(screen,green,(w0,h0),50)
        text_surface_obj = font_obj.render(obj2[0], True, black)
        text_center = (w0-18,h0-30)
        screen.blit(text_surface_obj, text_center)

    
    if obj2[1] != '--':
        pygame.draw.circle(screen,green,(w1,h1),50)
        text_surface_obj = font_obj.render(obj2[1], True, black)
        text_center = (w1-17,h1-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w0-30,h0),(w1+30,h1),10)

    if obj2[2] != '--':
        pygame.draw.circle(screen,green,(w2,h2),50)
        text_surface_obj = font_obj.render(obj2[2], True, black)
        text_center = (w2-17,h2-30)
        screen.blit(text_surface_obj, text_center)
        
        pygame.draw.line(screen,red,(w0+30,h0),(w2-30,h2),10)

    if obj2[3] != '--':
        pygame.draw.circle(screen,green,(w3,h3),50)
        text_surface_obj = font_obj.render(obj2[3], True, black)
        text_center = (w3-17,h3-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w1-30,h1+20),(w3+30,h3),10)

    if obj2[4] != '--':   
        pygame.draw.circle(screen,green,(w4,h4),50)
        text_surface_obj = font_obj.render(obj2[4], True, black)
        text_center = (w4-17,h4-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w1+30,h1+20),(w4-30,h4),10)

    if obj2[5] != '--':  
        pygame.draw.circle(screen,green,(w5,h5),50)
        text_surface_obj = font_obj.render(obj2[5], True, black)
        text_rect_obj.center =(w5-17,h5-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w2-30,h2+20),(w5+30,h5),10)

    if obj2[6] != '--':
        pygame.draw.circle(screen,green,(w6,h6),50)
        text_surface_obj = font_obj.render(obj2[6] , True, black)
        text_center = (w6-17,h6-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w2+30,h2+20),(w6-30,h6),10)


    if obj2[7] != '--': 
        pygame.draw.circle(screen,green,(w7,h7),50)
        text_surface_obj = font_obj.render(obj2[7], True, black)      
        text_center = (w7-17,h7-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w3-30,h3+20),(w7+30,h7),10)

    if obj2[8] != '--': 
        pygame.draw.circle(screen,green,(w8,h8),50)
        text_surface_obj = font_obj.render(obj2[8], True, black)
        text_center = (w8-17,h8-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w3+30,h3+20),(w8-30,h8),10)
    
    if obj2[9] != '--': 
        pygame.draw.circle(screen,green,(w9,h9),50)
        text_surface_obj = font_obj.render(obj2[9], True, black)
        text_center = (w9-17,h9-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w4-30,h4+20),(w9+30,h9),10)

    if obj2[10] != '--': 
        ygame.draw.circle(screen,green,(w10,h10),50)
        text_surface_obj = font_obj.render(obj2[10], True, black)
        text_center = (w10-17,h10-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w4+30,h4+20),(w10-30,h10),10)

    if obj2[11] != '--': 
        pygame.draw.circle(screen,green,(w11,h11),50)
        text_surface_obj = font_obj.render(obj2[11], True, black)
        text_center = (w11-17,h11-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w5-30,h5+20),(w11+30,h11),10)

    if obj2[12] != '--': 
        pygame.draw.circle(screen,(0,128,255),(w12,h12),50)
        text_surface_obj = font_obj.render(obj2[12], True, black)      
        text_center = (w12-17,h12-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w5+30,h5+20),(w12-30,h12),10)

    if obj2[13] != '--': 
        pygame.draw.circle(screen,green,(w13,h13),50)
        text_surface_obj = font_obj.render(obj2[13], True, black)   
        text_center = (w13-17,h13-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w6-30,h6+20),(w13+30,h13),10)

    if obj2[14] != '--': 
        pygame.draw.circle(screen,green,(w14,h14),50)
        text_surface_obj = font_obj.render(obj2[14], True, black)
        text_center = (w14-17,h14-30)
        screen.blit(text_surface_obj, text_center)
        pygame.draw.line(screen,red,(w6+30,h6+20),(w14-30,h14),10)

    #update the display
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
print('Pygame  is Done....')
#--------------------------- Emd program--------------------#
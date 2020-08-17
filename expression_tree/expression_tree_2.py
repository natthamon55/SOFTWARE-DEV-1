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
        self.prefix = ['None']*20

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

        #add operator and operand to self.prefix
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

        return self.prefix

# test program
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
scr_w, scr_h = 1000, 700
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
# rgb color
black = (0,0,0)
red   = (255,0,0)
green = (0, 255, 0)
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
#---------------------------------End Program----------------------------#






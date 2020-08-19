#student id : 6201012620139
#Name : Natthamon Bunnithi
#expression tree
#ref1 : https://riptutorial.com/pygame/example/21726/drawing-shapes--text-and-images-on-the-screen-with-a-small-animation
#ref2 : https://www.daniweb.com/programming/software-development/code/454765/save-a-pygame-drawing 
#ref3 : http://python.algorithmexamples.com/web/data_structures/stacks/infix_to_prefix_conversion.html
import pygame
import pygame.image
from pygame.locals import *
import sys #access to some variables used or maintained

#-----------------------------class of expression tree boolean-----------------------------------#
class stack():   
     
    def __init__(self):        
        self.postfix = []
        self.stack = []

    #for check if postfix is empthy
    def is_empty(self):
        return self.stack == []

    #add value to stacks
    def push(self,x) :
        self.stack.append(x)

    #deleat and show last element of stack
    def pop(self) :
        #self.stack.append(x)
        self.stack.pop()

    #get the last element of stack
    def top(self):
        return self.stack[-1]

# transform infix to postfix   
def infix_2_postfix(equation) : 
        S = stack()
        equ = equation.split()
        priority = {'!':3, '&':2, '+':2, '(':1}
        operator1 = '+&!'
        operand1 = "I0I1I2I3I4I5I6I7I8I9I10"

        for x in equ :
            if x in operand1 :
                S.postfix.append(x)
            elif x in operator1 :
                if not S.is_empty() and priority[x] <= priority[S.top()]:
                    S.postfix.append(S.stack.pop()) 
                S.push(x)
            elif x == '(':
                S.push(x)
            elif x == ')' :
                while (len(S.stack) != 0) and (S.top() != "("):
                    S.postfix.append(S.pop())
                S.stack.pop()

        # if true will return the output of postfix
        while not S.is_empty() : 
            S.postfix.append(S.stack.pop())

        print('infix is {}'.format(equation))
        print('postfix is: {}'.format(S.postfix))
        
        return S.postfix

#-------------------------Expression Tree----------------------#
class exp_tree():
    def __init__(self,equation):
        self.data = infix_2_postfix(equation)
        self.nodedata = []
        self.nodetree = []

    
        for i in range(len(self.data)):
            self.nodedata.append(self.data[len(self.data)-i-1]) 
        
        i=0
        while True :                                  
            if len(self.nodedata) <= (2**(i))-1 :      
                temp = 2**(i) - 1                   
                break                                               
            else : 
                i += 1
                 
        self.nodetree = ['None'] * 500

    def node(self) :                           
        p = 0 
        operand1 = "I0I1I2I3I4I5I6I7I8I9I10" 
                                             
        for i in self.nodedata :       
            self.left = (p * 2) + 1                        
            self.right = (p * 2) + 2                      
            if i in operand1 :                         
                if self.nodetree[p] in '+&':
                    if self.nodetree[self.left] == 'None' :      
                        self.nodetree[self.left] = i
                    elif self.nodetree[self.right] == 'None' : 
                        self.nodetree[self.right] = i
                    
                elif self.nodetree[p] == '!' and self.nodetree[self.left] == 'None' :
                    self.nodetree[self.left] = i
                    
                else :
                    for k in range( len(self.nodetree)-1 , -1 , -1 ):                      
                        if self.nodetree[k] in '+&':                              
                            par = k                             
                            self.left = (par * 2) + 1             
                            self.right = (par * 2) + 2
                            if self.nodetree[self.right] == 'None':
                                p = self.right
                                self.nodetree[p] = i
                                break
                        

            elif i in '+&!' :
            
                if self.nodetree[p] == 'None' :      
                    self.nodetree[p] = i        

                
                elif self.nodetree[p] == '!' and self.nodetree[self.left] == 'None' :                 
                    self.nodetree[self.left] = i
                    p = self.left

                elif self.nodetree[p] != '!' and self.nodetree[self.left] == 'None':
                    self.nodetree[self.left] = i
                    p = self.left

                elif self.nodetree[p] != '!' and self.nodetree[self.right] == 'None' :             
                    self.nodetree[self.right] = i   
                    p = self.right 
        
                elif self.nodetree[p] in '+&' and self.nodetree[self.left] != 'None' and self.nodetree[self.right] != 'None' :
                    for k in self.nodetree:                      
                        if k in '+&':                            
                            par = self.nodetree.index(k)        
                            self.left = (par * 2) + 1             
                            self.right = (par * 2) + 2
                            p = self.right
                            self.nodetree[p] = i
                            break
                                   
               
                elif self.nodetree[p] == '!' and self.nodetree[self.left] != 'None' :
                    for k in range( len(self.nodetree)-1 , -1 , -1 ):                      
                        if self.nodetree[k] in '+&':                              
                            par = k                             
                            self.left = (par * 2) + 1             
                            self.right = (par * 2) + 2
                            if self.nodetree[self.right] == 'None':
                                p = self.right
                                self.nodetree[p] = i
                                break
        return self.nodetree

#---------------- test program-----------------#
#exp1 = exp_tree("! ( 1 + 0 )")
exp2 = exp_tree("! ( ! ( 0 + I0 & 1 ) )")
#exp3 = exp_tree("( I0 + ! I1 + ! ( I2 ) ) &  ( ! I0 + I1 + I2 )")
#exp4 = exp_tree("! ( I0 & I1 ) + ! ( I1 + I2 )")
#exp5 = exp_tree("( ( ( I0 & I1 & ! I2 ) + ! I1 ) + I3 )")

#draw_node = exp1.node()
draw_node = exp2.node()
#draw_node = exp3.node()
#draw_node = exp4.node()
#draw_node = exp5.node()

#-------------------Pygame----------------------------#
# initialize PyGame
pygame.init()
pygame.display.set_caption('Expression Tree') 
scr_w, scr_h = 1100, 500
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# rgb color
black = (0,0,0)
red   = (255,0,0)
green = (0, 255, 0)

#font of text
text_font = pygame.font.Font('freesansbold.ttf', 40)

#create_text
def create_text(text,x,y):                                         
    text_surface = text_font.render( text, False, black )
    text_rect = text_surface.get_rect()
    text_rect.center = ( x,y )
    surface.blit( text_surface , text_rect )
    return 0


def get_height(tree):           
    tree.reverse()              
    item = ''                   
    for i in tree:
        if i == 'None':
            pass
        else :
            item = i
            break
    last_n = len(tree) - tree.index(i) 
    print('last_node is in index :',last_n)

    h = 0
    while True:                             
        if last_n <= (2**h)-1:              
            break
        else : 
            h += 1
    print('height of tree is : ', h)
    tree.reverse()                          
    return h

height = get_height(make_node)
w_list = []
h_list = []
h = 50                         
w_list.append(scr_w // 2)       
h_list.append(h)


for n in range(1,height):                       
    part = 2**n +1                              
                                               
    w_diff = scr_w // part                      
    h += 50                                     
    for i in range(1,part):                    
        w = w_diff * i                         
        w_list.append(w)
        h_list.append(h)

#-------------------Create node----------------------------#
class Node():                          
    def __init__(self,value,x,y):
        self.value = value
        self.r = 15
        self.x = x
        self.y = y
        self.draw = pygame.draw.circle(surface, green, (self.x,self.y), self.r ,0)
        self.text = create_text(self.value, self.x, self.y)


def draw_tree(nodetree):
    for i in range(len(nodetree)):          
        if nodetree[i] != 'None':                                   
            node = Node(nodetree[i],w_list[i],h_list[i])            

def draw_line(nodetree):
    for i in range(len(nodetree)) :      
        if nodetree[i] in '+&!':                
            left = (i * 2) + 1                        
            right = (i * 2) + 2
            if nodetree[left] != 'None':
                pygame.draw.line(surface, red, (w_list[i],h_list[i]) , (w_list[left],h_list[left]), 5)
                if nodetree[right] != 'None':
                    pygame.draw.line(surface,red, (w_list[i],h_list[i]) , (w_list[right],h_list[right]), 5)

#-------------------Running Pygame-------------------------------------------#
fname='expression_tree.jpg' #name of picture file (.jpg)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False
            #save image file to directory    
            pygame.image.save(screen,fname)
            print("file {} has been saved".format(fname))


    draw_line(draw_node)       
    draw_tree(draw_node)
    
    #update the display
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
print('Pygame  is Done....')
#--------------------------- End program--------------------#

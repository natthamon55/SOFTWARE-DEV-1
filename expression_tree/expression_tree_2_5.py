#student id : 6201012620139
#Name : Natthamon Bunnithi
#expression tree
#ref1 : https://riptutorial.com/pygame/example/21726/drawing-shapes--text-and-images-on-the-screen-with-a-small-animation
#ref2 : https://www.daniweb.com/programming/software-development/code/454765/save-a-pygame-drawing 
#ref3 : http://python.algorithmexamples.com/web/data_structures/stacks/infix_to_prefix_conversion.html
import pygame
import pygame.image
from pygame.locals import *
from random import choice
import sys #access to some variables used or maintained

class stack():
    def __init__(self):
        self.stack = list()
        self.postfix = list()
    #check if stack is empthy
    def is_empty(self):                      
        if len(self.stack) == 0:
            return True
        else : False
    #add item to stack
    def push(self,i):                   
        self.stack.append(i)        
    #removes and returns the last item in stack
    def pop(self):                         
        self.stack.pop()
    #return the last item of stack
    def top(self):                         
        return self.stack[-1]

# change infix equation to postfix equation
def infix_2_postfix(equation): 
    s = stack() #instant variable of class stack
    equ = equation.split()   #keep equation in list pattern
    priority = {'!':3, '&':2, '+':2, '(':1}
    operand = "I0I1I2I3I4I5I6I7I8I9I10" 
    operator = '&!+'
    
    for i in equ:
        if i in operand : #if i is operand add to postfix              
            s.postfix.append(i)
        elif i in operator :                                   
            if not s.is_empty() and priority[i] <= priority[s.top()]:  # while stack is not empthy anf priority of i is not greater than priority of element in the stack     
                s.postfix.append(s.stack.pop())   # pop stack & add to Postfix                      
            s.push(i)                                               
        elif i == '(':
            s.push(i) # if i is "(" push to Stack
        elif i == ')':
            while (len(s.stack) > 0) and (s.top() != "("):
                s.postfix.append(s.stack.pop()) # pop stack & add to Postfix  
            s.stack.pop()
    
    while not s.is_empty():                        
        s.postfix.append(s.stack.pop())
    
    print('infix is {} '.format(equation))
    print('postfix is {}'.format(s.postfix))

    return s.postfix #return the output of postfix

#--------------------------Expression Tree------------------------------------------#
class exp_tree():
    
    def __init__(self,equation):
        self.data = infix_2_postfix(equation)
        self.nodedata = []
        self.nodetree = []

        for i in range(len(self.data)): #reverse equation from infix_2_postfix
            self.nodedata.append(self.data[len(self.data)-i-1])
        
        i=0
        while True :                                  
            if len(self.nodedata) <= (2**(i))-1 : # (2**(i))-1 for calc size of tree      
                temp = 2**(i) - 1                    
                break                                               
            else : 
                i += 1
                        
        self.nodetree = ['None'] * 500 #create for keep element of tree

    #transform to tree pattern
    def do_tree(self) :                          
        p = 0     #p is oarent
        op = "I0I1I2I3I4I5I6I7I8I9I10"                         
        for i in self.nodedata :       
            self.left = (p * 2) + 1  #search position for left node                     
            self.right = (p * 2) + 2  #search position for right node                     

            if i in op:  #if i is operand put in empthy node                      
                if self.nodetree[p] in '+&': #if node parent have operator in node
                    if self.nodetree[self.left] == 'None' :      
                        self.nodetree[self.left] = i  #put operand in left node
                    elif self.nodetree[self.right] == 'None' : 
                        self.nodetree[self.right] = i   #put operand in right node
                    
                elif self.nodetree[p] == '!' and self.nodetree[self.left] == 'None' :
                    self.nodetree[self.left] = i
                    
                else : #check every item in  nodetree list that there is an operator but no child on left/right node
                    for k in range( len(self.nodetree)-1 , -1 , -1 ):                     
                        if self.nodetree[k] in '+&':                             
                            par = k                             
                            self.left = (par * 2) + 1             
                            self.right = (par * 2) + 2
                            if self.nodetree[self.right] == 'None':
                                p = self.right
                                self.nodetree[p] = i
                                break
                        

            elif i in '+&!' : #if i is operator 
            
                if self.nodetree[p] == 'None' :  #if parent node empthy put operator on it   
                    self.nodetree[p] = i        

              
                elif self.nodetree[p] == '!' and self.nodetree[self.left] == 'None' :    #If child node left  is empty put value and have the child on the left node as the parent.            
                    self.nodetree[self.left] = i
                    p = self.left

                elif self.nodetree[p] != '!' and self.nodetree[self.left] == 'None':
                    self.nodetree[self.left] = i
                    p = self.left

                elif self.nodetree[p] != '!' and self.nodetree[self.right] == 'None' : #If child node right  is empty put value and have the child on the right node as the parent.              
                    self.nodetree[self.right] = i   
                    p = self.right 

                #if node parent have +& and left-right node is not empthy
                elif self.nodetree[p] in '+&' and self.nodetree[self.left] != 'None' and self.nodetree[self.right] != 'None' :
                    for k in self.nodetree:                      
                        if k in '+&':                            
                            par = self.nodetree.index(k)        
                            self.left = (par * 2) + 1             
                            self.right = (par * 2) + 2
                            p = self.right
                            self.nodetree[p] = i
                            break
                                   
                #if node parent have ! and left node is not empthy
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


#-------------------Test Program------------------------------#

#exp1 = ! ( 1 + 0 )
#exp2 = ! ( ! ( 0 + I0 & 1 ) )
#exp3 = ( I0 + ! I1 + ! ( I2 ) ) & ( ! I0 + I1 + I2 )
#exp4 = ! ( I0 & I1 ) + ! ( I1 + I2 )  
#exp5 = ( ( ( I0 & I1 & ! I2 ) + ! I1 ) + I3 )

#---------------------------------------------------------------#

exp = input('Please input your equation :')
print('------------------------------------------------------------------')
exp1 = exp_tree(exp)
draw_node = exp1.do_tree()

#-------------------Pygame----------------------------#
# initialize PyGame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Expression Tree Infix_2_Postfix') 
scr_w, scr_h = 1100, 500
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#font of text
text_font = pygame.font.Font('freesansbold.ttf', 20)
#rgb color
black = (0,0,0)
gray = (192,192,192)
white =(255,255,255)
pink =(255,204,229)

#create text
def do_text(text,x,y):                                          
    text_surface = text_font.render( text, False, black )
    text_center = ( x,y )
    surface.blit( text_surface , text_center)
    return 0

#get height of tree
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

    print('-----------------------------------------------------------------------')
    print('last_node is in index  {}'.format(last_n))

    h = 0
    while True:                             
        if last_n <= (2**h)-1:   # (2**h)-1 this equation can find height of tree 
            break
        else : 
            h += 1
    
    print('height of tree is {}'.format(h))
    tree.reverse()                          
    return h

height = get_height(draw_node)
#width and height 
w_list = []
h_list = []
h = 50                          
w_list.append(scr_w // 2)       
h_list.append(h)

#divide width and increase hight
for n in range(1,height):                       
    part = 2**n +1                              
                                                
    w_diff = scr_w // part                      
    h += 50                                     
    for i in range(1,part):                    
        w = w_diff * i                          
        w_list.append(w)
        h_list.append(h)

class Node():                          
    def __init__(self,value,x,y):
        self.value = value
        self.r = 20
        self.x = x
        self.y = y
        self.draw = pygame.draw.circle(surface,rd_color(), (self.x,self.y), self.r ,0)
        self.text = do_text(self.value, self.x, self.y)
#random color
COLORS = [(119, 141, 252), 
          (119, 252, 181),
          (252, 243, 119),
          (225,142,197),
          (253,170,115)]
def rd_color():
    return choice(COLORS)

#draw tree
def draw_tree(nodetree):
    for i in range(len(nodetree)):          
        if nodetree[i] != 'None':  #if node have value draw this node with x,y position                           
            node = Node(nodetree[i],w_list[i],h_list[i])            
#draw Welding line for connect node
def draw_line(nodetree):
    for i in range(len(nodetree)) :      
        if nodetree[i] in '+&!':               
            left = (i * 2) + 1                        
            right = (i * 2) + 2
            if nodetree[left] != 'None':
                pygame.draw.line(surface,white, (w_list[i],h_list[i]) , (w_list[left],h_list[left]), 5)
                if nodetree[right] != 'None':
                    pygame.draw.line(surface,white, (w_list[i],h_list[i]) , (w_list[right],h_list[right]), 5)

#----------------------Running Pygame--------------------------------#
fname='expression_tree.jpg' #name of picture file (.jpg)
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False
            #save image file to directory    
            pygame.image.save(screen,fname)
            print('--------------------------------------------------------------------')
            print("file {} has been saved".format(fname))

    #fill the screen with gray
    screen.fill(gray)
    
    draw_line(draw_node)        
    draw_tree(draw_node)
    
    #update the display
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()


pygame.quit()
print('Pygame  is Done....')
#--------------------------- End program--------------------#


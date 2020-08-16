#student id : 6201012620139
#ref1 : https://riptutorial.com/pygame/example/21726/drawing-shapes--text-and-images-on-the-screen-with-a-small-animation
#ref2 : https://www.daniweb.com/programming/software-development/code/454765/save-a-pygame-drawing 
#ref3 : https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
#expression tree
import pygame
import pygame.image
from pygame.locals import *
import sys #access to some variables used or maintained

# initialize PyGame
pygame.init()
pygame.display.set_caption('Expression Tree') 
scr_w, scr_h = 1000, 700
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#class of expression tree boolean
class boolean_tree:   
     
    def __init__(self, capacity): 
        self.top = -1 
        self.capacity = capacity 
        # This stack is used a stack  
        self.stack = [] 
        # Precedence setting 
        self.output = [] 
        self.operator = {'+':1, '&':1, '!':2} 
        #operand
        self.operand = ['0','1','l0','l1','l2','l3']
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of  stack 
    def peek(self): 
        return self.stack[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.stack.pop() 
        else: 
            return "emthy stack"
  
    # add the element to the stack 
    def push(self,op): 
        self.top += 1
        self.stack.append(op)  
  
    # Check if the operator is strictly 
    # less than top of stack or not 
    def notGreater(self, i): 
        try: 
            a = self.operator[i] 
            b = self.operator[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
              
    # convert infix tp postfix
    def infixToPostfix(self, exp): 
           # Iterate over the expression for conversion 

        for i in exp: 
            if i in self.operand :
                self.output.append(i)
            elif i in self.operator:
                if len(self.stack) != 0 and self.operator[i] <= self.operator[self.stack[-1]]:
                    self.output.append(self.stack.pop())
                self.stack.append(i)
            
            # If the character is an '(', push it to stack 
            elif i  == '(': 
                self.push(i) 
  
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif i == ')': 
                while( (not self.isEmpty()) and self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
  
            # An operator is encountered 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 
  
        # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
        print ('postfix is {}'.format(self.output)) 
  
# test program
#exp1 = "!(1+0)"
#exp2 = "!(!(0+I0&1))"
#exp3 = "(I0+!I1+!(I2))&(!I0+I1+I2)"
#exp4 = "!(I0&I1)+!(I1+I2)"
#exp5 = "(((I0&I1&!I2)+!I1)+I3)"
exp = '!(1+0)'
obj = boolean_tree(len(exp)) 
print('infix is {}'.format(exp))
obj.infixToPostfix(exp) 



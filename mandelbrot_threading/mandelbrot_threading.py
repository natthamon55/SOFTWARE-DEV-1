# student id: 6201012620139
#ref :python_threading_demo-8.py by RSP
import threading
import time
import cmath 
import pygame
from random import randint, randrange, random

print( 'File:', __file__ )

def mandelbrot(c,max_iters=100):  
    i = 0
    z = complex(0,0)    # z start complex from 0
    while abs(z) <= 2 and i < max_iters:
        z = z * z  + c      
        i += 1 
    return i

# initialize pygame
pygame.init()
# create a screen of width=600 and height=400
scr_w, scr_h = 600, 400
screen = pygame.display.set_mode( (scr_w, scr_h) )
# set window caption
pygame.display.set_caption(' Mandelbrot') 
# create a clock
clock = pygame.time.Clock()
# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
# half width, half screen
w_2, h_2 = scr_w/2, scr_h/2 

# set the number of threads to be created
N = 100
# create a barrier and thread lock 
barrier = threading.Barrier(N+1)
lock = threading.Lock()
# create a list of semaphores 
semaphores_list = [ threading.Semaphore(0) for i in range(N) ]
#create a list for keeping  thread 
threading_list = []

# global variable 
stop_thread = False
#function of threading
def threading_work (id,surface,lock,barrier):
    global stop_thread
    scale = 0.008
    offset = complex(-0.55,0.0)  
    y_min = id * 4
    
    for y in range(y_min, scr_w):
        for x in range(scr_w):
            re = scale*(x-w_2) + offset.real
            im = scale*(y-h_2) + offset.imag

            c = complex( re, im )
            color = mandelbrot(c, 63)
            r = (color << 9) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 1) & 0xc0
            with lock:
                surface.set_at( (x, y), (255-r,255-g,255-b) )
            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                pass
# create a number of threads (e.g, N=100)
for i in range(N):
    id = (i+1)
    t1 = threading.Thread(target=threading_work, args=(id,surface,lock,barrier)) #sent to paremeter of def threading_work
    t1.setName( 'Thread-{}'.format(id) )
    threading_list.append(t1)

# start each of the threads in the list
for t1 in threading_list :
    t1.start()

running= True
while running:
    clock.tick(2000000) #update the clock
    with lock:
        screen.blit( surface, (0,0) ) # draw the surface on the screen
    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        pass
 
    ev=pygame.event.get()

    for event in ev :
        if event.type == pygame.QUIT:
            running = False
   
    pygame.display.update() #update the display

#exit from pygame
pygame.quit()
print( 'PyGame is done')

############################################

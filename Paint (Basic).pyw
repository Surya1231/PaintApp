import pygame
from pygame.locals import *
from sys import exit

WHITE = (255,255,255)
RED =  (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

def main():
    global displa , color
    
    pygame.init()
    displa=pygame.display.set_mode((400,400))
    pygame.display.set_caption("Yo Yo")
    displa.fill((255,255,255))
    t=0
    ini()
    color=(0,0,255)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONUP:
                t=0
                x,y=event.pos
                click(x,y)
            elif t==1:
                x,y=event.pos
                drawi(x,y,color)
            elif event.type == MOUSEBUTTONDOWN:
                t=1     
        pygame.display.update()

    
def click(x,y):
    global color
    if 10<=y<=45:
        if 10<=x<=45:
            color=(255,255,255)
        elif 65<=x<=100:
            color=RED
        elif 115<=x<=150:
            color=GREEN
        elif 165<=x<=200:
            color=BLUE
        elif 215<=x<=240:
            color=BLACK
        
def drawi(x,y,c):
    if y>55 and x>5 and x<395 and y<395:
        if c==(255,255,255):
            if y>65 and y<384 and x>17 and x<383:
                pygame.draw.circle(displa,c,(x,y),15)
        else:
            pygame.draw.circle(displa,c,(x,y),3)
                      
def ini():
    eraser=pygame.image.load('eraser.png')
    eraser1=pygame.transform.scale(eraser,(35,35))
    pygame.draw.rect(displa,BLACK, (0,0,398,398),2)
    pygame.draw.line(displa,BLACK , (0,50),(399,50),2)
    displa.blit(eraser1,(10,10))
    pygame.draw.rect(displa,RED,(65,10,35,35))
    pygame.draw.rect(displa,GREEN,(115,10,35,35))
    pygame.draw.rect(displa,BLUE,(165,10,35,35))
    pygame.draw.rect(displa,BLACK,(215,10,35,35))

main()
    






    



    
            

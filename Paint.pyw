import pygame
from pygame.locals import *
from sys import exit

WHITE = (255,255,255)
RED =  (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
BLUE2= (0, 255,255)
ORANGE = (255,128,0)
GRAY = (192,192,192)
GRAY2= (64,64,64)
HL =(255,255,0)
PINK= (255,0,255)

BLACK1= [ BLACK,(32,32,32),GRAY2,(100,100,100),GRAY]
BLUE1= [BLUE, (51,51,255),(102,102,255),BLUE2,(0,204,204)]
GREEN1= [GREEN,(51,255,51),(102,255,102),(128,255,0),(178,255,102)]
RED1= [RED,(255,51,51),(255,102,102),(102,0,0),(153,0,0)]
YELLOW1= [(255,255,0),(255,255,51),(255,255,102),(255,255,153),(255,255,204)]
ORANGE1 =[ORANGE,(255,153,51),(255,178,102),(204,102,0),(255,204,153)]
PURPLE1= [(152,52,255),(178,102,255),(204,153,255),(153,0,153),(204,0,204)]
PINK1= [PINK,(255,0,127),(255,51,153),(255,102,178),(255,153,204)]

color = [BLACK1,BLUE1,GREEN1,RED1,YELLOW1,ORANGE1 ,PURPLE1,PINK1]
def main():
    global win
    hl=[2,1,1,0]

    pygame.init()
    win=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Surya Paint")
    box()
    t=0

    while True:
        if t==0:
            drawside(hl)
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONUP:
                x,y=event.pos
                click(x,y,hl)
                drawing(x,y,x1,y1,x,y,hl)
                t=0
            elif event.type == MOUSEBUTTONDOWN:
                x1,y1=event.pos
                t=1
            elif t==1:
                x,y=event.pos
                drawing(x,y,x1,y1,0,0,hl)
            elif event.type == MOUSEMOTION:
                x,y=event.pos
                highllight(x,y)
        pygame.display.update()

def box():
    win.fill(WHITE)
    pygame.draw.rect(win,BLACK,(0,0,998,20),1)
    pygame.draw.rect(win,BLACK,(100,20,898,578),1)

def drawside(hl):
    pygame.draw.line(win,BLACK,(0,20),(0,600),2)
    pygame.draw.rect(win,GRAY,(2,20,98,580))

    eraser=pygame.image.load('eraser.png')
    eraser1=pygame.transform.scale(eraser,(32,32))
    pencil=pygame.image.load('pencil.png')
    pencil1=pygame.transform.scale(pencil,(32,32))
    line=pygame.image.load('line.png')
    line1=pygame.transform.scale(line,(32,32))
    clear=pygame.image.load('clear.png')
    clear1=pygame.transform.scale(clear,(32,32))
    
    win.blit(line1,(12,32))
    win.blit(pencil1,(56,32))
    pygame.draw.rect(win,(64,64,64),(12,84,32,32))
    pygame.draw.circle(win,(64,64,64),(72,100),16)
    win.blit(eraser1,(12,136))
    win.blit(clear1,(56,136))
    pygame.draw.rect(win,BLACK,(12,188,32,32),1)
    pygame.draw.rect(win,BLACK,(56,188,32,32),1)
    pygame.draw.line(win,BLACK,(12,240),(88,240),2)
 
    for i in range(0,8,2):
        pygame.draw.rect(win,color[i][0],(12,264+i*24,32,32))
        pygame.draw.rect(win,color[i+1][0],(56,264+i*24,32,32))
    pygame.draw.line(win,BLACK,(12,460),(88,460),2)

    co=[GRAY2]*5
    co[hl[2]-1]=WHITE
    l,v=475,510
    pygame.draw.line(win,co[0],(10,l),(10,v),2)
    pygame.draw.line(win,co[1],(25,l),(25,v),4)
    pygame.draw.line(win,co[2],(40,l),(40,v),6)
    pygame.draw.line(win,co[3],(60,l),(60,v),8)
    pygame.draw.line(win,co[4],(80,l),(80,v),10)

    pygame.draw.line(win,BLACK,(12,520),(88,520),2)
    for i in range(5):
        pygame.draw.rect(win,color[hl[1]-1][i],(12+i*18,535,6,30))    

    l,v=get(hl[0])
    pygame.draw.rect(win,WHITE,(l,28+v*52,40,40),4)
    l,v=get(hl[1])
    pygame.draw.rect(win,WHITE,(l,260+48*v,38,38),4)
    pygame.draw.rect(win,WHITE,(9+hl[3]*18,533,9,33),3)

def get(h):
    if h%2!=0:
        return 8,(h-1)//2
    return 52,(h-1)//2

def click(x,y,hl):
    if y>=264 and y<=440 and x>=12 and x<=88:
        l=2
        if x<50:
            l=1
        hl[1]=2*((y-264)//48)+l
        hl[3]=0
    elif y>=32 and y<=216 and x>=12 and x<=88:
        l=2
        if x<50:
            l=1
        hl[0]=2*((y-32)//52)+l
    elif y>=475 and y<=510 and x>0 and x<100:
        hl[2]=x//20+1
    elif y>=535 and y<=565 and x>0 and x<100:
        hl[3]=x//20

def drawing(x,y,x1,y1,x2,y2,h):
    if x>102 and x<998 and y>=22 and y<598:
        if h[0]==1 and x2!=0:
            pygame.draw.line(win,color[h[1]-1][h[3]],(x1,y1),(x2,y2),h[2]*4)
        elif h[0]==2:
            pygame.draw.circle(win,color[h[1]-1][h[3]],(x,y),h[2]*4)
        elif h[0]==3:
            pygame.draw.rect(win,color[h[1]-1][h[3]],(x1,y1,x-x1,y-y1))
        elif h[0]==4:
            pygame.draw.circle(win,color[h[1]-1][h[3]],(x1,y1),abs(x-x1))
        elif h[0]==5:
            pygame.draw.circle(win,WHITE,(x,y),h[2]*4)
        elif h[0]==6:
            box()

def highllight(x,y):
    if y>=264 and y<=440 and x>=12 and x<=88:
        l=2
        if x<50:
            l=1
        k=2*((y-264)//48)+l
        l,v=get(k)
        pygame.draw.rect(win,HL,(l,260+48*v,38,38),4)
    elif y>=32 and y<=216 and x>=12 and x<=88:
        l=2
        if x<50:
            l=1
        k=2*((y-32)//52)+l
        l,v=get(k)
        pygame.draw.rect(win,HL,(l,28+v*52,40,40),4)
        
main()
    






    



    
            

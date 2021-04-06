import pygame
import sys
import numpy as np

pygame.init()
loun = (50, 150, 152)
loun2 = (255,255,255)
ecran = pygame.display.set_mode((600, 600))
pygame.display.set_caption("XO BELTOUNSI")
ecran.fill(loun)
board = np.zeros((3,3))
print(board)
#pygame.draw.line(ecran, loun2,(10,10),(300,300),10)
def sawer():
    pygame.draw.line(ecran, loun2,(0,200),(600,200),15)
    pygame.draw.line(ecran, loun2,(0,400),(600,400),15)
    pygame.draw.line(ecran, loun2,(200,0),(200,600),15)
    pygame.draw.line(ecran, loun2,(400,0),(400,600),15)

def sawerXO():
    for row in range(3):
        for col in range(3):
            if board[row][col] ==1:
                pygame.draw.circle(ecran,loun2,(int(col*200+200/2),int(row *200+200/2)),60,15)
            elif board[row][col] ==2:
                pygame.draw.line(ecran,loun2,(col*200 + 55,row *200+200-55),(col *200+200-55,row*200 +55),30)
                pygame.draw.line(ecran,loun2,(col*200 + 55,row *200+55),(col *200+200-55,row*200+200 -55),30)

def gamer(row,col,player):
    board[row][col] = player

def mawjoud(row,col):
    return board[row][col] ==0

def t3aba():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def chkounrbe7(player):
    for col in range(3):
        if board[0][col]== player and board[1][col] ==player and board[2][col] ==player:
            sawer_vert(col,player)
            return True
    for row in range(3):
        if board[row][0]== player and board[row][1] ==player and board[row][2] ==player:
            sawer_hor(row,player)
            return True

    if board[2][0]== player and board[1][1] ==player and board[0][2] ==player:
       sawer_diag(player)
    if board[0][0]== player and board[1][1] ==player and board[2][2] ==player:
        sawer_diag2(player)
    
def sawer_vert(col,player):
    posX= col * 200 +100
    if player == 1 :
        color = loun2
    if player == 2 :
        color = loun2
    pygame.draw.line(ecran,color,(posX,15),(posX,600-15),15)

def sawer_hor(row,player):
    posO= row * 200 +100
    if player == 1 :
        color = loun2
    if player == 2 :
        color = loun2
    pygame.draw.line(ecran,color,(15,posO),(600-15,posO),15)
def sawer_diag(player):
   
    if player == 1 :
        color = loun2
    if player == 2 :
        color = loun2
    pygame.draw.line(ecran,color,(15,600-15),(600-15,15),15)
def sawer_diag2(player):
    
    if player == 1 :
        color = loun2
    if player == 2 :
        color = loun2
    pygame.draw.line(ecran,color,(15,15),(600-15,600-15),15)
def aawed():
    pass


sawer()
player = 1
dam_lfareh = False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not(dam_lfareh):



            X = event.pos[0]
            O = event.pos[1]

            clicked_row = int(O // 200)
            clicked_col = int(X//200)
            if mawjoud(clicked_row,clicked_col):
                if player == 1:
                    gamer(clicked_row,clicked_col,1)
                    if chkounrbe7(player): 
                        dam_lfareh= True
                    player =2
                elif player ==2 :
                    gamer(clicked_row,clicked_col,2)
                    if chkounrbe7(player): 
                        dam_lfareh= True
                    player = 1
                sawerXO()
                print(board)
    pygame.display.update()
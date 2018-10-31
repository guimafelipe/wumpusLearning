from board import *
from utility import *
import pygame
from pygame.locals import *
import sys
from sys import exit
import math

N = 4
M = 8

WHITE		= (255, 255, 255)
BLACK		= (  0,   0,   0)
BLUE		= (  0,   0, 255)
GREEN		= (  0, 255,   0)
RED			= (255,   0,   0)
ORANGE		= (255, 165,   0)
GREY		= (128, 128, 128) 
YELLOW		= (255, 255,   0)
PINK		= (255, 192, 203)
LBLUE 		= (191, 238, 244)
BOARD_L		= (219, 202, 142)
BOARD_D		= ( 58,  41,  14)

pygame.init()

screen_size = 900

screen = pygame.display.set_mode((screen_size, screen_size), 0, 32)
screen.fill(WHITE)

pygame.display.set_caption("Wumpus learning")

clock = pygame.time.Clock()

snap = 100

pygame.font.init()
myfont = pygame.font.SysFont('Sans Serif', math.ceil(snap*1.5))

arrow = pygame.image.load("assets/arrow.png").convert()
arrow = pygame.transform.scale(arrow, (snap, snap))
arrow.set_alpha(250)
arrow.set_colorkey((0,0,0))

def move(i, j, ut, bo): # N = 0, L = 1, S = 2, O = 3
    rf = bo.board[i][j].r
    gamma = 1
    value, direction = rf + gamma*(0.6*ut.get(i-1,j) + 0.4*ut.get(i,j+1)), 0

    curr_val = rf + gamma*(0.6*ut.get(i,j-1) + 0.4*ut.get(i-1,j))
    if curr_val > value:
        value, direction = curr_val, 1

    curr_val = rf + gamma*(0.6*ut.get(i+1,j) + 0.4*ut.get(i,j-1))
    if curr_val > value:
        value, direction = curr_val, 2

    curr_val = rf + gamma*(0.6*ut.get(i,j+1) + 0.4*ut.get(i+1,j))
    if curr_val > value:
        value, direction = curr_val, 3

    return value, direction


def bellman_it(ut, bo):
    nu = Utility(N, M, bo)
    policy = [[0 for i in range(M)]for j in range(N)] # There is no point of doing this everytime, but whatever
    for i in range(1, N+1):
        for j in range(1, M+1):
            if(bo.board[i][j].reset == False):
                nu.board[i][j], policy[i-1][j-1] = move(i, j, ut, bo)
            else:
                nu.board[i][j] = bo.board[i][j].r
    
    return nu, policy


if __name__ == "__main__":
    b = Board(N,M)
    b.add_gold(2,2)
    b.add_gold(3,6)
    b.add_wumpus(2,1)
    b.add_wumpus(3,5)
    b.add_pit(1,2)
    b.add_pit(1,7)
    b.add_pit(2,3)
    b.add_pit(2,7)
    b.add_pit(4,3)
    b.add_pit(4,7)

    u = Utility(N, M, b)
    policy = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            print(b.board[i][j].r, " ", end='')
        print()
    for k in range(200):
        u, policy = bellman_it(u, b)
    
        for i in range(1, N+1):
            for j in range(1, M+1):
                print("%8.2f" % (u.board[i][j]), " ", end='')
            print()
        print()

    for i in range(N):
        for j in range(M):
            pol = policy[i][j]
            if b.board[i+1][j+1].reset:
                char = "O"
            elif pol == 0:
                char = "^"
            elif pol == 1:
                char = "<"
            elif pol == 2:
                char = "v"
            elif pol == 3:
                char = ">"
            print(char, " ", end='')
        print()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        for i in range(N):
            for j in range(M):
                tipo = b.board[i+1][j+1].r
                if tipo == -50: # pit
                    pygame.draw.rect(screen, BOARD_D, [j*snap, i*snap, snap, snap])
                else:
                    pygame.draw.rect(screen, BOARD_L, [j*snap, i*snap, snap, snap])
                if tipo == -100:
                    pygame.draw.circle(screen, RED, [j*snap + int(snap/2), i*snap + int(snap/2)], int(snap/3))
                elif tipo == 100:
                    pygame.draw.circle(screen, ORANGE, [j*snap + int(snap/2), i*snap + int(snap/2)], int(snap/3))
                pygame.draw.rect(screen, BLACK, [j*snap, i*snap, snap, snap], 3)

                pol = policy[i][j]
                if b.board[i+1][j+1].reset:
                    pass
                elif pol == 0:
                    screen.blit(pygame.transform.rotate(arrow, 90), (j*snap, i*snap))
                elif pol == 1:
                    screen.blit(pygame.transform.rotate(arrow, 180), (j*snap, i*snap))
                elif pol == 2:
                    screen.blit(pygame.transform.rotate(arrow, 270), (j*snap, i*snap))
                elif pol == 3:
                    screen.blit(pygame.transform.rotate(arrow, 360), (j*snap, i*snap))
                

        
        pygame.display.update()
        time_passed = clock.tick(30000)
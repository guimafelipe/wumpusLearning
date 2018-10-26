from board import *
from utility import *

N = 4
M = 8

def move(i, j, ut, bo): # N = 0, L = 1, S = 2, O = 3
    rf = bo.board[i][j].r
    value, direction = rf + 0.6*ut.get(i-1,j) + 0.4*ut.get(i,j+1), 0

    curr_val = rf + 0.6*ut.get(i,j-1) + 0.4*ut.get(i-1,j)
    if curr_val > value:
        value, direction = curr_val, 1

    curr_val = rf + 0.6*ut.get(i+1,j) + 0.4*ut.get(i,j-1)
    if curr_val > value:
        value, direction = curr_val, 2

    curr_val = rf + 0.6*ut.get(i,j+1) + 0.4*ut.get(i+1,j)
    if curr_val > value:
        value, direction = curr_val, 3

    return value, direction


def bellman_it(ut, bo):
    nu = Utility(N,M, bo)
    policy = [[0 for i in range(M)]for j in range(N)]
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
    for k in range(100):
        u, policy = bellman_it(u, b)
    
        for i in range(1, N+1):
            for j in range(1, M+1):
                print(u.board[i][j], " ", end='')
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
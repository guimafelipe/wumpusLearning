from board import *
from utility import *

def move(i, j, ut, bo): # N = 0, L = 1, S = 2, O = 3
    rf = bo.board[i][j]
    value, direction = rf + 0.6*ut.get(i-1,j) + 0.4*ut.get(i,j-1), 0

    curr_val = rf + 0.6*ut.get(i,j-1) + 0.4*ut.get(i-1,j)
    if curr_val > value:
        value, direction = curr_val, 1

    curr_val = rf + 0.6*ut.get(i+1,j) + 0.4*ut.get(i,j-1)
    if curr_val > value:
        value, direction = curr_val, 2

    curr_val = rf + 0.6*ut.get(i+1,j) + 0.4*ut.get(i+1,j)
    if curr_val > value:
        value, direction = curr_val, 3

    return value, direction


def bellman_it(ut, bo):
    nu = Utility(4,8)
    policy = [[0]*4]*8
    for i in range(4):
        for j in range(8):
            if(bo.board[i][j].reset == False):
                nu = move(i, j, ut, bo)


if __name__ == "__main__":
    u = Utility(4, 8)
    b = Board(4,8)
    b.add_gold(1,1)
    b.add_gold(2,5)
    b.add_wumpus(1,0)
    b.add_wumpus(2,4)
    b.add_pit(0,1)
    b.add_pit(0,6)
    b.add_pit(1,2)
    b.add_pit(1,6)
    b.add_pit(3,2)
    b.add_pit(3,6)
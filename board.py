class Cell:
    def __init__(self, r, reset):
        self.r = r
        self.reset = reset # boolean, reset game for wumpuns or gold

class Board:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.move_cost = -0.1
        self.board = [[Cell(0, False)]*m]*n
    
    def move(self, i, j):
        if (i < 0 or i >= self.n) or (j < 0 or j >= self.m):
            return False, -10, False
        else:
            cell = self.board[i][j]
            return True, cell.r, cell.reset
    
    def add_wumpus(self, x, y):
        self.board[x][y] = Cell(-100, True)
    
    def add_gold(self, x, y):
        self.board[x][y] = Cell(100, True)
    
    def add_pit(self, x, y):
        self.board[x][y] = Cell(-50, False)
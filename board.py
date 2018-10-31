class Cell:
    def __init__(self, r, isWall, reset):
        self.r = r
        self.isWall = isWall
        self.reset = reset # boolean, reset game for wumpuns or gold

class Board:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = [[None for i in range(m+2)] for j in range(n+2)]
        for i in range(n+2):
            for j in range(m+2):
                self.board[i][j] = Cell(0, False, False)
        for i in range(m+2):
            self.board[0][i].isWall = True
            self.board[n+1][i].isWall = True
        for j in range(n+2):
            self.board[j][0].isWall = True
            self.board[j][m+1].isWall = True
    
    def move(self, i, j): #indexado em 1
        if (i < 0 or i >= self.n) or (j < 0 or j >= self.m):
            return False, -10, False
        else:
            cell = self.board[i][j]
            return True, cell.r, cell.reset
    
    def add_wumpus(self, x, y):
        self.board[x][y] = Cell(-100, False, True)
    
    def add_gold(self, x, y):
        self.board[x][y] = Cell(100, False, True)
    
    def add_pit(self, x, y):
        self.board[x][y] = Cell(-50, False, False)
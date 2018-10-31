class Utility:
    def __init__(self, n, m, b):
        self.n = n
        self.m = m
        self.board = [[0 for i in range(m+2)]for j in range(n+2)]
        self.info = b
    
    def get(self, i, j): #indexado em 1
        to_ret = -0.1
        if (i < 1 or i > self.n) or (j < 1 or j > self.m): # Detect wall
            to_ret -= 10
        elif self.info.board[i][j].reset: # Detect wumpus or gold
            return to_ret + self.info.board[i][j].r # Just return the reinforciment
        # Adjust bellow in case of wall
        if i < 1: i = 1
        if i > self.n: i = self.n
        if j < 1: j = 1
        if j > self.m: j = self.m
        
        return to_ret + self.board[i][j]
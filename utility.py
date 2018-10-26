class Utility:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = [[0]*m]*n
    
    def get(self, i, j):
        to_ret = 0
        if (i < 0 or i >= self.n) and (j < 0 or j >= self.m):
            to_ret -= 10
        if i < 0: i = 0
        if i >= self.n: i = self.n - 1
        if j < 0: j = 0
        if j >= self.m: j = self.m -1
        
        return to_ret + self.board[i][j]
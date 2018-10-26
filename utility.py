class Utility:
    def __init__(self, n, m, b):
        self.n = n
        self.m = m
        self.board = [[0 for i in range(m+2)]for j in range(n+2)]
        self.info = b
    
    def get(self, i, j):
        to_ret = -0.1
        if (i < 0 or i >= self.n) and (j < 0 or j >= self.m):
            to_ret -= 10
        elif self.info.board[i][j].reset:
            return self.info.board[i][j].r
        if i < 0: i = 0
        if i >= self.n: i = self.n - 1
        if j < 0: j = 0
        if j >= self.m: j = self.m -1
        
        return to_ret + self.board[i][j]
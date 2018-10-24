from board import *
from utility import *

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
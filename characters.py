import numpy as np
from config import *

class Base:
    def __init__(self):
        self.id = None
        self.size = []
        self.location = []

    def place(self, board, element):
        print(f"location: {self.location}")
        print(f"size: {self.size}")
        board[self.location[0] - self.size[0]+1:self.location[0]+1,self.location[1]:self.location[1] + self.size[1]] = np.full((self.size[0], self.size[1]),element)

class Character(Base):    
    def __init__(self):
        
        self.lives = 0
        self.health = 0
        self.velocity_y = -1 * GRAVITY

        self.right = []
        self.left = []
        self.down = []
        self.up = []

    
    def check_proximity(self, board):
        if self.location[1] + self.size[1] >= WIDTH:
            self.right = [100] * self.size[0]
        else:
            self.right=board[self.location[0]-self.size[0]+1:self.location[0]+1,self.location[1]+self.size[1]]

        if self.location[1] - 1 < 0:
            self.left = [100] * self.size[0]
        else:
            self.left = board[self.location[0]-self.size[0]+1:self.location[0]+1, self.location[1]-1]
        
        if self.location[0] - self.size[0] < 0:
            self.up = [100] * self.size[1]
        else:
            self.up = board[self.location[0] - self.size[0], self.location[1]:self.location[1] + self.size[1]]

        if self.location[0] + 1 >= HEIGHT:
            self.down = [100] * self.size[1]
        else:
            self.down = board[self.location[0] + 1,self.location[1]:self.location[1] + self.size[1]]
        
        print(f"right: {self.right}")
        print(f"left: {self.left}")
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def pick_coin(self, board, proximity):
        return np.count_nonzero(proximity == 1)

    def move(self, board, key,):
        
        score_delta = 0
        if key == 'd':
            #Check if there is space on the right
            if max(self.right) <= 1:
                score_delta += self.pick_coin(board, self.right)
                self.place(board, 0)
                self.location[1] += 1
                self.place(board, self.id)
            elif max(self.right) in [7,8,9,10]:
                return -1

        if key == 'a':
            #Check if there is space on the left
            if max(self.left) <= 1:
                score_delta += self.pick_coin(board, self.left)
                self.place(board, 0)
                self.location[1] -= 1
                self.place(board, self.id)
            elif max(self.left) in [7,8,9,10]:
                return -1

        if key == 'w':
            self.velocity_y += JUMP_VEL
            
        if self.velocity_y > 0:
            #Check if there is space on the top
            if max(self.up) <= 1:
                score_delta += self.pick_coin(board, self.up)
                self.place(board,0)
                self.location[0] -= 1
                self.place(board, self.id)
            elif max(self.up) in [7,8,9,10]:
                return -1
        
        elif self.velocity_y < 0:
            #Check if there is space in the bottom
            if max(self.down) <= 1:
                score_delta += self.pick_coin(board, self.down)
                self.place(board, 0)
                self.location[0] += 1
                self.place(board, self.id)
            elif max(self.down) in [7,8,9,10]:
                return -1
        
        self.velocity_y = -1
        return score_delta

class Mando(Character):
   
    def __init__(self, board):
        
        Character.__init__(self)
        self.id = 5
        self.lives = M_LIVES
        self.health = M_HEALTH
        self.size = M_SIZE
        self.location = M_INIT_LOCATION
        self.place(board, self.id)
        

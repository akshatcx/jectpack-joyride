import numpy as np
from config import *

class Base:
    def __init__(self):
        self.id = None
        self.size = []
        self.location = []

    def place(self, board, element):
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

    def move(self, board, key,):
        
        if key == 'd':
            #Check if there is space on the right
            if max(self.right) <= 1:
                self.place(board, 0)
                self.location[1] += 1
                self.place(board, self.id)

        if key == 'a':
            #Check if there is space on the left
            if max(self.left) <= 1:
                self.place(board, 0)
                self.location[1] -= 1
                self.place(board, self.id)

        if key == 'w':
            self.velocity_y += JUMP_VEL
            
        if self.velocity_y > 0:
            #Check if there is space on the top
            if max(self.up) <= 1:
                self.place(board,0)
                self.location[0] -= 1
                self.place(board, self.id)
        
        elif self.velocity_y < 0:
            #Check if there is space in the bottom
            if max(self.down) <= 1:
                self.place(board, 0)
                self.location[0] += 1
                self.place(board, self.id)
        
        self.velocity_y = -1

class Mando(Character):
   
    def __init__(self, board):
        
        Character.__init__(self)
        self.id = 1
        self.lives = M_LIVES
        self.health = M_HEALTH
        self.size = M_SIZE
        self.location = M_INIT_LOCATION
        self.place(board, self.id)
        

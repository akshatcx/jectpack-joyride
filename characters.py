import numpy as np
from config import *

class Character:
    
    def __init__(self):
        
        #Check inheritance contructor
        
        self.id = None
        self.lives = 0
        self.health = 0
        self.size = [0, 0]
        self.location = [0, 0]
        self.velocity_y = -1 * GRAVITY

        self.right = 0
        self.left = 0
        self.down = 0
        self.up = 0
    """
    @property
    def id(self):
        return self.id
    
    @property
    def location(self):
        return self.location
    
    @property
    def size(self):
        return self.size
    """

    def init_location(self, board):
        print(self.location)
        board[self.location[0] - self.size[0]+1:self.location[0]+1,self.location[1]:self.location[1] + self.size[1]] = np.full((self.size[0], self.size[1]),self.id)

    def check_proximity(self, board):
        if self.location[1] + self.size[1] >= WIDTH:
            self.right = -1
        else:
            self.right=max(board[self.location[0]-self.size[0]+1:self.location[0]+1,self.location[1]+self.size[1]])

        if self.location[1] - 1 < 0:
            self.left = -1
        else:
            self.left = max(board[self.location[0]-self.size[0]+1:self.location[0]+1, self.location[1]-1])
        
        if self.location[0] - self.size[0] < 0:
            self.up = -1
        else:
            self.up = max(board[self.location[0] - self.size[0], self.location[1]:self.location[1] + self.size[1]])

        if self.location[0] + 1 >= HEIGHT:
            self.down = -1
        else:
            self.down = max(board[self.location[0] + 1,self.location[1]:self.location[1] + self.size[1]])
        
        print(f"right: {self.right}")
        print(f"left: {self.left}")
        print(f"down: {self.down}")
        print(f"up: {self.up}")
    def move(self, board, key,):
        
        if key == 'd':
            #Check if there is space on the right
            if self.right == 0:
                board[self.location[0] - self.size[0] + 1:self.location[0] + 1,self.location[1]] = [0] * self.size[0]
                board[self.location[0]-self.size[0]+1:self.location[0]+1,self.location[1]+self.size[1]] = [self.id] * self.size[0]
                self.location[1] += 1

        if key == 'a':
            #Check if there is space on the left
            if self.left == 0:
                board[self.location[0]-self.size[0]+1:self.location[0]+1, self.location[1]+self.size[1]-1] = [0] * self.size[0]
                board[self.location[0]-self.size[0]+1:self.location[0]+1, self.location[1]-1] = [self.id] * self.size[0]
                self.location[1] -= 1

        if key == 'w':
            self.velocity_y += JUMP_VEL
            
        if self.velocity_y > 0:
            #Check if there is space on the top
            if self.up == 0:
                board[self.location[0], self.location[1]:self.location[1] + self.size[1]] = [0] * self.size[1]
                board[self.location[0] - self.size[0], self.location[1]:self.location[1] + self.size[1]] = [self.id] * self.size[1]
                self.location[0] -= 1
        
        elif self.velocity_y < 0:
            #Check if there is space in the bottom
            if self.down == 0:
                board[self.location[0] - self.size[0] + 1,self.location[1]:self.location[1] + self.size[1]] = [0] * self.size[1]
                board[self.location[0] + 1,self.location[1]:self.location[1] + self.size[1]] = [self.id] * self.size[1]
                self.location[0] += 1
        self.velocity_y = -1

class Mando(Character):
   
    def __init__(self):
        
        Character.__init__(self)
        self.id = 1
        self.lives = M_LIVES
        self.health = M_HEALTH
        self.size = M_SIZE
        self.location = M_INIT_LOCATION
        

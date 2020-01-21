import numpy as np
from config import *
from props import Bullet
from base import Base
import time

class Character(Base):
    def __init__(self):

        self.lives = 0
        self.health = 0
        self.velocity_y = -1 * GRAVITY
        
        self.weapons = []
        self.right = []
        self.left = []
        self.down = []
        self.up = []

    def check_proximity(self, board, frame):
        if self.location[1] + self.size[1] >= frame + HEIGHT*2 + 1:
            self.right = [100] * self.size[0]
        else:
            self.right = board[
                self.location[0] - self.size[0] + 1 : self.location[0] + 1,
                self.location[1] + self.size[1],
            ]

        if self.location[1] - 1 < frame:
            self.left = [100] * self.size[0]
        else:
            self.left = board[
                self.location[0] - self.size[0] + 1 : self.location[0] + 1,
                self.location[1] - 1,
            ]

        if self.location[0] - self.size[0] < 0:
            self.up = [100] * self.size[1]
        else:
            self.up = board[
                self.location[0] - self.size[0],
                self.location[1] : self.location[1] + self.size[1],
            ]

        if self.location[0] + 1 >= HEIGHT:
            self.down = [100] * self.size[1]
        else:
            self.down = board[
                self.location[0] + 1, self.location[1] : self.location[1] + self.size[1]
            ]

        # print(f"right: {self.right}")
        # print(f"left: {self.left}")
        # print(f"down: {self.down}")
        # print(f"up: {self.up}")


class Mando(Character):
    def __init__(self, board):

        Character.__init__(self)
        self.id = 5
        self.lives = M_LIVES
        self.health = M_HEALTH
        self.size = M_SIZE
        self.location = M_INIT_LOCATION
        self.place(board, self.id)
        self.shield = False
        self.stime = time.time() - 70

    def pick_coin(self, board, proximity):
        return np.count_nonzero(proximity == 1)

    def move(
        self, board, key, frame
    ):
        self.check_proximity(board, frame)
        score_delta = 0
        if key == "d":            
            # Check if there is space on the right
            if max(self.right) <= 1 or self.shield:
                score_delta += self.pick_coin(board, self.right)
                self.place(board, 0)
                self.location[1] += 1
                self.place(board, self.id)
            elif max(self.right) in [7, 8, 9, 10] and self.shield == False:
                self.lives -= 1

        if key == "a":
            # Check if there is space on the left
            if max(self.left) <= 1 or self.shield:
                score_delta += self.pick_coin(board, self.left)
                self.place(board, 0)
                self.location[1] -= 1
                self.place(board, self.id)
            elif max(self.left) in [7, 8, 9, 10]:
                self.lives -= 1

        if key == "w":
            self.velocity_y += JUMP_VEL

        if self.velocity_y > 0:
            # Check if there is space on the top
            if max(self.up) <= 1 or self.shield:
                score_delta += self.pick_coin(board, self.up)
                self.place(board, 0)
                self.location[0] -= 1
                self.place(board, self.id)
            elif max(self.up) in [7, 8, 9, 10]:
                self.lives -= 1

        elif self.velocity_y < 0:
            # Check if there is space in the bottom
            if (max(self.down) <= 1 or self.shield) and max(self.down) != 6:
                score_delta += self.pick_coin(board, self.down)
                self.place(board, 0)
                self.location[0] += 1
                self.place(board, self.id)
            elif max(self.down) in [7, 8, 9, 10]:
                self.lives -= 1

        self.velocity_y = -1
        

        if key == "e":
            bullet = Bullet(board, [self.location[0] - self.size[0] +1,self.location[1] + self.size[1]])
            self.weapons.append(bullet)
            print(self.weapons)
        
        return score_delta

    def move_relative(self, board, frame):
        score_delta = 0
        self.check_proximity(board, frame)
        if max(self.right) <= 1 or self.shield:
                score_delta += self.pick_coin(board, self.right)
                self.place(board, 0)
                self.location[1] += 1
                self.place(board, self.id)
        elif max(self.right) in [7, 8, 9, 10] and self.shield == False:
            self.lives -= 1
        return score_delta

    def upd_att(self, board, key):
        for weapon in self.weapons:
            weapon.advance(board)
            weapon.advance(board)
        
        if key == "z":
            if time.time() - self.stime >= 70:
                self.stime = time.time()
                self.shield = True
                self.id = 11
                self.place(board, self.id)

        if self.shield and time.time() - self.stime >= 10:
            self.shield = False
            self.id = 5
    
    

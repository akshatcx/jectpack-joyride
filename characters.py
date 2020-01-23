import numpy as np
from config import *
from props import Bullet, IceBall
from base import Base
import time
from utils import *
import sys


class Character(Base):
    def __init__(self):

        self._lives = 0
        self._velocity_y = 0

        self._weapons = []
        self._right = []
        self._left = []
        self._down = []
        self._up = []

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, var):
        self._lives = var
    
    @property
    def velocity_y(self):
        return self._velocity_y

    @velocity_y.setter
    def velocity_y(self, var):
        self._velocity_y = var

    def check_proximity(self, board, frame):
        if self.location[1] + self.size[1] >= frame + HEIGHT * 2 + 1:
            self._right = [-1] * self.size[0]
        else:
            self._right = board[
                self.location[0] - self.size[0] + 1 : self.location[0] + 1,
                self.location[1] + self.size[1],
            ]

        if self.location[1] - 1 < frame:
            self._left = [-1] * self.size[0]
        else:
            self._left = board[
                self.location[0] - self.size[0] + 1 : self.location[0] + 1,
                self.location[1] - 1,
            ]

        if self.location[0] - self.size[0] < 0:
            self._up = [-1] * self.size[1]
        else:
            self._up = board[
                self.location[0] - self.size[0],
                self.location[1] : self.location[1] + self.size[1],
            ]

        if self.location[0] + 1 >= HEIGHT:
            self._down = [-1] * self.size[1]
        else:
            self._down = board[
                self.location[0] + 1, self.location[1] : self.location[1] + self.size[1]
            ]


class Mando(Character):
    def __init__(self, board):

        Character.__init__(self)
        self.id = 5
        self.lives = M_LIVES
        self.size = M_SIZE
        self.location = M_INIT_LOCATION
        self.place(board, self.id)
        self.__shield = False
        self.__stime = time.time() - 70
        self.__fast = False
        self.__ftime = time.time() - 5
        self.__tail = [1,0,1,2,1,0,1,2,1,0,1,2]
        self.__dragon = False
        self.__dflag = False

    def activate_dragon(self):
        if not self.__dflag:
            self.__dragon = True
            self.__dflag = True

    def pick_coin(self, board, proximity):
        return np.count_nonzero(proximity == 1)

    def powerup(self, proximity):
        if 2 in proximity:
            self.__ftime = time.time()
            self.__fast = True

    def frate(self):
        if self.__fast:
            return 2
        return 1

    def move(self, board, key, frame):
        self.check_proximity(board, frame)
        score_delta = 0
        if key == "d":
            self.powerup(self._right)
            # Check if there is space on the right
            if max(self._right) in [7, 8, 9, 10, 15] and not self.__shield:
                if self.__dragon:
                    self.__dragon = False
                else:
                    self.lives -= 1
            if -1 not in self._right:
                score_delta += self.pick_coin(board, self._right)
                self.place(board, 0)
                self.location[1] += 1
                self.place(board, self.id)
            

        if key == "a":
            self.powerup(self._left)
            # Check if there is space on the left
            if max(self._left) in [7, 8, 9, 10, 15] and not self.__shield:
                if self.__dragon:
                    self.__dragon = False
                else:
                    self.lives -= 1
            if -1 not in self._left:
                score_delta += self.pick_coin(board, self._left)
                self.place(board, 0)
                self.location[1] -= 1
                self.place(board, self.id)
            

        if key == "w":
            self.powerup(self._up)
            # Check if there is space on the top
            if max(self._up) in [7, 8, 9, 10, 15] and not self.__shield:
                if self.__dragon:
                    self.__dragon = False
                else:
                    self.lives -= 1
            if -1 not in self._up:
                score_delta += self.pick_coin(board, self._up)
                self.place(board, 0)
                self.location[0] -= 1
                self.place(board, self.id)
            
            self.velocity_y = 0

        
        self.velocity_y += GRAVITY
        
        for i in range(int(self.velocity_y)):
            self.check_proximity(board, frame)
            self.powerup(self._down)
            # Check if there is space in the bottom
            if max(self._down) in [7, 8, 9, 10, 15] and not self.__shield:
                if self.__dragon:
                    self.__dragon = False
                else:
                    self.lives -= 1
            if -1 not in self._down and 6 not in self._down:
                score_delta += self.pick_coin(board, self._down)
                self.place(board, 0)
                self.location[0] += 1
                self.place(board, self.id)
            


        if key == "e":
            bullet = Bullet(
                board,
                [self.location[0] - self.size[0] + 1, self.location[1] + self.size[1]],
            )
            self._weapons.append(bullet)
            print(self._weapons)

        self.render_tail(board)

        return score_delta

    def checkmag(self, board, frame):
        if (
            3
            in board[
                maxh(self.location[0] - 20) : maxh(self.location[0] + 20),
                maxw(self.location[1] - 40) : maxw(self.location[1] + 40),
            ]
        ):
            mag_loc = np.where(board == 3)
            #if int(mag_loc[0]) > self.location[0]:
            #    self.move(board, "", frame)
            #elif int(mag_loc[0]) < self.location[0]:
            #    self.move(board, "w", frame)
            if int(mag_loc[1]) > self.location[1]:
                self.move(board, "d", frame)
            elif int(mag_loc[1]) < self.location[1]:
                self.move(board, "a", frame)

    def move_relative(self, board, frame):
        score_delta = 0
        self.check_proximity(board, frame)
        self.powerup(self._right)
        if max(self._right) in [7, 8, 9, 10, 15] and not self.__shield:
            if self.__dragon:
                self.__dragon = False
            else:
                self.lives -= 1
        if -1 not in self._right:
            score_delta += self.pick_coin(board, self._right)
            self.place(board, 0)
            self.location[1] += 1
            self.place(board, self.id)
        
        return score_delta

    def upd_att(self, board, key, frame):
        for weapon in self._weapons:
            weapon.advance(board)
            if self.__fast:
                weapon.advance(board)
            if frame < WIDTH - ENEMY_OFFSET:
                weapon.advance(board)

        if key == " ":
            if time.time() - self.__stime >= 70:
                self.__stime = time.time()
                self.__shield = True
                self.id = 11
                self.place(board, self.id)

        if key == "q":
            sys.exit()

        if self.__fast and time.time() - self.__ftime >= 5:
            self.__fast = False
        if self.__shield and time.time() - self.__stime >= 10:
            self.__shield = False
            self.id = 5

    def render_tail(self, board):
        if self.__dragon:
            self.__tail = np.roll(self.__tail,1)
            board[self.location[0]-4:self.location[0]+1, self.location[1]-len((self.__tail))-4:self.location[1] - 1] = np.full((5,len(self.__tail)+3),0)
            for piece, i in zip(self.__tail, range(len(self.__tail))):
                board[self.location[0] - piece - 1:self.location[0] -piece + 1, self.location[1] -i -1] = [self.id]*2
            
            board[self.location[0] - self.size[0], self.location[1]+self.size[1]:self.location[1] + self.size[1] + 4] = [30]*4

class Enemy(Character):
    def __init__(self, board):
        super().__init__()
        self.id = 14
        self.lives = E_LIVES
        self.health = E_HEALTH
        self.size = E_SIZE
        self.location = E_INIT_LOCATION
        self.place(board, self.id)

    def move(self, board, location):
        self.place(board, 0)
        self.location[0] = location[0]
        self.place(board, self.id)

    def shoot(self, board):
        ice = IceBall(
            board, [self.location[0] - self.size[0] + 1, self.location[1] - 1]
        )
        self._weapons.append(ice)

    def move_ice(self, board):
        for ice in self._weapons:
            ice.advance(board)
        self._left = board[
            self.location[0] - self.size[0] + 1 : self.location[0] + 1,
            self.location[1] - 1,
        ]
        if 4 in self._left:
            self.lives -= 1

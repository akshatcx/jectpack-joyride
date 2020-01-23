from base import Base
from config import *
import random
import numpy as np


class Floor(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 6
        self.location = location
        self.size = F_SIZE
        self.place(board, self.id)


class Coin(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 1
        self.location = location
        self.size = C_SIZE


class Lazer_H(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 8
        self.location = location
        self.size = LH_SIZE


class Lazer_V(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 7
        self.location = location
        self.size = LV_SIZE


class Lazer_D1(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 9
        self.location = location
        self.size = LD_SIZE

    def place(self, board, element):
        lazer = np.zeros(self.size)
        for i in range(self.size[0]):
            lazer[i, self.size[1] - i - 2 : self.size[1] - i] = element
        board[
            self.location[0] - self.size[0] + 1 : self.location[0] + 1,
            self.location[1] : self.location[1] + self.size[1],
        ] = lazer


class Lazer_D2(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 10
        self.location = location
        self.size = LD_SIZE

    def place(self, board, element):
        lazer = np.zeros(self.size)
        for i in range(self.size[0]):
            lazer[i, i : i + 2] = element

        board[
            self.location[0] - self.size[0] + 1 : self.location[0] + 1,
            self.location[1] : self.location[1] + self.size[1],
        ] = lazer


class Magnet(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 3
        self.location = location
        self.size = MG_SIZE


class Powerup(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 2
        self.location = location
        self.size = P_SIZE


class Bullet(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 4
        self.location = location
        self.size = B_SIZE
        self.dead = False

    def destroy(self, board):
        if self.location[1] + 1 >= WIDTH:
            self.dead = True
            return True
        if board[self.location[0], self.location[1] + 1] == 14:
            self.place(board, 0)
            self.dead = True
        if board[self.location[0], self.location[1] + 1] in [1, 7, 8, 9, 10, 15]:
            self.location[1] += 1
            board[
                self.location[0] - 1 : self.location[0] + 2,
                self.location[1] : self.location[1] + 3,
            ] = np.zeros([3, 3])
            self.dead = True
            return self.dead

    def advance(self, board):
        if self.dead == False:
            self.place(board, 0)
            if self.destroy(board) == True:
                return
            self.location[1] += 1
            self.place(board, self.id)


class IceBall(Base):
    def __init__(self, board, location):
        super().__init__()
        self.id = 15
        self.location = location
        self.size = I_SIZE
        self.dead = False

    def advance(self, board):
        if self.dead == False:
            self.place(board, 0)
            if self.location[1] - 1 < WIDTH - ENEMY_OFFSET or board[
                self.location[0], self.location[1] - 1
            ] in [4, 5]:
                self.place(board, 0)
                self.dead = True
                return
            self.location[1] -= 1
            self.place(board, self.id)

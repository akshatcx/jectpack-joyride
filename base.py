import numpy as np
from config import *

class Base:
    def __init__(self):
        self.id = None
        self.size = []
        self.location = []

    def place(self, board, element):
        # print(f"location: {self.location}")
        # print(f"size: {self.size}")
        board[
            self.location[0] - self.size[0] + 1 : self.location[0] + 1,
            self.location[1] : self.location[1] + self.size[1],
        ] = np.full((self.size[0], self.size[1]), element)


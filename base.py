import numpy as np
from config import *


class Base:
    def __init__(self):
        self._id = None
        self._size = []
        self._location = []

    def place(self, board, element):
        # print(f"location: {self.location}")
        # print(f"size: {self.size}")
        board[
            self.location[0] - self.size[0] + 1 : self.location[0] + 1,
            self.location[1] : self.location[1] + self.size[1],
        ] = np.full((self.size[0], self.size[1]), element)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, var):
        self._id = var

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, var):
        self._size = var

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, var):
        self._location = var

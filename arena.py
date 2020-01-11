import numpy as np
from colorama import Fore, Back, Style 

from config import *

class Arena:
    """Represents a single screen
    """

    def __init__(self):
        self.board = self.gen_board()

    def gen_board(self):
        new_board = np.zeros((HEIGHT, WIDTH))
        new_board[56:64, :] = 6
        return new_board

    def render(self):
        trackc = 0
        
        color_mappings = {
            0: Back.Black + Fore.Black + ' ',
            6: Back.Blue + ' ',
        }

        for row in board:
            for pixel in row:
                print(color_mappings[pixel])

        print(Style.RESET_ALL + '')

    

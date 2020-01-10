import numpy as np
from colorama import Fore, Back, Style 

from config import all

class Arena:
    """Represents a single screen
    """

    def __init__(self, engine):
        self.engine = engine
        self.board = self.gen_board()

    def gen_scene():
        board = np.array([[0 for col in range(WIDTH)]
                            for row in range(HEIGHT)])
        board[56:64] = [[6] * WIDTH]*8
        return board

    def render():
        trackc = 0
        
        color_mappings = {
            0: Back.Black + Fore.Black + ' ',
            6: Back.Blue + ' ',
        }

        for row in board:
            for pixel in row:
                print(color_mappings[pixel])

        print(Style.RESET_ALL + '')
    
    def board(self, x, y):
        return board[x][y]



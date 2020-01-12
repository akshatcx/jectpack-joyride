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
        new_board[int((HEIGHT*7)/8):HEIGHT] = 6
        return new_board

    def render(self):
        trackc = 0
        
        color_mappings = {
            0: Back.GREEN + Fore.BLACK + '.',
            1: Back.RED + Fore.BLACK + '.',
            6: Back.BLUE + Fore.BLACK + '.',
            
        }

        for row in self.board:
            for pixel in row:
                print(color_mappings[pixel], end='')
                #print(pixel, end='')
            print(Style.RESET_ALL + '')
            #print()

    
